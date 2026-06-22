# AFI Monthly Production Runbook — Issue 006 (25 June 2026)

Send these as **separate messages in one continuous chat thread**, not separate sessions. Each prompt assumes Claude still has the prior steps' output in context. Reuse this template every month by swapping the issue number, date, and any thesis-revision notes.

---

## Before you start: pick your build path

**Default (recommended)**: don't ask Claude to produce `index.html` at all. Generate the markdown only, commit it, and let your existing `build.yml` CI handle the HTML build on push.

**Alternative**: if you want Claude to hand you rendered HTML directly in this chat, upload `afi_parser.py`, `build.py`, `templates/index.j2`, and `templates/issue.j2` into the conversation *before* Prompt 5, then add the build instruction shown at the end of Prompt 5 below.

---

## PROMPT 1 — Planning checkpoint

```
Produce Issue 006 — the first monthly-format AFI issue, publishing Thursday 25 June 2026.

Run Steps 1–3 of the pipeline only:
1. Memory Agent — produce the Pre-Production Memory Brief. This is the first
   monthly issue, so also log the Cadence Transition Flag in Register 1 now
   (prior cadence: weekly; new cadence: monthly, starting this issue).
2. Planning Agent — full Issue Brief: situational assessment, 3–5 thesis
   candidates with scoring, the selected monthly thesis and its defence, the
   Section Emphasis Map, and all six agent briefing packages.
3. Orchestrator — confirm thesis distribution and quality gate priorities.

Also flag whether a brief masthead note announcing the format change to
readers is warranted for this issue.

Stop after Step 3. Do not run Research, Risk, Category, or Strategic agents
yet — I want to review and approve the thesis before the rest of the
pipeline runs against it.
```

**Your job here**: read the thesis and its defence. Either approve it, or ask for a different angle before continuing — this is the cheapest point in the whole process to redirect.

---

## PROMPT 2 — Research + Risk

```
Thesis approved. Continue the pipeline:
Step 5 — Research Intelligence: produce the Monthly Intelligence Brief.
Step 6 — Risk Analyst: produce Black Swan Watch and the Fragility Index.
```

If you want a different thesis instead, replace the first line with: *"Revise the thesis to [your direction] instead, then continue with Steps 5–6."*

---

## PROMPT 3 — Category Intelligence

```
Continue: Step 7 — Category Analyst. Produce all 8 category sections (5A–5H).
```

---

## PROMPT 4 — Strategic layer

```
Continue: Step 8 — Strategic Analyst. Produce Hidden Profit Pools,
Second-Order Effects, and the 9 Strategic Recommendations.
```

---

## PROMPT 5 — Final assembly

```
Continue: Step 9 — Writer-Editor. Produce the Title, Executive Brief,
Contrarian Take, and Closing Line, then perform the full editorial pass and
assemble the complete document. Confirm total word count is 7,500–9,000
words (Section 2.6) before presenting.

Output two things:
1. The complete content/issue-006.md file, including YAML front matter,
   ready to drop into the repo.
2. The 5-line edit to content/index.md adding the Issue 006 entry.
```

**If you uploaded the build files**, append:
```
Also run python3 build.py --all using the uploaded build files and present
the generated issue-006.html and index.html.
```

---

## PROMPT 6 — Audit

```
Continue: Step 10 — Auditor Agent. Run all 7 audit passes against the
assembled issue-006.md. Give me the full Audit Report, the publication
decision, and the Memory Agent update instructions.
```

If the decision is **CLEARED WITH REVISIONS** or **RETURNED FOR REVISION**, send a follow-up prompt listing the blocking issues and asking the Writer-Editor (or the relevant analytical agent) to resolve them — then re-request the affected check only, not a full re-audit.

---

## After CLEARED

1. Copy `issue-006.md` into `afi-build/content/`
2. Apply the 5-line `index.md` edit
3. Commit and push — `build.yml` builds and commits the HTML back automatically
4. (Only if you skipped CI and built in-chat instead) download and commit the `issue-006.html` / `index.html` Claude generated directly

---

## Reuse next month

Duplicate this file, swap "Issue 006" → "Issue 007," the date → the next last Thursday, and drop the Cadence Transition Flag line from Prompt 1 (one-time only). Everything else repeats unchanged.
