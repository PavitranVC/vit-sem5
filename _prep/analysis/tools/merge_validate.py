"""Merge extractor shards into questions.csv / questions_text.jsonl and validate.

Usage: python -I merge_validate.py <subject_prefix> [<subject_prefix> ...]
e.g.   python -I _prep/analysis/tools/merge_validate.py AI
Run from the repo root. Reads _prep/analysis/shards/<PREFIX>-*.jsonl.
Writes _prep/analysis/<subject>/questions.csv, questions_text.jsonl, papers.json, validation.md
"""
import csv, glob, json, os, re, sys
from collections import defaultdict, Counter

BASE = "_prep/analysis"
COLS = ["subject", "course_code", "year", "exam", "slot", "q_no", "marks", "syllabus_module", "type",
        "bloom_level", "file_name", "has_scenario_wrapper", "one_line_core_task", "ocr_flag",
        "topic", "or_group", "has_figure", "page", "is_answer_key", "step_marks", "required_keywords",
        "penalties", "key_final_answer", "batch_id", "marks_imputed"]
TYPES = {"numerical", "trace", "theory", "scenario"}
# Files whose filename year is wrong (verified from the printed header). Never rename the PDFs.
# Files excluded after header check (misfiled; PDFs untouched)
EXCLUDE = {"CN/PYQ/FAT/BCSE308L - FAT - B1 - 2024 - Question Paper (2).pdf"}  # header: BECE308L Optical Fiber Communications
# Rows corrected after orchestrator re-read (see <subject>/verification.md)
ROW_OVERRIDES = {
    ("CN/PYQ/FAT/BCSE308L - FAT - D2 - 2023 - Question Paper.pdf", "4"): {"marks": 10, "verification_note": "extractor wrote 41.0; paper is 10 x 10 and every other question sums to 10 (inferred)"},
    ("CN/PYQ/FAT/BCSE308L - FAT - D2 - 2023 - Question Paper.pdf", "5"): {"marks": 10, "verification_note": "extractor wrote 41.0; paper is 10 x 10 and every other question sums to 10 (inferred)"},

    ("2026-27 QPs/CD/PYQ/BCSE307L/CAT2/BCSE307L-CAT2-G2-2026-2027.pdf", "3a"): {"marks": "", "verification_note": "Q3 total 10 marks; sub-part split not printed (extractor had 10 on each part)"},
    ("2026-27 QPs/CD/PYQ/BCSE307L/CAT2/BCSE307L-CAT2-G2-2026-2027.pdf", "3b"): {"marks": "", "verification_note": "Q3 total 10 marks; sub-part split not printed (extractor had 10 on each part)"},
    ("2026-27 QPs/CD/PYQ/BCSE307L/CAT2/BCSE307L-CAT2-G2-2026-2027.pdf", "3c"): {"marks": "", "verification_note": "Q3 total 10 marks; sub-part split not printed (extractor had 10 on each part)"},
("AI/PYQ/FAT/BCSE306L - FAT - E2 - 2024 - Question Paper.pdf", "3"):
                 {"ocr_flag": 1, "verification_note": "figure edge 'A->G 2' doubtful; label 2 is likely C->A. Check image."}}
YEAR_OVERRIDES = {"AI/PYQ/CAT1/BCSE306L-CAT1-C2-2025-2026-Key.pdf": "2026-2027"}


def num(x):
    t = str(x).strip()
    if re.fullmatch(r"\d+(\.\d+)?(\s*\+\s*\d+(\.\d+)?)*", t):
        return sum(float(v) for v in t.split("+"))
    return None


def load(prefix):
    rows, papers, errs = [], [], []
    for f in sorted(glob.glob(f"{BASE}/shards/{prefix}-*.jsonl")):
        bid = os.path.basename(f).replace(".jsonl", "")
        is_paper = bid.endswith("_papers")
        for i, line in enumerate(open(f, encoding="utf-8")):
            line = line.strip()
            if not line:
                continue
            try:
                o = json.loads(line)
            except Exception as e:
                errs.append(f"{bid} line {i+1}: bad JSON ({e})")
                continue
            o["batch_id"] = bid.replace("_papers", "")
            if o.get("file_name") in EXCLUDE:
                continue
            o.update(ROW_OVERRIDES.get((o.get("file_name"), str(o.get("q_no"))), {}))
            if o.get("file_name") in YEAR_OVERRIDES:
                o["year"] = YEAR_OVERRIDES[o["file_name"]]
            (papers if is_paper else rows).append(o)
    return rows, papers, errs


def impute_marks(rows, papers):
    """Fill empty leaf marks from an 'N x M' paper header. Marked marks_imputed=1. Never overrides printed marks."""
    pm = {p.get("file_name"): p for p in papers}
    by = defaultdict(lambda: defaultdict(list))
    for r in rows:
        by[r.get("file_name")][(r.get("or_group") or "") + "|" + (str(r.get("q_no")).split(".")[0].lower() if r.get("or_group") else root_q(r.get("q_no")))].append(r)
    for f, groups in by.items():
        p = pm.get(f, {})
        m = re.search(r"(\d+)\s*[xX×*]\s*(\d+)", str(p.get("instructions", "")) + " " + str(p.get("notes", "")))
        if not m:
            continue
        per = float(m.group(2))
        for key, rs in groups.items():
            known = sum(num(r.get("marks")) or 0 for r in rs if num(r.get("marks")) is not None)
            unk = [r for r in rs if num(r.get("marks")) is None]
            if unk and known < per:
                for r in unk:
                    r["marks"] = round((per - known) / len(unk), 2)
                    r["marks_imputed"] = 1


def root_q(q):
    m = re.match(r"\s*Q?(\d+)", str(q))
    return m.group(1) if m else str(q)


def validate(rows, papers, inv_paths):
    issues = []
    seen = Counter((r.get("file_name"), str(r.get("q_no"))) for r in rows)
    for k, c in seen.items():
        if c > 1:
            issues.append(f"DUPLICATE (file,q_no) {k} x{c}")
    for r in rows:
        tag = f"{r.get('file_name')}:{r.get('q_no')}"
        if r.get("file_name") not in inv_paths:
            issues.append(f"UNKNOWN FILE {tag}")
        if r.get("type") not in TYPES and str(r.get("ocr_flag")) != "1":
            issues.append(f"BAD type '{r.get('type')}' {tag}")
        b = num(r.get("bloom_level"))
        if (b is None or b not in range(1, 7)) and str(r.get("ocr_flag")) != "1":
            issues.append(f"BAD bloom '{r.get('bloom_level')}' {tag}")
        if r.get("has_scenario_wrapper") not in ("y", "n") and str(r.get("ocr_flag")) != "1":
            issues.append(f"BAD scenario '{r.get('has_scenario_wrapper')}' {tag}")
        if str(r.get("ocr_flag")) not in ("0", "1"):
            issues.append(f"BAD ocr_flag '{r.get('ocr_flag')}' {tag}")
        mod = str(r.get("syllabus_module", ""))
        if not (re.match(r"^M[1-9] ", mod) or mod.startswith("derived:")) and str(r.get("ocr_flag")) != "1":
            issues.append(f"BAD module '{mod}' {tag}")
    # marks per paper
    pmeta = {p.get("file_name"): p for p in papers}
    by_file = defaultdict(list)
    for r in rows:
        by_file[r.get("file_name")].append(r)
    summary = []
    for f, rs in sorted(by_file.items()):
        groups = defaultdict(lambda: defaultdict(float))
        total = 0.0
        missing = 0
        for r in rs:
            m = num(r.get("marks"))
            if m is None:
                missing += 1
                continue
            g = r.get("or_group") or ""
            if g:
                groups[g][str(r.get("q_no")).split(".")[0].lower()] += m
            else:
                total += m
        for g, alts in groups.items():
            total += max(alts.values())
        rule = str(pmeta.get(f, {}).get("choice_rule", "")) + " " + str(pmeta.get(f, {}).get("instructions", ""))
        anyn = re.search(r"any\s+(TEN|EIGHT|FIVE|SIX|SEVEN|NINE|FOUR|\d+)", rule, re.I)
        if anyn and not groups:
            words = {"FOUR": 4, "FIVE": 5, "SIX": 6, "SEVEN": 7, "EIGHT": 8, "NINE": 9, "TEN": 10}
            k = int(words.get(anyn.group(1).upper(), anyn.group(1)))
            per_root = defaultdict(float)
            for r in rs:
                if num(r.get("marks")) is not None:
                    per_root[root_q(r.get("q_no"))] += num(r.get("marks"))
            total = sum(sorted(per_root.values(), reverse=True)[:k])
        stated = num(pmeta.get(f, {}).get("stated_max_marks"))
        n = len({root_q(r.get("q_no")) for r in rs})
        ok = stated is not None and abs(total - stated) < 0.01 and missing == 0
        flag = "" if ok else "FLAG"
        summary.append((f, n, total, stated, missing, flag))
    for f in pmeta:
        if f not in by_file:
            summary.append((f, 0, 0, num(pmeta[f].get("stated_max_marks")), 0, "FLAG no questions"))
    return issues, summary


def main():
    inv = list(csv.DictReader(open(f"{BASE}/inventory.csv", encoding="utf-8"), delimiter="|"))
    inv_paths = {x["path"] for x in inv}
    for prefix in sys.argv[1:]:
        subj = prefix.lower()
        out = f"{BASE}/{subj}"
        os.makedirs(out, exist_ok=True)
        rows, papers, errs = load(prefix)
        impute_marks(rows, papers)
        issues, summary = validate(rows, papers, inv_paths)
        with open(f"{out}/questions.csv", "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh, delimiter="|")
            w.writerow(COLS)
            for r in rows:
                w.writerow([re.sub(r"[|\r\n]+", " ", str(r.get(c, ""))) for c in COLS])
        with open(f"{out}/questions_text.jsonl", "w", encoding="utf-8") as fh:
            for r in rows:
                fh.write(json.dumps({"file_name": r.get("file_name"), "q_no": r.get("q_no"),
                                     "marks": r.get("marks"), "or_group": r.get("or_group"),
                                     "question_text": r.get("question_text"),
                                     "ocr_flag": r.get("ocr_flag"),
                                     "verification_note": r.get("verification_note", "")}, ensure_ascii=False) + "\n")
        json.dump(papers, open(f"{out}/papers.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
        with open(f"{out}/validation.md", "w", encoding="utf-8") as fh:
            fh.write(f"# Validation: {prefix}\n\nquestions: {len(rows)} | papers with rows: "
                     f"{len({r.get('file_name') for r in rows})} | paper records: {len(papers)} | "
                     f"ocr_flag=1: {sum(1 for r in rows if str(r.get('ocr_flag'))=='1')}\n\n")
            fh.write("## Marks check (sum counts one alternative per OR group)\n\n"
                     "| file | n_q | sum | stated | rows w/o marks | flag |\n|---|---|---|---|---|---|\n")
            for s in summary:
                fh.write("| " + " | ".join(str(x) for x in s) + " |\n")
            fh.write("\n## Schema/enum issues\n\n" + ("\n".join(f"- {i}" for i in errs + issues) or "none") + "\n")
        print(f"{prefix}: {len(rows)} q, {len(papers)} papers, {len(errs)+len(issues)} issues, "
              f"{sum(1 for s in summary if s[5])} papers flagged on marks")


if __name__ == "__main__":
    main()
