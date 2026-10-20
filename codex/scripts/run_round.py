"""Execute one authorized Stitch round; review and edit prompts stay agent-owned."""
from pathlib import Path
from datetime import datetime, timezone
import json,sys,subprocess,urllib.request,fcntl
from stitch_client import Client
ROOT=Path(__file__).resolve().parents[2]
code=sys.argv[1];n=int(sys.argv[2]);mode=sys.argv[3]
out=ROOT/'codex-runs'/code
s=json.loads((out/'state.json').read_text())
def write_state():
 s['updated_at']=datetime.now(timezone.utc).isoformat();tmp=out/'state.tmp';tmp.write_text(json.dumps(s,ensure_ascii=False,indent=2));tmp.replace(out/'state.json')
def redact(x):
 if isinstance(x,dict):return {k:('[URL omitted]' if 'url' in k.lower() else redact(v)) for k,v in x.items()}
 if isinstance(x,list):return [redact(v) for v in x]
 return x
def find_screens(x):
 if isinstance(x,dict):
  if '/screens/' in x.get('name','') and ('screenshot' in x or 'htmlCode' in x):yield x
  for v in x.values():yield from find_screens(v)
 elif isinstance(x,list):
  for v in x:yield from find_screens(v)
c=Client();s['round']=n;s['status']='running';s['prompt_path']=str(out/(f'v{n-1}-edit-prompt.txt' if mode=='edit' else 'v0-prompt.txt'));write_state()
response_path=out/f'v{n}-response.json'
if mode in ['generate','edit'] and response_path.exists():raise SystemExit('Response exists; recover with fetch, do not generate twice.')
if mode=='generate':r=c.tool('generate_screen_from_text',{'projectId':s['project_id'],'prompt':(out/'v0-prompt.txt').read_text(),'deviceType':'MOBILE'})
elif mode=='edit':
 s['parent_screen_id']=s['best_screen_id'];write_state()
 r=c.tool('edit_screens',{'projectId':s['project_id'],'selectedScreenIds':[s['best_screen_id']],'prompt':(out/f'v{n-1}-edit-prompt.txt').read_text(),'deviceType':'MOBILE'})
elif mode=='fetch':r={'name':f"projects/{s['project_id']}/screens/{s['screen_id']}"}
else:raise ValueError(mode)
if mode!='fetch':response_path.write_text(json.dumps(redact(r),ensure_ascii=False,indent=2))
screens=list(find_screens(r)) or ([r] if mode=='fetch' else [])
if not screens:
 s.update(status='BLOCKED',stop_reason='response_without_screen');write_state();print('BLOCKED: response has no screen; inspect sanitized response before retry.');raise SystemExit(2)
screen=screens[0];sid=screen['name'].split('/')[-1]
if mode=='edit' and sid==s['parent_screen_id']:
 s.update(status='BLOCKED',stop_reason='edit_reused_source_id');write_state();raise SystemExit('Edit did not create a new screen ID.')
s['screen_id']=sid;write_state();screen=c.tool('get_screen',{'name':f"projects/{s['project_id']}/screens/{sid}"})
(out/f'v{n}-screen.json').write_text(json.dumps(redact(screen),ensure_ascii=False,indent=2))
# Canvas membership is committed before review; existing frames are preserved verbatim.
with (ROOT/'codex-runs/.canvas.lock').open('a') as canvas_lock:
 fcntl.flock(canvas_lock,fcntl.LOCK_EX)
 pname='projects/'+s['project_id'];p=c.tool('get_project',{'name':pname});instances=p.get('screenInstances',[])
 source=pname+'/screens/'+sid
 if not any(v.get('sourceScreen')==source for v in instances):
  (out/f'v{n}-canvas-before.json').write_text(json.dumps(instances,ensure_ascii=False,indent=2))
  row=s['canvas_row'];x=n*1344;y=-2304-row*1536
  height=round(float(screen.get('height',2048))/float(screen.get('width',2560))*1280)
  entry={'id':sid,'sourceScreen':source,'x':x,'y':y,'width':1280,'height':height,'label':'An Nhiên - '+s['title']+(f' (Cập nhật v{n})' if n else '')}
  latest=c.tool('get_project',{'name':pname}).get('screenInstances',[])
  if latest!=instances:
   s.update(status='CANVAS_PENDING',stop_reason='concurrent_canvas_change');write_state();raise SystemExit('Canvas changed concurrently; generation retained, recover with fetch.')
  headers=json.loads(subprocess.run(['/usr/bin/python3','/home/qhius/.config/codex/stitch_headers.py'],capture_output=True,text=True,check=True).stdout);headers['Content-Type']='application/json'
  req=urllib.request.Request('https://stitch.googleapis.com/v1/'+pname+'?updateMask=screenInstances',data=json.dumps({'screenInstances':instances+[entry]}).encode(),headers=headers,method='PATCH')
  with urllib.request.urlopen(req,timeout=45) as response:response.read()
  after=c.tool('get_project',{'name':pname}).get('screenInstances',[]);lookup={v['id']:v for v in after}
  assert all(lookup.get(v['id'])==v for v in instances),'Unexpected modification of existing frames'
  assert lookup.get(sid,{}).get('sourceScreen')==source,'New canvas entry missing'
  (out/f'v{n}-canvas-verification.json').write_text(json.dumps({'canvas_instance':lookup[sid],'other_instances_unchanged':True,'ui_confirmed':False},ensure_ascii=False,indent=2))
  s['delivery_status']='API_CANVAS_MEMBERSHIP_VERIFIED_UI_UNCONFIRMED';write_state()
for field,ext in [('screenshot','png'),('htmlCode','html')]:
 url=screen.get(field,{}).get('downloadUrl')
 if not url:raise RuntimeError('Missing artifact '+field)
 with urllib.request.urlopen(url,timeout=60) as response:data=response.read()
 if not data:raise RuntimeError('Empty artifact '+field)
 (out/f'v{n}.{ext}').write_bytes(data)
s['stage']='awaiting_review';write_state()
print(json.dumps({'screen':code,'round':n,'screen_id':sid,'canvas_exported':True,'title':screen.get('title'),'artifacts_downloaded':True},ensure_ascii=False))
