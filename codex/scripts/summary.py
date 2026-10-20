from pathlib import Path
import json,re
root=Path(__file__).resolve().parents[2]
lines=(root/'CHIA-VIEC.md').read_text().splitlines()
rows=[]
for line in lines:
 p=[v.strip() for v in line.split('|')]
 if len(p)>4 and re.fullmatch(r'B\d\d',p[1]):rows.append((p[1],p[2],p[3]))
out=['# Tiến độ làn B — Codex','','Project đang dùng: `2013215887278758682` — An Nhiên của Sanh. Mỗi phiên bản được giữ riêng trên canvas; chưa export Figma.','','| Task | Mã | Màn | Trạng thái | Điểm các vòng | Bản tốt nhất |','|---|---|---|---|---|---|']
for task,code,title in rows:
 folder=root/'codex-runs'/code;state=folder/'state.json'
 if not state.exists():out.append(f'|{task}|{code}|{title}|Chưa chạy|—|—|');continue
 s=json.loads(state.read_text());critiques=[]
 for f in sorted(folder.glob('v[0-9]*-critique.json'),key=lambda p:int(re.search(r'v(\d+)',p.name)[1])):
  q=json.loads(f.read_text());critiques.append(f"v{q['round']}:{q['score']}")
 best=f"v{s['best_round']}" if s.get('best_round') is not None else '—'
 out.append(f"|{task}|[{code}]({code}/log.md)|{title}|{s['status']}|{' → '.join(critiques) or '—'}|{best}|")
out+=['','`API_CANVAS_MEMBERSHIP_VERIFIED` xác nhận instance qua API; không tự nhận đã nhìn thấy UI trình duyệt.','Lịch sử project riêng dùng nhầm trước đó giữ trong `archive/`.']
(root/'codex-runs/SUMMARY.md').write_text('\n'.join(out)+'\n')
