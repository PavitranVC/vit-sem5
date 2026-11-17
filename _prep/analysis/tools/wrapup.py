"""Phase 5: merge all subjects into _prep/analysis/questions.csv and write _prep/analysis/report.md (tables only).
Run: python -I _prep/analysis/tools/wrapup.py
"""
import csv, json, re, collections

B = "_prep/analysis"
SUBJ = ["ai", "dbs", "cn", "cd", "os", "aws"]
CORE = {"ai": "BCSE306L", "os": "BCSE303L", "aws": "BCSE355L", "dbs": "BCSE302L", "cn": "BCSE308L", "cd": "BCSE307L"}
SLOT = {"ai": "C2", "dbs": "D2", "cn": "F2", "cd": "G2", "os": "done", "aws": "done"}

rows_all, header = [], None
for s in SUBJ:
    with open(f"{B}/{s}/questions.csv", encoding="utf-8") as fh:
        rd = csv.reader(fh, delimiter="|")
        h = next(rd)
        header = header or h
        for r in rd:
            d = dict(zip(h, r))
            rows_all.append([d.get(c, "") for c in header])
with open(f"{B}/questions.csv", "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh, delimiter="|")
    w.writerow(header)
    w.writerows(rows_all)

inv = list(csv.DictReader(open(f"{B}/inventory.csv", encoding="utf-8"), delimiter="|"))
bt = json.load(open(f"{B}/backtest_summary.json"))


def val(s):
    t = open(f"{B}/{s}/validation.md", encoding="utf-8").read()
    return int(re.search(r"questions: (\d+)", t).group(1)), t.count("| FLAG |"), int(re.search(r"ocr_flag=1: (\d+)", t).group(1))


L = ["# FAT pattern analysis: summary (Fall 2026-27)", "",
     "Per-subject detail: `<subject>/report.md` and `<subject>/patterns.json`. All rows: `questions.csv` (pipe-delimited). "
     "O = observed count, I = inferred. Probability = (2k_recent + k_older + 1)/(2n_recent + n_older + 2) over the course's FATs. Read as ranks, not chances.", "",
     "## Corpus and validation", "",
     "| subject | slot | rows | papers flagged on marks | rows ocr_flag=1 | orchestrator re-read: rows, pooled tag agreement | FATs used (2026-27) |",
     "|---|---|---|---|---|---|---|"]
for s in SUBJ:
    n, fl, oc = val(s)
    p = json.load(open(f"{B}/{s}/patterns.json", encoding="utf-8")) if s in ("ai", "dbs", "cn", "cd") else None
    if s == "ai":
        rr = "35, 0.886"
        fats = "7 (1)"
    elif p:
        v = json.load(open(f"{B}/{s}/verification.json", encoding="utf-8"))
        rr = f'{v["sampled_rows"]}, {v["pooled_rate"]}'
        ar = json.load(open(f"{B}/{s}/analysis_raw.json", encoding="utf-8"))
        nf = sum(1 for x in ar["papers_core"].values() if x["exam"] == "FAT"); nr = sum(1 for x in ar["papers_core"].values() if x["exam"] == "FAT" and x["recent"])
        fats = f"{nf} ({nr})"
    else:
        rr = "not re-read (backtest only)"
        ar = json.load(open(f"{B}/{s}/analysis_raw.json", encoding="utf-8"))
        nf = sum(1 for x in ar["papers_core"].values() if x["exam"] == "FAT"); nr = sum(1 for x in ar["papers_core"].values() if x["exam"] == "FAT" and x["recent"])
        fats = f"{nf} ({nr})"
    L.append(f"| {s.upper()} {CORE[s]} | {SLOT[s]} | {n} | {fl} | {oc} | {rr} | {fats} |")
L += ["", f"Inventory: {len(inv)} PDFs, {sum(1 for x in inv if not x['duplicate_of'])} unique by hash; {sum(1 for x in inv if x['path'].endswith('-AK.pdf'))} files end in -AK.pdf; "
      f"{sum(int(x['is_answer_key']) for x in inv)} answer keys by name ({sum(int(x['is_answer_key']) for x in inv if not x['duplicate_of'])} unique). "
      f"Backtest (OS+AWS, 4 slot-2 FATs): {bt['hits']} of {bt['of']} top-10 topics hit, tier {bt['tier']}; plain frequency also {bt['naive_hits']} of {bt['of']}.", ""]

for s in ("ai", "dbs", "cn", "cd"):
    p = json.load(open(f"{B}/{s}/patterns.json", encoding="utf-8"))
    m = p["meta"]
    L += [f"## {m['subject']}: slot {m['student_slot']}", "",
          "| rank | topic | module | p | FAT ratio | 2026-27 evidence | core type |", "|---|---|---|---|---|---|---|"]
    for t in p["predicted_topics"][:12]:
        name = t.get("topic_name")
        if s == "ai":
            rec = t["recent_ratio"]
        else:
            rec = f'CATs {t["core_2026_27_cat_ratio"]}; sister FATs {t["sister_2026_27_fat_ratio"]}'
        L.append(f'| {t["rank"]} | {name} | {t["module"]} | {t["probability"]:.2f} | {t["appearance_ratio"].replace(" FATs","")} | {rec} | {t["core_type"]} |')
    sp = p["slot_pair_hit_rates"]
    L += ["", "| finding | value |", "|---|---|",
          f'| slot 1 -> slot 2 same archetype | {sp["Same concept new numbers"]:.2f} ({sp["_n"]}) vs different-year baseline {sp["_baseline_different_year_same_concept"]:.2f} (O) |',
          f'| identical questions slot 1 -> slot 2 | {sp["Identical"]:.2f} (O) |',
          f'| backtest confidence | {m["backtest_confidence"]["tier"]} ({m["backtest_confidence"]["hits"]} of {m["backtest_confidence"]["of"]}) |',
          f'| tag agreement (orchestrator re-read) | {m["tag_agreement_rate"]} |',
          f'| no clear pattern | {"; ".join(p["no_clear_pattern"][:3])} |', ""]

open(f"{B}/report.md", "w", encoding="utf-8").write("\n".join(L) + "\n")
print("questions.csv rows:", len(rows_all), "| report.md written")
