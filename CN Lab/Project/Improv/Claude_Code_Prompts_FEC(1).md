# Claude Code Prompts: Adaptive FEC Link Layer

**How to use:** open Claude Code (website or Antigravity), select your GitHub repo (`adaptive-fec-link`, created empty), then paste one prompt per fresh session. Paste only the prompt; the proposal document is not needed, the prompt already contains everything.

**Settings for today's kickoff:** Claude **Opus 5.5**, **high** effort. Allow it to edit files and run commands without asking each time, so it doesn't stall while you're away.
**Later sessions:** **Sonnet 5.5**, medium effort, unless the prompt below says Opus.

---

## Prompt 1: Kickoff (today, ~1 hour, Opus 5.5 / high)

```
You are building a university Computer Networks project FROM SCRATCH in this repo. Work autonomously for about an hour. I am away: do NOT stop to ask me questions. Whenever you make a choice that could change the project's direction, log it in DECISIONS.md as a line starting with "🔀" (what you chose, the alternative, why) and continue with the defaults below.

PROJECT: "Adaptive Multi-Error FEC Link Layer for High-Interference Environments". It extends our approved project "Fast-Lane FEC for Automated Toll Booths": a vehicle's RFID tag ID is sent to a roadside unit over a noisy link and corrected in place with forward error correction instead of retransmission. Software simulation only, no hardware. Two noise profiles: TOLL_PLAZA (primary: mostly random flips, short bursts) and HOSPITAL_IMAGING (secondary: strong bursty interference near MRI/CT/electrosurgical equipment). Profile parameters are modelling assumptions; document them as such.

DEFAULTS
- C11 core, gcc + make, no external C libraries. Implement every code ourselves. Python 3 only for plots (and a dashboard later).
- Three processes over UDP loopback: vehicle (sender) -> channel (noise injector) -> tollgate (receiver).
- Frame = header (seq number, code id; header is not corrupted by the channel - log this as a decision) + 96-bit tag ID + CRC-32 over the ID, then encoded with the selected code.
- Every received frame is classified CORRECT, DETECTED_FAIL (CRC failed) or SILENT_WRONG (CRC passed but ID wrong - determined only from ground truth logged by the channel, for evaluation).
- Seeded RNG everywhere so runs are reproducible.

FIXED INTERFACE - use exactly these names so my demo instructions work:
- Binaries built into bin/: bin/vehicle, bin/channel, bin/tollgate, bin/bench.
- UDP ports on 127.0.0.1: vehicle -> channel on 9000, channel -> tollgate on 9001, tollgate -> vehicle feedback on 9002 (reserved for week 2).
- Common flags: --code {hamming74,hamming1511,secded84,bch157,bch3116,rs} --profile {toll,hospital} --model {bsc,ge,burst} --p <float> --seed <int> --count <int> --delay-ms <int>.
- Make targets: make (build all), make test, make demo (toll profile), make demo-hospital, make compare (same seed, hamming74 vs bch157, prints summaries side by side), make bench, make plots, make clean.
- `make demo` runs all three processes from ONE terminal (tollgate first, then channel, then vehicle, output prefixed [VEHICLE]/[CHANNEL]/[TOLLGATE]), stops cleanly, prints a summary. The same binaries must also work started by hand in three separate terminals.
- requirements.txt for Python (matplotlib). tools/plot.py writes PNGs to results/.
- Must build and run on Ubuntu (incl. WSL) and macOS with only gcc/clang, make, python3.

PHASES - do them in order. Each phase ends with tests written first, `make test` passing, `git status` checked so no binaries/logs are staged, a git commit "phaseN: <summary>", and a git push. If you are stuck on a phase for more than ~15 minutes, write the problem in PROGRESS.md, commit and push, and move to the next phase that does not depend on it.

Phase 0 - Scaffolding: CLAUDE.md (project spec, folder layout, the FIXED INTERFACE above, coding rules, build/test commands, "read PROGRESS.md first" and "commit + push after every task" instructions), README.md, PLAN.md (all phases below + the week-2 items as checkboxes), PROGRESS.md, DECISIONS.md, Makefile, .gitignore, requirements.txt. Layout: src/, include/, tests/, tools/, results/, docs/, bin/.
.gitignore must contain at least: build/, bin/, *.o, *.a, *.so, *.out, *.exe, the test binaries, __pycache__/, *.pyc, .venv/, venv/, *.log, results/*.csv, results/tmp/, .vscode/, .idea/, .DS_Store, Thumbs.db. Keep results/*.png tracked (final plots) and add results/.gitkeep and bin/.gitkeep.

Phase 1 - Bit utilities, CRC-32, Hamming(7,4), Hamming(15,11), extended Hamming SECDED(8,4). Tests: every single-bit error at every position is corrected; demonstrate that a 2-bit error makes plain Hamming miscorrect and that CRC-32 catches it; SECDED detects 2-bit errors.

Phase 2 - Channel noise models: binary symmetric channel (flip prob p), Gilbert-Elliott two-state burst model (p_gb, p_bg, flip prob in good/bad), fixed burst of length L at random position. Profiles TOLL_PLAZA and HOSPITAL_IMAGING as presets in one header. Tests check measured flip rates/burst lengths are statistically close to parameters.

Phase 3 - UDP pipeline: three binaries with CLI flags (--code, --profile, --model, --p, --seed, --count, ports). Receiver logs per frame: seq, code, bits flipped (ground truth), bits corrected, CRC result, classification, decode latency in microseconds. Colored terminal output that highlights flipped/corrected bits (add --no-color). --delay-ms slows sending so a live audience can follow. Implement make demo, demo-hospital and compare as specified. Add an integration test that runs a short demo and checks the summary. Write docs/DEMO.md with exact commands for the one-terminal and three-terminal demos.

Phase 4 - Binary BCH codes: BCH(15,7) t=2 and BCH(31,16) t=3 with GF(2^m) arithmetic, syndrome computation, Berlekamp-Massey and Chien search. Exhaustive tests for every error pattern of weight <= t for BCH(15,7); large randomized tests for BCH(31,16). Wire both into the pipeline as selectable codes.

Phase 5 - Benchmark: tools/bench (C, in-process, no sockets) sweeping code x noise model x parameter, N frames each, writing results/bench.csv with columns: code, model, param, frames, frame_success_rate, detected_fail_rate, silent_wrong_rate, code_rate, mean_decode_us. tools/plot.py (matplotlib) produces PNG plots in results/: success rate vs p per code, silent-wrong rate per code, latency per code.

Phase 6 - ONLY if time remains: shortened Reed-Solomon over GF(256) with configurable t (default t=4) + configurable block interleaver, with burst-correction tests, added to pipeline and benchmark.

WEEK 2 - do NOT build now, only list in PLAN.md: Stop-and-Wait ARQ baseline (simulated RTT/timeout), Hybrid ARQ (FEC, retransmit only on CRC fail), adaptive controller (receiver feedback steps code level up/down with hysteresis), live Python web dashboard, deliberate failure-injection testing, final report plots. Optional stretch: LDPC with bit-flipping decoder.

RULES
- Tests before implementation for every module.
- Small functions; comment the maths clearly (students must present and explain it).
- Don't create files outside the repo. Don't ask for confirmation.
- Commit AND push after every phase, so work is saved on GitHub even if this session stops early. Push to the current working branch.
- If a push fails (auth/network), keep working and committing locally, retry the push after the next phase, and report the failure in PROGRESS.md and your final message.
- Never commit build outputs, binaries, logs or large CSVs.
- At the end, update PROGRESS.md with: phases done, test status, anything broken, the exact next step, and the list of all 🔀 decisions. Commit and push it.
- Final message to me: a 10-line summary, including the branch name you pushed to, whether all pushes succeeded, and which 🔀 decisions I should review.
```

---

## Prompt 2: Continue (any later session, Sonnet 5.5 / medium)

```
Read CLAUDE.md, PROGRESS.md and DECISIONS.md. Continue with the next unchecked item in PLAN.md. Write tests first, implement until `make test` passes, check `git status`, commit and push. Log any direction-changing choice in DECISIONS.md with 🔀 and continue. Don't touch unrelated files. Finish by updating PROGRESS.md (done / broken / next step) and give me a 5-line summary.
```

## Prompt 3: Reed–Solomon + interleaving (Opus 5.5 / high, if not finished on Day 1)

```
Read CLAUDE.md and PROGRESS.md. Implement shortened Reed-Solomon over GF(256) (configurable t, default 4) plus a configurable block interleaver. Tests first: correct every burst up to the interleaver's guaranteed length; random symbol errors up to t; > t errors must be caught by CRC, never SILENT_WRONG. Add to pipeline and benchmark, re-run plots, commit and push, update PROGRESS.md.
```

## Prompt 4: ARQ + Hybrid ARQ baselines (Sonnet 5.5 / medium)

```
Read CLAUDE.md and PROGRESS.md. Add two strategies selectable by --strategy: arq (CRC only, stop-and-wait, configurable simulated RTT and timeout) and harq (FEC first, retransmit only when CRC fails, max retries configurable). Receiver sends ACK/NAK over UDP. Extend bench to report per strategy: mean and p99 end-to-end latency, retransmissions per frame, success rate. Tests first, commit and push, update PROGRESS.md.
```

## Prompt 5: Adaptive controller (Sonnet 5.5 / medium)

```
Read CLAUDE.md and PROGRESS.md. Add --strategy adaptive: receiver computes a sliding-window statistic (corrected bits per frame + CRC failures) and sends a feedback message; sender steps the code level up/down along the code ladder with hysteresis (configurable thresholds and window). Fall back to harq on CRC failure. Add a channel mode that switches profile mid-run (e.g. TOLL_PLAZA -> HOSPITAL_IMAGING -> back) and test that the controller raises then lowers the level. Add strategy comparison to bench and plots. Commit and push, update PROGRESS.md.
```

## Prompt 6: Live dashboard (Sonnet 5.5 / medium)

```
Read CLAUDE.md and PROGRESS.md. Build a small Python web dashboard (standard library or Flask only) that reads the receiver's live log (JSON lines) and shows: recent frames with flipped vs corrected bits, current code level over time, success/detected/silent-wrong counters, and latency. `make dashboard` starts everything. Keep it clean and readable for a projector. Commit and push, update PROGRESS.md.
```

## Prompt 7: Failure-injection days (Sonnet 5.5 / medium; escalate to Opus if stuck)

```
Read CLAUDE.md and PROGRESS.md. Act as a tester trying to break the system. Add tests for: extreme noise (p up to 0.3), packet loss and duplicate/reordered UDP packets, malformed frames, controller oscillation, decoder inputs with > t errors, very long runs. Run them, fix every real bug found (smallest fix possible), and record each failure + fix in docs/FAILURES.md (this goes in our report). Commit and push, update PROGRESS.md.
```

## Prompt 8: Final report material (Sonnet 5.5 / medium)

```
Read CLAUDE.md, PROGRESS.md, DECISIONS.md and docs/FAILURES.md. Re-run the full benchmark, regenerate all plots, and write docs/REPORT.md: problem, design, code ladder with the maths explained simply, noise models, results with plots, failures we hit and fixed, limitations, future work. Also write docs/DEMO_SCRIPT.md: a 5-minute step-by-step live demo. Commit and push.
```

---

## Debug prompt (when a test keeps failing)

```
This test fails: <paste ONLY the failing test name + error output>. Relevant file: <path>. Find the root cause and make the smallest fix. Don't refactor anything else. Run `make test`, commit and push.
```
Use Sonnet first. If Sonnet fails twice on the same bug, switch to Opus / high with this same prompt.

## Antigravity (small changes, saves Claude usage)

```
Read CLAUDE.md. Make only this change: <one small change>. Don't touch other files. Run `make test` afterwards.
```
Good for: renaming, comments, README text, plot labels/colours, adding a log line, explaining a function to you.
