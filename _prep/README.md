# _prep: FAT preparation notes (Nov 2026)

This folder is an index and planning layer on top of the course material in the rest of the repo. It never moves or renames anything outside `_prep/`.

## Start here (humans and AI agents)
1. `plan/schedule.md`: the day-by-day plan, exam dates and rules for adjusting it
2. `context.md`: the student's self-ratings, panic ranking and internal marks (read before advising)
3. `study-guide/<SUBJ>-blocks.md`: block-by-block guide with exact files and page ranges (written per subject as each exam approaches)
4. `study-guide/<SUBJ>-slide-map.md`: page-by-page titles of the slide decks, generated from the PDFs/PPTX. Use it to find where a topic is instead of opening big files
5. `pyq-index/<SUBJ>.md`: every PYQ question tagged by module, as plain text (many PYQ PDFs are phone photos and cannot be searched). Raw index; analysis comes later

## Subject codes
CAD = Cloud Architecture Design (folder `AWS/`), OS, AI, DBS, CD, CN, ACC, plus the Indian Constitution (`Indian Constitution/`).

## Status (6 Nov 2026)
| Subject | PYQ index | Slide map | Block guide |
|---|---|---|---|
| CAD | FAT (5) + CAT-2 (most) done | done | done |
| CD | FAT (7) done | done | pending |
| OS | pending | done | done (7-14 Nov) |
| AI | pending | done | pending |
| DBS | pending | done | pending |
| CN | pending | done | pending |
| ACC | no PYQs (slides in `ACC/`) | n/a | pending |

Topic-frequency analysis was postponed until all subjects were indexed. CAD is the exception (done early on request): see `analysis/CAD.md`. Other subjects follow once indexed.

## Rules for any agent working here
- Additive only: create or edit files under `_prep/`. Do not delete, rename or move existing files.
- Commit and push only changes the student has approved. Keep commits to `_prep/` unless asked otherwise.
- Do not paste whole PDFs into notes. Index by question, tagged by module, in the format used in `pyq-index/CAD.md`.
- Check PDFs for extractable text first (`pdftotext`); scanned or photographed papers need to be read as images.
- Ignore labs, projects, case studies and build artifacts when planning study.
- The student's registration number appears in some file names. The repo is private; keep it that way.

`analysis/important-topics.html` is a single-page topic matrix for all subjects (open it in a browser). It shows which topics appeared in which FAT papers, a priority label and what to practise. Raw working notes: `analysis/raw-tallies.md`.
