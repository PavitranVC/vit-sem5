Here is your final, completely scrubbed master prompt. Every single requested update has been integrated, and absolutely no other words or formatting rules have been touched.

---

# MASTER PROMPT — Exam Rapid-Reference Textbook (Markdown + typeset PDF)

> **How to use:** fill in the CONFIG block, attach all class materials, past papers and answer keys **as the original PDFs/photos** (do not convert them to text first; scanned papers and hand-drawn keys only survive as images), then send everything below the line as one message. Best results: the most capable model available, maximum effort, in a session that can run code and create files.

---

## CONFIG (fill in before sending)

```text
SUBJECT TITLE (cover)       : COMPUTER NETWORKS
COURSE CODE (title page)    : BCSE308L    (NEVER MENTIONED ON THE BOOK)
EXAM BEING PREPARED FOR     : CAT-2            (used for analysis only; NEVER printed on cover/title page)
SYLLABUS IN SCOPE           :   Module 3: Data Link Layer
                3.3 Flow control mechanism: Stop and Wait Protocol
                3.4 Flow control mechanism: Sliding Window Protocol (Go-Back-N, Selective Repeat)
                3.5 Multiple access: Aloha, Slotted Aloha
                3.6 CSMA, CSMA/CD
                3.7 IEEE Standards (IEEE 802.3 Ethernet)
                3.8 IEEE 802.11 (WLAN), RFID, Bluetooth Standards

                Module 4: Network Layer
                4.1 Network Layer IPv4 Address Space
                4.2 Notations
                4.3 Classful Addressing
                4.4 Classless Addressing
                4.5 Network Address Translation (NAT)
                4.6 IPv6 Address Structure
                4.7 IPv4 header format
                4.8 IPv6 header format

                Module 5: Routing Protocols
                5.1 Routing Protocols Introduction
                5.2 Link State Routing Protocols
                5.3 Distance Vector Routing Protocols
TIME LEFT BEFORE EXAM       : 12 hours
INSTITUTION NAMES           : neutralise
   if neutralise → university = "the university"; campuses = "Main Campus" / "City Campus";
                   semesters = "Michaelmas Term <yr>" / "Hilary Term <yr>" / "Trinity Term <yr>";
                   slots = "Paper I … Paper VI"; question tag "PPQ" (past-paper question);
                   student / registration IDs = made-up format like SN23-1001;
                   building/room codes = generic names. Do not substitute any other real institution.
PERSON NAMES                : neutralise (default)
   if neutralise → replace EVERY real or recognisable person's name anywhere in the book
                   (students, faculty, authors, actors, celebrities, sample-data names such as
                   "Tom Hanks", "J.K. Rowling", "Smith", "Aarav") with made-up, culturally
                   ambiguous first/last names drawn evenly from Arabic, Hebrew and English name
                   pools (e.g. Samir Haddad, Noa Levin, Eliot Hart, Yara Nasser, Ari Kaplan,
                   Clara Ashby). Never use a famous person's name. Keep each replacement
                   consistent everywhere it appears, including inside queries, tables, figures
                   and solutions. Keep sort order and initials sensible where a question depends
                   on them (e.g. hashing on the first letter: replace with a name of the SAME
                   first letter so every computed answer stays valid). List the mapping once
                   in a one-line note at the start of each affected question.
                   Exception: citations of the source textbooks (e.g. "Forouzan, Data Communications and Networking") keep their real authors; never invent or
                   alter a citation. This rule overrides "word-for-word" for names only.
PEN NAMES                   : two made-up, neutral pen names, e.g. "Ari Haddad & Noa Ashby"
                              (or "auto": invent two names that mix Arabic, Hebrew and English
                              origins and are NOT a real author, academic or public figure)
OUTPUTS                     : Markdown e-book + typeset PDF (default: both)
ATTACHED FILES              : lecture notes, past papers, answer keys (all attached)

```

---

## ROLE

Act as a world-class academic textbook author and senior publishing editor (Forouzan / Kurose register). Produce a single, zero-scramble, open-book-ready textbook for the exam in CONFIG from the attached lecture notes, past papers and answer keys. Start with academic content. No conversational preambles, no AI filler.

## OPERATING RULES

* Work end-to-end without stopping to ask. Ask only if a decision is irreversible **and** genuinely ambiguous. State any assumption in one line where it applies.
* Keep a visible task list. Tick items off as they finish.
* **Syllabus boundary lock:** include only the units in SYLLABUS IN SCOPE. If past papers for this exam repeatedly test a prerequisite from an earlier unit (e.g., framing and CRC before flow control), add a short, clearly labelled **"Bridging Toolkit"** section at the start of the relevant chapter. Never add full chapters for out-of-scope units.
* Never print the exam name on the cover or the title page.
* **Attribution = pen names only:** never print a real name of whoever wrote, compiled or uses the book (no "prepared for …", no student or reader name). The only attribution is the two PEN NAMES, always as **"Compiled by <Pen 1 Name> & <Pen 2 Name>"**. Never present the pen names as authors of a published title, and never pair them with a real publisher.

---

## PHASE 1 — Read everything, lose nothing

1. Read **every page** of every file. Extract the text. Then **view the page image** for scanned, photographed or handwritten pages, and wherever extraction drops symbols (∞, network topology graphs, CIDR slashes (/24), subscripts, routing tables).
2. Build a **question inventory**: paper (term / slot / campus), Q number, sub-parts, marks, syllabus unit, answer key present or not, and whether the key has diagrams.
3. Transcribe every question **word-for-word**, including sub-parts, data sets, tables, network topologies and frame formats. Keep the original typos, and flag them in one line (e.g., "the stem says 15 keys; 12 are listed"). Apply only the PERSON NAMES and INSTITUTION NAMES replacements from CONFIG.

## PHASE 2 — Pattern analysis → Highest-Yield Matrix

1. Map each question to one syllabus unit or topic. Count hits per topic out of N papers.
2. **Probability** = hit frequency weighted by recency (latest academic year × 3, older × 2) and by campus / paper set (other campus × 1.5 recent, × 1 older). Adjust for the fixed question-slot structure. Round to the nearest 5 %. State in one line that the sample is small.
3. Identify:
* the **fixed exam skeleton** (which module sits in which question position, and what the question type almost always is);
* **rotating slots** and their frequencies;
* **exact repeats** across papers (same data set or schedule).


4. **Book plan (write it down before drafting):** the chapter list mapped to syllabus units, and every inventory question assigned to exactly one chapter with its final PPQ number. Draft strictly from this plan so numbering, cross-references and Appendix C stay consistent.

## PHASE 3 — Solve and verify (non-negotiable)

1. Recompute **every** numeric result, routing table, shortest path tree, subnet mask / CIDR allocation, ALOHA throughput calculation, and sliding window sequence **with code** (write small simulations). Do this for teacher keys and for your own solutions.
2. If an official key is wrong:
* keep the **[Teacher's Solution]** verbatim;
* add an **[Erratum]** callout with the corrected working;
* list every erratum in Appendix D.


3. If conventions differ (e.g., subnet zero inclusion, routing table tie-breakers, CSMA backoff limits), show both results and tell the student to write a one-line convention statement.
4. **Show the inequality before every rounded number:** for any ceiling, floor, logarithm, order or capacity bound, write the explicit comparison first (e.g. `2⁷ = 128 < 129 ≤ 256 = 2⁸ ⇒ ⌈log₂ 129⌉ = 8`), then the result.
5. **Substitute real numbers into every formula** used in a solution (block sizes, record counts, buffers, rates, etc.), never only the symbolic formula.
6. For questions with no key: write an **[AI-Generated Solution] (source: , Q)**, step by step, derived from the lecture notes.

## PHASE 4 — Write the Markdown e-book (exact structure)

### 4.1 Front matter (in this order)

1. YAML metadata: title, subtitle, compiled_by (the two pen names), subject, edition, language.
2. **Half-title page:** the book title only.
3. **Title page:** title, subtitle, tagline, "Compiled by " with the "Independent study notes" line, then a metadata table: Title · Subtitle · Subject · Coverage · Edition · Primary references (textbooks the notes follow) · Question corpus (N papers, M keys).
4. **Contents** (numbered parts, chapters, sections), then **List of Figures** and **List of Tables**.
5. **Question Finder:** a lookup table "If the question asks [e.g., 'Divide the CIDR block' or 'Find the shortest path'] → go to §x.y, p. n" covering every recurring question type (the fastest open-book entry point).
6. **Preface** (≤ ½ page): who the book is for, how it is organised, how the chapters, past-paper sections and appendices fit together.
7. **Acknowledgements** (≤ 1 page), signed by the two pen names:
* thank 2–3 **fictional** people only (e.g. a mentor, a reviewer, classmates "who tested early drafts"), with invented names that follow the PERSON NAMES style and match no real person;
* add 3–4 generic sentences: thanks to students past and present, to "the authors of the standard texts on which these notes draw", and to readers who report errors;
* never thank or name a real person, publisher or institution.


8. **Conventions & Notation:** the solution-tag legend ([Teacher's Solution] / [AI-Generated Solution] / [Erratum]), the callout legend (Definition, Formula/Algorithm, Exam Trap, High-Yield, Erratum), the symbol table, and the lookup order (Question Finder → Contents → chapter → its past-paper section).
9. **Highest-Yield Matrix** (Excel-style table): `Rank | Module | Unit | Topic | Hits (/N) | Marks at stake | Probability | Priority (★)`, plus a **Question-position table** (`Question | Module | Marks | What it almost always is`) and an **Exact repeats** callout.

Do **not** include a "How to Use This Book" section; its content lives in the Preface and Conventions page.

### 4.2 Body

* **One Part per module.** The Part opens with a blockquote: module weight, question position, typical pattern.
* **Chapters map 1:1 to syllabus units.** Merge tiny units; name the units under the chapter title (`**Syllabus unit x.y** · Textbook ch. refs`).
* **Chapter layout, always in this order:**
0. **"In this chapter" box** (≤ 4 lines): 3–4 learning outcomes plus "Exam weight: X M · Appears in n/N papers". Then a **Key Terms** strip of 5–8 bold terms (each also in the Glossary).
1. Definitions / theorems in `> [!NOTE]` callouts.
2. Formulas and algorithms in `> [!TIP]` callouts, with code fences (step blocks or pseudocode).
3. Comparison tables and worked patterns (e.g., CIDR block allocation tables, Dijkstra's permanent/tentative lists, and Distance Vector update tables).
4. Figures in Mermaid, each preceded by `**Figure c.n: <caption>**`.
5. `## c.k Exam Traps: Chapter c`: each trap in a `> [!WARNING]` callout starting `**⚠ EXAM TRAP c.n: <title>.**`.
6. `## c.k Chapter at a Glance`: a ≤ ½-page revision summary (the essential formulas, rules and steps, nothing new), ending with a **Self-check** list: "Can you …? → PPQ c.n".
7. `## c.k Past-Paper Questions: Chapter c`: questions placed at the end of the chapter whose topic they test.


* **Cross-references:** wherever a topic depends on another, add "→ see §x.y" (in the PDF, also the page number).
* **Part openers** include one **decision flowchart** (Mermaid) for the module's most common choice (e.g. "which ARQ protocol?", "which routing algorithm?").
* **Past-paper question block format:**
```text
### PPQ c.n · <Term Year> · <Paper> · Q<no> (<marks>)
> <question verbatim: sub-parts, tables, schemas, data; hard line breaks with "\">
**[Teacher's Solution]** <verbatim transcription; hand-drawn trees/graphs re-drawn as Mermaid>
> [!CAUTION] **[Erratum]: …**    (only if needed)
**[AI-Generated Solution] (source: <paper>, Q<n>)** <numbered steps, tables, figures>

```


* High-yield repeats go in `> [!IMPORTANT]` callouts.

### 4.3 Back matter

* **Appendix A:** Master Formula Sheet (all formulas, grouped, in `[!TIP]` code blocks).
* **Appendix B:** Answer-Writing Templates, one per recurring question type (numbered steps and where the marks sit), plus a Last-Hour Checklist.
* **Appendix C:** Past-paper index by paper (rows = papers, columns = Q1…Q5, cells = PPQ numbers).
* **Appendix D:** Errata in official keys (`# | Paper · Q | Key says | Correct | Book ref`).
* **Glossary:** every Key Term with a one-line definition and its page/section.
* **Index** (PDF): as specified in Phase 5.
* **Quick-Reference Card** (last 2 pages): a dense, printable sheet of the core formulas plus the 10 highest-yield answer templates.

### 4.4 Style rules

* No paragraph longer than two lines. Use bullets, numbered steps and tables. Keep sentences short and direct.
* Every definition, formula and algorithm goes in a callout. Every trap is bold-tagged.
* Put a `---` separator between major sections.
* **Framework lock:** the content and in-chapter style (callouts, traps, past-paper blocks, figures) stay exactly as specified; the front matter, chapter frame (opening box, Key Terms, Chapter at a Glance) and back matter are additions around that content, never a rewrite of it.
* **Length budget:** Preface ≤ ½ page, Acknowledgements ≤ 1 page, "In this chapter" ≤ 4 lines, Chapter at a Glance ≤ ½ page; theory pages per chapter ≈ 2–6 before its past-paper section.
* **Number everything:** every figure and table is numbered (Figure c.n / Table c.n) and appears in the List of Figures / List of Tables.
* Markdown hygiene:
* balanced code fences;
* a blank line before tables;
* in verbatim question blockquotes, end each line with `\` for a hard break, **except** the line before a list item;
* a blank `>` line before and after lists inside blockquotes.



### 4.5 Mermaid rules

* Quote every label: `R1["Router 1 (192.168.1.1)"]`. Use `≠`, never `<>`. Use `<br/>` for line breaks.
* **Network Topologies & Routing:** Use `graph TD` or `LR`, representing routers as nodes and links with cost labels. For Dijkstra's shortest path trees, use thick or distinct lines to highlight the final computed paths.
* **Protocol Timelines & ARQ:** Use `sequenceDiagram` for Stop-and-Wait, Go-Back-N, Selective Repeat, and Multiple Access collisions. Show frame transmissions as arrows, and use `Note` blocks to indicate Timeouts, Window sliding, and lost frames.
* **Algorithmic Flowcharts:** Use `flowchart TD` for MAC protocols like CSMA/CD, CSMA/CA, and ALOHA (e.g., showing condition diamonds for "Collision detected?" or "Channel idle?").
* **Subnet/Address mapping diagrams:** Use `classDef` colored nodes for CIDR block divisions.
* **Packet/Frame Formats:** Do **not** use Mermaid for packet headers (like IPv4 headers, MAC frames, or HDLC frames). Instead, use structured **Markdown Tables** specifying field names and their bit/byte lengths (e.g., `| VER (4 bits) | HLEN (4 bits) | ... |`).
* Validate by rendering **every** block with mermaid-cli before delivery. Fix any that fail or look misaligned.

## PHASE 5 — Typeset the PDF (professional book standard)

1. **Figures:** render the Mermaid blocks to PNG with mermaid-cli (Chromium).
* Compact config: `nodeSpacing 22, rankSpacing 26, padding 6, fontSize 15px`. Use `rankSpacing 60` for left-to-right network topologies and timeline diagrams.
* Display at about 0.82× natural size, capped at 640 px wide and 360 px tall.
* Put consecutive figures side by side (flex row) when they fit.


2. **Page setup:** HTML → headless Chromium, A4, margins 19 / 17 / 17 / 17 mm.
* Fonts embedded from npm fontsource: **Source Serif 4** body 9.7 pt, **Inter** headings, **Playfair Display** titles, DejaVu Sans Mono for code.
* Callouts colour-coded (note blue, tip green, warning amber, important purple, caution red) **and** labelled with an icon or word, so they still read correctly when printed in black and white.


3. **Page order and breaks** (each item starts on a new page):
1. Cover (full-bleed, zero margins).
2. Half-title page (title only, centred, generous white space).
3. Title page (title, subtitle, gold rule, tagline, "Compiled by " with the "Independent study notes" line, metadata table at the bottom; no real names).
4. **Contents** (dotted leaders, page numbers, Parts → Chapters → Sections), **List of Figures**, **List of Tables**, **List of Solved Past-Paper Questions** (all with page numbers).
5. **Question Finder**, **Preface**, **Acknowledgements**, **Conventions & Notation**, **Highest-Yield Matrix**.
6. **Part opener pages:** full page, gold left bar, "Part I · Module 3", big title, module-weight line, decision flowchart, chapter list with page numbers.
7. **Chapters:** each starts on a new page with a small gold "CHAPTER n" label, a large display title, the syllabus line, then the "In this chapter" box and Key Terms.
8. **Each chapter's Past-Paper Questions section starts on a new page** under a dark navy banner, so theory and numericals stay separated. "Chapter at a Glance" sits immediately before it.
9. Appendices, Glossary, Index (two columns, about 100 key terms, alphabetical letter groups; bold page = defining section), Quick-Reference Card. Each starts on a new page.
10. **Edge tabs:** a coloured tab on the outer page edge, one colour and vertical position per Part (and one for back matter), so a printed copy can be flipped open by colour.


4. **Two-pass pagination:** render once with placeholder numbers. Read the PDF named destinations to get each heading's page. Fill the Contents, the question list, the Part opener lists and the Index. Render again and confirm nothing moved.
5. **Copy-fitting:** if any section's last page is less than 30 % full, tighten **only that section** (levels 1–3: slightly smaller font and spacing, figure zoom 0.9 / 0.8 / 0.72) and re-render. Repeat until no near-empty pages remain. Never shrink the whole book.
6. **Stamping:**
* Running header: chapter number and title (left) and current **section number and title** (right, e.g. "§6.4 Insertion Algorithm"), with a hairline rule.
* Centred footer page number: roman numerals for front matter, arabic from Part I.
* No header or footer on the cover, the title page or Part openers.
* Set PDF page labels.
* Build a bookmark tree: Part → Chapter → Section → each PPQ.
* Compress with qpdf.


7. **Cover:**
* Background: navy gradient (#081a33 → #113a6c), with a left spine band (13 mm, #061427) edged by a gold (#d9a441) rule and vertical spaced-caps text "RAPID REFERENCE SERIES · ".
* Top line: "Rapid Reference Series" left, "First Edition · " right.
* Title block: italic gold kicker "A Rapid-Reference Examination Text"; the title in large Playfair (about 60 pt) with the **last word in gold italic**; a short gold rule; a one-line subtitle of the module themes.
* Watermark: faint, large subject symbols (≈ 4 % opacity).
* Bottom band (cream #f4f1ea): "Subject: <course code · name>" and a circular monogram "RR" with "Rapid Reference Series".
* Bottom band also carries "Compiled by  · Independent study notes" in small caps.
* **Do not put on the cover:** the exam name, statistics, diagrams, any real person's name, or any real publisher's name or logo.
* PDF document properties: Title, Subject, and Author = "Compiled by ".



## PHASE 6 — QA before delivery

* [ ] Inventory check: every question of every paper appears exactly once as a PPQ (count = inventory).
* [ ] Every computed answer is verified by code; every erratum is listed in Appendix D.
* [ ] All Mermaid blocks render; no misaligned or overlapping figures (inspect the rendered pages).
* [ ] Contents, Lists of Figures/Tables, Question Finder, question-list and cross-reference page numbers match the actual pages (spot-check at least 3 of each).
* [ ] Every chapter has its "In this chapter" box, Key Terms, Chapter at a Glance and Self-check; every Key Term is in the Glossary.
* [ ] Acknowledgements name only fictional people; no "How to Use This Book" section exists.
* [ ] No near-empty pages. Each chapter's questions start on a new page.
* [ ] The only attribution anywhere is "Compiled by " with the study-notes line; no real person's name and no "prepared for" (search both files and the PDF properties).
* [ ] If PERSON NAMES = neutralise: no real or famous person's name remains; all answers that depend on name letters still verify.
* [ ] If INSTITUTION NAMES = neutralise: search both files for the old university, campus, slot and semester names and ID patterns. Result = 0.
* [ ] Code fences balanced; no stray `\` or literal markdown in the PDF.

## DELIVERABLES

1. `<Subject>_Rapid_Reference.md`: the single-file Markdown e-book.
2. `<Subject>_Rapid_Reference.pdf`: the typeset book.
3. A short reply covering:
* coverage (N papers, M questions, K figures);
* the top-5 highest-yield topics with their probabilities;
* errata found in the keys;
* any question that could not be read reliably (e.g. a blurred photo), so it can be checked by hand;
* assumptions made;
* a study order that fits TIME LEFT BEFORE EXAM.