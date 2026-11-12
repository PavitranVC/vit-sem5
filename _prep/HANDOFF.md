# Handoff for another AI agent (Antigravity, Gemini, Cursor, anything)

Read this first, then `_prep/README.md`, `_prep/plan/priority-blocks.md`, `_prep/context.md`. Last updated Thu 12 Nov 2026, 15:45 IST.

## Who and what
V C Pavitran, VIT Vellore B.Tech CSE. FAT exams 13-30 Nov 2026 (dates in `_prep/plan/schedule.md`). He started late, panics when he sits down to study, and learns badly by passively reading slides. Be calm, short, practical. Remind him to sleep (by midnight on the night before an exam).

## Rules
- Do not delete, rename or move existing files. Put new notes under `_prep/`.
- Do not commit or push without his explicit approval.
- He may have local files that are not in git. Never run `git reset --hard`, `git clean`, or anything that discards local changes.

## State right now
- His exam tomorrow is CAD (Cloud Architecture Design, folder `AWS/`), Fri 13 Nov 9:30. He has prepared Module 1 only. Everything else is from scratch.
- CAD FAT shape: 10 questions x 10 marks, one scenario question per module, answers are designs. Modules 1, 2, 4, 6 weigh 10 marks each; 3, 5, 7, 8 weigh 20. About 10 of the 50 questions give a choice.
- Teaching method that works for him: TEST him, do not lecture. Ask one question, let him answer in his own words, say what is right, correct the missing part in 2-3 lines, ask the next. A session of 5 questions per topic gives him proof he remembers.

## CAD triage for the last ~18 hours (priority order, from `_prep/analysis/CAD.md` and `_prep/plan/priority-blocks.md`)
P1 (asked in 4-5 of 5 FAT papers): VPC (public/private subnets, IGW, NAT, route tables, SG vs NACL); IAM (users, groups, roles, policies, least privilege); RDS Multi-AZ vs read replicas; CloudWatch + CloudTrail + Config; SQS, SNS, Step Functions, SWF; Snow family (Snowball, Snowball Edge, Snowmobile).
P2 (3 of 5): EC2 launch steps, Auto Scaling + ELB, S3/EBS/EFS/Glacier choice, KMS, WAF, Shield, cost tools (Budgets, Cost Explorer, Trusted Advisor), RDS vs Aurora vs DynamoDB, DMS, Server Migration.
Teacher's CAT-2 DA lists 8 likely questions, all Modules 7 and 8: SQS vs SNS, fan-out with SNS+SQS, SWF vs Step Functions, Standard vs Express workflows, six pillars, server migration, DMS, Snowball family. Page map: end of `_prep/study-guide/CAD-slide-map.md`.
Answer template he should use for every scenario: 1) restate the requirement, 2) name the services, 3) small diagram, 4) one line of why per requirement (availability, scalability, security, cost).
Already covered with him in chat: public vs private subnet, NAT vs IGW, security group vs NACL. Next quiz question was "list the VPC components for a web tier + database tier".

## Suggested session shape for tomorrow-before-exam and tonight
1. Quiz him on the 6 P1 topics, 5 questions each, using the slides in `AWS/`.
2. For each DA question (Modules 7-8), have him write the answer once, then correct it.
3. Timed practice: take two questions from `_prep/pyq-index/CAD.md` and let him answer them in the 4-line template.
4. Hard stop at 23:30 on Thu 12 Nov, light recall only, sleep.

## Everything else
Per-subject block guides: `_prep/study-guide/`. Past-paper indexes: `_prep/pyq-index/`. Topic matrix (open in a browser): `_prep/analysis/important-topics.html`. Plan: `_prep/plan/schedule.md`.
