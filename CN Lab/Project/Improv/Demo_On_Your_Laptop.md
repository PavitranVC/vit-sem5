# Running the Demo on Your Laptop

These commands match the names fixed in the kickoff prompt (`bin/vehicle`, `bin/channel`, `bin/tollgate`, ports 9000/9001, `make demo` etc.). If anything differs, the repo's `docs/DEMO.md` (written by Claude) is the source of truth.

**Before you start:** read the last section of `PROGRESS.md` on GitHub. It says which phases finished. Phases 1–3 are enough for a live demo; Phase 4+ adds BCH (multi-error) and Phase 5 adds plots.

---

## 1. One-time setup

**Windows (use WSL, takes ~10 min the first time)**
1. Open PowerShell **as Administrator** and run: `wsl --install` then restart the laptop.
2. Open **Ubuntu** from the Start menu, create a username/password.
3. In Ubuntu, run:
   ```bash
   sudo apt update
   sudo apt install -y build-essential git python3 python3-pip python3-venv
   ```

**Ubuntu / Linux:** run the same `sudo apt ...` commands as above.

**macOS:** in Terminal run `xcode-select --install` (gives gcc/clang, make, git). Install Python 3 from python.org if `python3 --version` fails.

---

## 2. Get the code

Claude Code on the website usually pushes to a branch named like `claude/...`, not `main`.

**Easiest:** on GitHub, open your repo → you'll see a banner "*claude/... had recent pushes*" → **Compare & pull request** → **Merge**. Then:
```bash
git clone https://github.com/<your-username>/adaptive-fec-link.git
cd adaptive-fec-link
```

**Without merging:**
```bash
git clone https://github.com/<your-username>/adaptive-fec-link.git
cd adaptive-fec-link
git branch -r                 # shows e.g. origin/claude/xyz
git checkout claude/xyz       # use the name shown
```

Later updates: `git pull`.

---

## 3. Build and test

```bash
make            # builds everything into bin/
make test       # all tests should say PASS
```
If `make test` passes, you're ready to demo.

---

## 4. Demo A: one terminal (quickest)

```bash
make demo             # toll plaza profile
make demo-hospital    # hospital imaging profile (bursty noise)
make compare          # same noise, Hamming vs BCH side by side
```

**What to point out:**
- Flipped bits are highlighted; corrected bits are shown separately.
- Each frame says **CORRECT**, **DETECTED_FAIL** or **SILENT_WRONG**.
- In `make compare`, Hamming produces SILENT_WRONG or DETECTED_FAIL frames under multi-bit noise; BCH corrects them. CRC catches every Hamming miscorrection, so the ID is never accepted wrong.
- Decode latency is in **microseconds**, far below any retransmission delay.

---

## 5. Demo B: three terminals (best for the presentation)

Open three terminal windows in the project folder (Windows Terminal: open three Ubuntu tabs, `cd adaptive-fec-link` in each). Start them **in this order**:

**Terminal 1: Toll Gate (receiver)**
```bash
./bin/tollgate --code bch157
```

**Terminal 2: Noisy Channel**
```bash
./bin/channel --profile toll --model ge --seed 42
```

**Terminal 3: Vehicle (sender)**
```bash
./bin/vehicle --code bch157 --count 20 --delay-ms 500
```

Then repeat with `--code hamming74` in terminals 1 and 3 to show Hamming failing on the same noise. Try `--profile hospital` in terminal 2 for heavy bursty interference.

`--delay-ms 500` sends two frames a second so the audience can follow. Use `--delay-ms 0` to show raw speed.

Stop any process with **Ctrl + C**.

---

## 6. Benchmark plots (if Phase 5 is done)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
make bench
make plots
```
Plots are saved in `results/` as PNG files.
- Windows/WSL: `explorer.exe results` opens the folder in Windows.
- macOS: `open results`
- Linux: `xdg-open results`

---

## 7. 60-second talking script

1. "Toll RFID reads happen in a split second near heavy metal and electrical noise, and that noise comes in bursts."
2. "Our Review 1 design used Hamming, which fixes one bit. Watch what happens with two flipped bits." → show Hamming SILENT_WRONG / DETECTED_FAIL.
3. "We added a CRC check after decoding, so a wrong ID is never accepted silently."
4. "We generalised Hamming to BCH codes, which fix 2–3 bits per block." → same seed, BCH: all CORRECT.
5. "Hospital imaging areas have even stronger bursts; that's why Reed–Solomon with interleaving and an adaptive controller come next week."
6. "Correction takes microseconds, versus a full round trip for retransmission." → point at latency / plot.

---

## 8. If something goes wrong

| Problem | Fix |
|---|---|
| `make: command not found` / `gcc: not found` | Run the setup commands in section 1 again |
| `Address already in use` | An old run is still open: `pkill -f bin/` then retry |
| Nothing arrives at the toll gate | Start order matters: tollgate → channel → vehicle |
| Weird symbols instead of colours | Add `--no-color` to each command |
| `No module named matplotlib` | Activate the venv and `pip install -r requirements.txt` (section 6) |
| `make compare` / `demo-hospital` missing | That phase didn't finish; check `PROGRESS.md` and demo `make demo` only |
| Repo looks empty after cloning | You're on `main`; merge the pull request or `git checkout` the claude branch (section 2) |
| Tests fail | Don't fix it live. Demo whatever passes, and paste the error into the Debug prompt later |

**Do a full dry run once before presenting.**
