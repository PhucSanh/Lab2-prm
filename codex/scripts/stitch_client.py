import json, subprocess, urllib.request, sys
from pathlib import Path
class Client:
 def __init__(self):
  r=subprocess.run(['/usr/bin/python3','/home/qhius/.config/codex/stitch_headers.py'],capture_output=True,text=True,check=True)
  self.h=json.loads(r.stdout); self.h.update({'Content-Type':'application/json','Accept':'application/json, text/event-stream'})
  x=self.rpc('initialize',{'protocolVersion':'2024-11-05','capabilities':{},'clientInfo':{'name':'codex-hieu-loop','version':'1'}})
  self.h['MCP-Protocol-Version']=x.get('protocolVersion','2024-11-05')
 def rpc(self,method,params):
  req=urllib.request.Request('https://stitch.googleapis.com/mcp',data=json.dumps({'jsonrpc':'2.0','id':1,'method':method,'params':params}).encode(),headers=self.h,method='POST')
  with urllib.request.urlopen(req,timeout=600) as r:
   raw=r.read().decode()
   if r.headers.get('Mcp-Session-Id'):self.h['Mcp-Session-Id']=r.headers['Mcp-Session-Id']
  if raw.startswith('data:') or 'event:' in raw:raw=[v[5:].strip() for v in raw.splitlines() if v.startswith('data:')][-1]
  x=json.loads(raw)
  if 'error' in x:raise RuntimeError(json.dumps(x['error']))
  return x.get('result',{})
 def tool(self,name,args):
  x=self.rpc('tools/call',{'name':name,'arguments':args})
  if x.get('isError'):raise RuntimeError(json.dumps(x))
  for c in x.get('content',[]):
   if c.get('type')=='text':
    try:return json.loads(c['text'])
    except ValueError:pass
  return x
