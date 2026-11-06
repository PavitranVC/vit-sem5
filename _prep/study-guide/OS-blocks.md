# OS study guide: blocks for 7-14 Nov (exam Sun 15 Nov, 9:30)

Files are under `OS/`. Page numbers come from `_prep/study-guide/OS-slide-map.md`.
Your starting point: Modules 1-3 and the numericals feel easy; the fear is Module 4 (race conditions, semaphores, classical problems). So the plan front-loads Module 4 and revisits it three times.
The OS PYQ index (`_prep/pyq-index/OS.md`) is not written yet; PYQ-driven priorities will be added after all subjects are indexed.

## Sat 7 Nov, evening: Module 4a (race condition, critical section, semaphores)
- `OS/MOD 4/concurrency-material.pdf` pp.21-43: process synchronization, race condition (p.29), critical section (pp.30-31), Peterson's solution (pp.32-34), bakery (p.35), TestAndSet and Swap (pp.36-41), semaphores (pp.42-43)
- Do: after each idea, write it from memory (what goes wrong without it; what it fixes). For a race condition, trace two threads doing `counter++` by hand with an interleaving that loses an update.
- Skip for now: pp.2-20 (IPC, pipes), pp.58-65 (monitors). They come in 8 Nov or revision.

## Sun 8 Nov, evening: Module 4b (classical problems, monitors)
- Same file, pp.44-65: bounded buffer (pp.44-47), readers-writers (pp.48-50), dining philosophers (pp.51-53), problems with semaphores (p.54), no-busy-wait implementation (pp.55-57), monitors and condition variables (pp.58-65)
- Learn these four templates and write each from memory:
  1. mutex around a critical section
  2. producer-consumer with `empty`, `full`, `mutex`
  3. readers-writers
  4. dining philosophers
- For each, answer: why does each semaphore exist, and what happens if two `wait` calls are swapped?

## Mon 9 Nov, afternoon: Module 5, memory management
- `OS/MOD 5/memory-management.pptx` slides 1-53: base/limit, relocation, contiguous allocation (first/best/worst fit, p.15 example), fragmentation, paging, TLB and effective access time (pp.28-30), hierarchical and hashed/inverted page tables, segmentation
- You said numericals are easy, so spend the time on the diagrams of address translation and the page-table structures.

## Mon 9 Nov, evening: Module 5 virtual memory + Module 3 refresher
- `memory-management.pptx` slides 54-95: demand paging, page-fault handling, page replacement (FIFO, optimal, LRU, p.73 reference string, Belady's anomaly p.76), thrashing and working set (pp.90-95)
- Quick refresher of numericals: `OS/MOD 3/module3.pdf` pp.6-19 (FCFS, SJF, priority, SRTF, RR) and pp.32-39 (I/O burst problems); `OS/MOD 3/deadlocks.pdf` pp.26-33 (Banker's algorithm)

## Tue 10 Nov, morning: Module 6, virtualization and file systems
- `OS/MOD 6/virtualization.pdf` pp.2-23 (hypervisors, trap-and-emulate, binary translation, nested page tables, containers)
- `OS/MOD 6/File-systems.pdf` pp.2-52: access methods, directory structures, allocation methods (contiguous, linked/FAT, indexed pp.27-39), recovery and journaling (pp.40-42), log-structured and distributed file systems (pp.41-52)

## Tue 10 Nov, afternoon: Module 7, disk, protection, security
- `OS/MOD 7/module-7.pdf` pp.2-17 (disk structure and scheduling: FCFS, SSTF, SCAN, C-SCAN, C-LOOK; practice example p.17)
- pp.18-37 (access control, domain of protection, access matrix with copy/owner/control rights)
- pp.38-53 (security threats and attacks, policy vs mechanism, network security models)

## Wed 11 Nov, afternoon: semaphore problems again
- Re-open `concurrency-material.pdf` pp.21-65 and rewrite all four templates from memory, then check. Then write monitor solutions for producer-consumer and dining philosophers (pp.58-65).

## Fri 13 Nov, afternoon (after the CAD exam): timed mixed paper
- Pick one OS FAT paper from `OS/PYQ/FAT/` and write it under exam conditions (up to 3 hours). Focus on numericals first (scheduling, Banker's, page replacement, disk scheduling), then the sync problems.

## Sat 14 Nov, morning: final problem set + weak spots
- Rewrite the four semaphore templates one last time.
- 60-minute skim of Modules 1-2 (the easy part, so keep it fast): `Module1.pdf` pp.34-53 (OS types, modes, structure approaches), `Module2.pdf` pp.2-23 (system calls, interrupts), pp.29-31 (process states, PCB), pp.41-51 (fork, zombies, orphans), pp.64-81 (threads).
- Evening: light recall only, sleep by 11.
