from pathlib import Path
import json,re,sys
from datetime import datetime,timezone
root=Path(__file__).resolve().parents[2];code=sys.argv[1];out=root/'codex-runs'/code;n=int(sys.argv[2]);c=json.loads((out/f'v{n}-critique.json').read_text());s=json.loads((out/'state.json').read_text())
rules=[]
for line in (root/'rule.md').read_text().splitlines():
 parts=[v.strip() for v in line.split('|')]
 if len(parts)>4 and re.fullmatch('R-[A-Z]+-[0-9]+',parts[1]):rules.append((parts[1],parts[-3],parts[-2]))
assert [v['rule'] for v in c['results']]==[v[0] for v in rules]
for r,v in zip(rules,c['results']):
 assert (v['level'],v['check'])==r[1:]
 assert v['status'] in ['pass','fail','n/a']
 if v['status']=='fail':assert all(v.get(k) for k in ['where','evidence','fix'])
errors=sum(v['status']=='fail' and v['level']=='error' for v in c['results']);warns=sum(v['status']=='fail' and v['level']=='warn' for v in c['results'])
assert (c['errors'],c['warns'],c['score'])==(errors,warns,max(0,100-10*errors-3*warns))
if s.get('last_processed_round') != n:
 old=s['best_score'];s['patience']=0 if old is None or c['score']>old else s['patience']+1
 if old is None or c['score']>old or (c['score']==old and c['errors']<=json.loads((out/f"v{s['best_round']}-critique.json").read_text())['errors']):
  s.update(best_round=n,best_score=c['score'],best_screen_id=s['screen_id'])
 s['last_processed_round']=n
best=json.loads((out/f"v{s['best_round']}-critique.json").read_text());reason='score_100' if c['score']==100 else 'patience_2' if s['patience']>=2 else 'v8' if n>=8 else None
if reason:s.update(status='NEEDS_HUMAN' if best['errors'] else 'MAX_ROUNDS' if reason=='v8' else 'CONVERGED',stop_reason=reason)
s['updated_at']=datetime.now(timezone.utc).isoformat();tmp=out/'state.tmp';tmp.write_text(json.dumps(s,ensure_ascii=False,indent=2));tmp.replace(out/'state.json')
rows=[]
for k in range(n+1):
 critique_path=out/f'v{k}-critique.json'
 if not critique_path.exists():
  attempt_path=out/f'v{k}-attempt-response.json'
  assert attempt_path.exists(), f'Missing critique and attempt record for v{k}'
  rows.append(f"| v{k} | Không sinh màn | — | — | — | — |")
  continue
 q=json.loads(critique_path.read_text());rows.append(f"| v{k} | {q['score']} | {q['errors']} | {q['warns']} | {', '.join(q['fixed']) or '—'} | {', '.join(q['regressions']) or '—'} |")
log=f"# {code} — {s.get('title',code)}\n\nProject: `{s['project_id']}` — An Nhiên (project của Sanh)\n\n**Màn chốt hiện tại: v{s['best_round']} — {s['best_score']} điểm**\n\nScreen ID: `{s['best_screen_id']}`\n\n**Kết quả: {s['status']}** · stop_reason: {s['stop_reason'] or 'đang lặp'}\n\n| Vòng | Điểm | Error | Warn | Đã sửa | Regression |\n|---|---:|---:|---:|---|---|\n"+'\n'.join(rows)+'\n'
for k in range(n+1):
 critique_path=out/f'v{k}-critique.json'
 if not critique_path.exists():
  attempt=json.loads((out/f'v{k}-attempt-response.json').read_text())
  log+=f"\n## v{k} — không sinh màn\n\nStitch trả về nội dung kế hoạch thay vì screen; không chấm vòng này. Phản hồi đã lưu tại `v{k}-attempt-response.json`.\n\n"
  continue
 q=json.loads(critique_path.read_text());screen=json.loads((out/f'v{k}-screen.json').read_text())
 log+=f"\n## v{k} — {q['score']} điểm\n\nScreen: `{screen['name']}`\n\n![Stitch v{k}](v{k}.png)\n\n![Viewport 360px](v{k}-viewport-360.png)\n\n"
 for item in q['results']:
  if item['status']=='fail':log+=f"- {item['rule']} ({item['level']}): {item['where']}. Bằng chứng: {item['evidence']}. Sửa: {item['fix']}\n"
 log+='\n'+q['summary']+'\n'
 edit=out/f'v{k}-edit-prompt.txt'
 if edit.exists():log+='\n### Edit prompt\n\n```text\n'+edit.read_text()+'\n```\n'
(out/'log.md').write_text(log)
print(json.dumps({'score':c['score'],'best_round':s['best_round'],'status':s['status'],'patience':s['patience'],'fails':[v for v in c['results'] if v['status']=='fail']},ensure_ascii=False))
