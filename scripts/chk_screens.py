import json
import sys

sys.stdout.reconfigure(encoding="utf-8")
j = json.load(open(sys.argv[1], encoding="utf8"))
s = j["screens"]
print(len(s), list(s[0].keys()))
for x in s:
    t = x.get("title", "")
    if "G11" in t or "Mai" in t:
        print(x.get("name"), "|", t)
