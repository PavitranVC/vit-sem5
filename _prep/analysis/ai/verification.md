# AI extraction: orchestrator verification (observed)

Re-read from page images by the orchestrator: 35 of 344 questions (10.2%), from 5 papers.
Papers: BCSE306L-CAT1-C2-2026-2027 (10 q), BCSE306L-FAT-B1-2026-2027 Q1-Q5a (5 q),
BITE308L-CAT1-D2-2025-2026 (7 q), BCSE306L CAT-2 E2 2024 (8 q), BCSE306L FAT E2 2024 Q1-Q5 (5 q).

| check | agree | rate |
|---|---|---|
| verbatim text incl. figure numbers | 34 / 35 | 97.1% |
| type | 30 / 35 | 85.7% |
| bloom_level | 30 / 35 | 85.7% |
| has_scenario_wrapper | 33 / 35 | 94.3% |
| all three tags pooled (tag_agreement_rate) | 93 / 105 | 88.6% |
| first 15 questions only (type / bloom / scenario) | 15/15, 13/15, 14/15 | |

## Disagreements (pattern)
- type: agents label narrative-wrapped computations as `scenario` although the spec says to tag the work
  (trace/numerical) and record narrative in has_scenario_wrapper. Cases: CAT-2 E2 2024 Q2 (resolution proof),
  Q4A (truth table); BITE308L CAT1 D2 Q3a (should be scenario, tagged theory), Q5 (theory tagged trace);
  FAT E2 2024 Q3 (explain DFS/BFS, tagged trace).
  -> Analysis uses has_scenario_wrapper (94% agreement) for "scenario %", not type=scenario.
- bloom: verbs "justify" (C2 CAT1 1a: agent 2, rule 5), "draw/compare" (FAT B1 26-27 Q2: agent 6, rule 4),
  "give PEAS" (BITE D2 2b: agent 2, rule 3), "formalize/find" (E2 CAT2 4A: agent 4, rule 3),
  "explain/discuss" (FAT E2 Q3: agent 4, rule 2). No systematic up/down bias (3 high, 2 low).
- scenario wrapper: C2 CAT1 5b has one context sentence (agent y, rule n); FAT E2 2024 Q3 technical setup (agent y, rule n).
- text: FAT E2 2024 Q3 figure lists edge "A->G 2"; image suggests the 2 belongs to C->A. Row set ocr_flag=1.

## Shard history
- AI-D1, D2, D3 were first extracted from the text layer only (the Read tool cannot rasterise PDFs here:
  no pdftoppm). 96 of 138 rows were flagged. Re-dispatched once to Sonnet with page images rendered by
  PyMuPDF; flags fell to 1 + 0 + 3. AI-D4 got a figure-fill pass (16 figure rows).
- AI-S1, AI-S2 (scanned, Sonnet, vision) accepted first time.

## Marks check
33 of 37 papers sum to their stated maximum. 4 flagged, all explained:
- BCSE306L-FAT-D1-2025-2026, FAT-D2-2025-2026: sub-part marks not printed (Q totals 10 each per instructions).
- BCSE306L-CAT1-D2-2025-2026-AK: marks column not printed for Q1, Q3-Q5.
- CSI3003-CAT2-E1-2026-2027-AK: answer key only, no question paper or max marks; Q1, Q2, Q5 stems absent.

## Corrections to file metadata
- `AI/PYQ/CAT1/BCSE306L-CAT1-C2-2025-2026-Key.pdf` is the **Revised Answer Key, CAT-I, Fall 2026-2027,
  Slot C2+TC2** (printed header). Its 10 answers match BCSE306L-CAT1-C2-2026-2027.pdf. Year overridden.
- 24 files end in `-AK.pdf`; 48 files (40 unique) are answer keys by name; 6 more files named as question
  papers contain worked answers (ak_contains_answers=y in papers.json).

## Unreadable / incomplete
No page was fully unreadable. 23 rows have ocr_flag=1 (partly illegible figure labels, missing stems in
key-only files). See questions.csv ocr_flag column.
