# Extraction spec (given to every extractor subagent)

## Task
Extract every question from the files listed in your batch. For each file:
1. Run `pdftotext -layout "<path>" -` (Bash, read-only) to get the text layer.
2. ALSO Read every pre-rendered page image (.jpg) listed for the file in your manifest, to see
   figures, tables, trees, graphs and any page with no text layer. The Read tool CANNOT render PDFs
   on this machine (no pdftoppm), so never Read the .pdf itself. Scanned/photographed pages: read
   the images visually.
3. Copy question text VERBATIM. Do not summarize, fix, or complete it. If a word/number is unreadable,
   write `[illegible]` in place. Describe figures inside the text as `[FIGURE: <faithful description,
   all numbers/labels/edge weights you can read>]`. Never invent numbers.
4. If you are unsure about a question's text or fields, set `ocr_flag`=1 and leave unsure fields empty.

## Output (write ONLY these files, nothing else)
- `_prep/analysis/shards/<batch_id>.jsonl`  one JSON object per question (leaf level, see q_no)
- `_prep/analysis/shards/<batch_id>.csv`    same rows, pipe `|` delimited, header row, NO question_text
  column, and no `|` or newlines inside fields
- `_prep/analysis/shards/<batch_id>_papers.jsonl`  one JSON object per file (paper-level facts)

### Question object keys (all keys required; use "" when empty)
file_name (exact repo-relative path given to you), subject, course_code, year, exam, slot,
q_no, or_group, marks, syllabus_module, topic, type, bloom_level, has_scenario_wrapper, has_figure,
one_line_core_task, question_text, ocr_flag, page, is_answer_key,
step_marks, required_keywords, penalties, key_final_answer

### CSV column order
subject|course_code|year|exam|slot|q_no|marks|syllabus_module|type|bloom_level|file_name|has_scenario_wrapper|one_line_core_task|ocr_flag|topic|or_group|has_figure|page|is_answer_key|step_marks|required_keywords|penalties|key_final_answer

### Paper object keys
file_name, stated_max_marks (as printed, number or ""), duration, instructions (verbatim, e.g.
"Answer ALL questions"), n_questions_printed, choice_rule (e.g. "Q9 or Q10", "" if none),
ak_contains_answers (y/n: does the file actually contain worked answers/marking scheme?),
unreadable_pages (list of page numbers you could not read), notes

## Field definitions
- q_no: the paper's own numbering. Use sub-parts as separate rows ONLY when they carry separate marks
  ("3a","3b"). If a question has one mark total, one row ("3").
- or_group: if the paper offers an alternative ("OR", "Answer any"), give both alternatives the same
  group label, e.g. "G9" for "9 OR 10". Else "".
- marks: number printed for that row (leaf). "" if not printed.
- syllabus_module: if your prompt gives a module list for your subject, use it exactly (and its topic
  examples); otherwise (AI) use one of the BCSE306L module names below, exactly:
  M1 Introduction & Intelligent Agents | M2 Search (uninformed/informed) | M3 Local & Adversarial Search |
  M4 Logic Reasoning | M5 Uncertain Knowledge & Reasoning | M6 Planning | M7 Communication, Perceiving & Acting
  If the topic does not fit any (e.g. ML/neural nets in a sister course), write `derived:<short name>`.
- topic: short canonical topic, 2-5 words, e.g. "A* search", "BFS/DFS trace", "Minimax + alpha-beta",
  "Hill climbing", "Simulated annealing", "Genetic algorithm", "CSP / map colouring",
  "PEAS / agent types", "Environment properties", "Propositional resolution", "FOL conversion (CNF)",
  "Forward/backward chaining", "Bayes theorem", "Bayesian network inference", "STRIPS / planning",
  "NLP / parsing". Reuse these spellings when they fit.
- type: exactly one of `numerical` | `trace` | `theory` | `scenario`
  numerical = needs computing a number or table; trace = step-by-step execution of an algorithm;
  theory = explain/define/compare; scenario = applied situation where the task is not stated until
  after narrative. If both scenario and trace/numerical apply, pick the one describing the WORK asked
  (trace/numerical) and record the narrative via has_scenario_wrapper.
- bloom_level: integer 1-6 from the main action verb: define/list=1, explain/describe=2,
  apply/compute/solve/trace=3, analyze/compare/differentiate=4, evaluate/justify=5, design/formulate/create=6.
  If the paper prints its own BL column, still use the verb rule here, and append
  " [printed BL=<n>]" to one_line_core_task.
- has_scenario_wrapper: `y` if there are 2+ sentences of narrative context before the actual task,
  otherwise `n`.
- has_figure: `y` if the question depends on a figure/table/tree/graph, else `n`.
- one_line_core_task: your own <=20-word statement of what must be produced, fluff removed
  (this is the ONLY non-verbatim field).
- ocr_flag: 1 if any part was illegible/uncertain, else 0.
- page: page number in the PDF where the question starts.
- is_answer_key: 1 if this file is an answer key, else 0 (given in your manifest).
- For answer keys only (else ""):
  step_marks = the marking split as stated in the key, e.g. "2 heuristic table; 4 expansion order; 2 path+cost".
               If the key gives no split, write "not stated".
  required_keywords = semicolon list of terms/intermediate states the key explicitly shows as needed.
  penalties = any stated deduction rule; "not stated" if none.
  key_final_answer = the key's final answer in <=25 words (path, value, result).

## Reply
Reply with ONE line only: `<batch_id> done, <n> questions, <m> flagged`. Do not paste extracted text.
Do not create, edit, move or delete any other file.
