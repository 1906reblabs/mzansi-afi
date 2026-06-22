# ANTIFRAGILE INSURANCE — Weekly → Monthly Migration Spec (Rev. 2)

**Revision note:** Rev. 1 of this spec targeted 4,500–5,000 words, treating the cadence shift mainly as a length-cutting exercise. Benchmarked against comparable premium periodic intelligence products — McKinsey Quarterly's long-form ("fifty-minute read") format, Eurasia Group's *Top Risks*, BCG/Oliver Wyman/Swiss Re-style industry reports — that target was too aggressive for AFI's actual positioning as a C-suite intelligence publication rather than a newsletter. **Revised target: 7,500–9,000 words**, close to the top of the original weekly range. Most Rev. 1 structural cuts are reversed below; the real discipline monthly cadence requires is sharper signal selection upstream (Research/Planning), not compression downstream (Writer-Editor).

**New cadence:** Last Thursday of each calendar month
**New target length:** 7,500–9,000 words

## Next six publish dates

| Month | Last Thursday |
|---|---|
| June 2026 | 25 June |
| July 2026 | 30 July |
| August 2026 | 27 August |
| September 2026 | 24 September |
| October 2026 | 29 October |
| November 2026 | 26 November |

**December flag:** the literal last Thursday of December 2026 is **31 December** — New Year's Eve. Standing exception rule: *"Last Thursday, or the preceding Thursday if the last Thursday falls in the final week of December."* Write this into AFI-PLANNING-AGENT.md.

---

## Master Word Budget (Rev. 2)

| Section | Original (weekly) | **Rev. 2 — monthly target** |
|---|---|---|
| 0. Title | 5–12 words | unchanged |
| 1. Executive Brief | 150–200 | **180–220** |
| 2. Black Swan Watch | 3–5 risks × 150–200w | **3–5 risks (default 4) × 160–200w** |
| 3. Fragility Index | 8 × 100–150w | **8 × 120–150w** — Hidden Leverage Point and What Breaks First stay as separate blocks |
| 4. Hidden Profit Pools | 2–3 pools × 200–300w | **2–3 pools × 220–280w** |
| 5A–5H Categories | 8 × 250–350w | **8 × 270–340w, uniform treatment** — no PRIMARY/STANDARD tiering |
| 6. Second-Order Effects | 400–600 | **450–600** |
| 7. Strategic Recommendations | 9 × 100–150w | **9 × 110–140w** |
| 8. Contrarian Take | 200–250 | **210–260** |
| 9. Closing Line | ≤30 words | unchanged |
| **Total** | ~5,300–8,300 | **~7,500–9,000** |

**What actually changes from the original weekly budget: almost nothing mechanically.** Executive Brief and Second-Order Effects nudge slightly larger (more to synthesize per issue). Strategic Recommendations trims slightly. Everything else is essentially the original weekly target carried forward.

**What the Planning Agent's PRIMARY/SECONDARY/STANDARD emphasis map now governs:** depth and sharpness of insight — which risks or categories get the most ambitious, thesis-central treatment — **not** word count. All 8 categories get the full three-part structure at comparable length; emphasis determines which ones the Category Analyst pushes hardest on, not which ones get cut short.

---

## 1. Skill File Changes

### AFI-ORCHESTRATOR.md
- "WEEKLY ISSUE PIPELINE" → "MONTHLY ISSUE PIPELINE"; "weekly thesis" / "weekly issue" → "monthly thesis" / "monthly issue" throughout
- Replace the per-section word table with a pointer to the Rev. 2 master table in AFI-WRITER-EDITOR.md
- Thematic Calendar: note that each lens now spans a full month, so the six-lens rotation completes roughly **twice per year**
- Special Issue protocol: Regulatory Response / Catastrophe Response issues can still fire **between** scheduled monthly issues, labelled "Special Edition," and don't consume the next sequential issue number

### AFI-PLANNING-AGENT.md
- "Invoked once per weekly production cycle" → "once per monthly production cycle, in the week before the last Thursday"
- Phase 1.1: "Scan the past 7 days" → "Scan the period since the last published issue (~30 days)"
- **Add a triage step.** This matters more under Rev. 2 than it would under a shorter target — the word budget barely moved from weekly to monthly, but the raw signal volume to scan did. The Research Brief has to filter a month's worth of developments down to what's genuinely thesis-relevant, or sections built for a week's evidence will feel crowded with a month's worth crammed in
- Thesis Exclusion List lookback: "last 6 issues" → **last 8 issues** (now 8 months, proportionate to the slower cadence)
- Add the December exception rule above
- Section Emphasis Map: PRIMARY/SECONDARY/STANDARD now signals depth of ambition, not a word-count tier

### AFI-RESEARCH-INTELLIGENCE.md
- "Weekly Intelligence Brief" → "Monthly Intelligence Brief" throughout
- "Top 5 signals this week" → "Top 6–8 signals this month"
- Add a distinction between **this month's new signals** and **longer-running trends carried over from prior months**
- This agent is the primary mechanism absorbing the weekly→monthly volume increase. Because word budgets stay close to original, the Research Agent's filtering discipline — not the Writer-Editor's compression — is what keeps the publication sharp rather than diffuse

### AFI-RISK-ANALYST.md
- Black Swan Watch: **3–5 risks**, 160–200 words each, defaulting to 4 in a typical issue
- Fragility Index: keep "Hidden Leverage Point" and "What Breaks First" as **separate** labelled blocks, 120–150 words per sub-sector total

### AFI-CATEGORY-ANALYST.md
- All 8 categories: uniform three-part structure (contrarian insight / risk scenario / opportunity), 270–340 words each — **no PRIMARY/STANDARD word-count tiering**
- Planning Agent's emphasis designations still appear in the brief, but instruct the Category Analyst on which 2–3 categories deserve the most aggressive, thesis-central insight — not which ones get shorter treatment

### AFI-STRATEGIC-ANALYST.md
- Hidden Profit Pools: **2–3 pools**, 220–280 words each, full five-part structure intact
- Strategic Recommendations: stays at 9 (3 insurers / 3 brokers / 3 regulators), light trim to 110–140 words each

### AFI-WRITER-EDITOR.md
- Section 2.4 becomes the canonical Rev. 2 master word-budget table above
- Executive Brief target: 180–220 words
- Final QA step before Auditor handoff: confirm total assembled document is **7,500–9,000 words**

### AFI-AUDITOR-AGENT.md
- Pass 7 checklist: add `□ Total word count between 7,500–9,000`
- Pass 3 Specificity: no calibration changes needed — original rule stands as written (minimum 2 Level 3 claims per section, including all 8 categories, since there's no tiering to accommodate)
- Pass 4 Longitudinal Consistency: "repeated... from the last 4 issues" → "last 6 issues" (≈6 months, proportionate to the new cadence)

### AFI-MEMORY-AGENT.md
- "Longitudinal Pattern Report (every 6 issues)" → consider **every 4 issues** (≈ quarterly) — every-6 means twice a year, too infrequent a feedback loop at monthly cadence
- Fragility Score History annotations: "week-over-week" framing → "month-over-month" where implied
- See the continuity flag below — the one non-optional addition, independent of word count

### AFI-RAG-AGENT.md
- No functional changes required.

---

## 2. GitHub Repo / Code Changes

The build pipeline (`build.py`, `afi_parser.py`) doesn't need functional changes for the cadence shift — it parses markdown → HTML regardless of frequency. The changes are in rendered copy and a couple of optional additions.

### `templates/issue.j2`
Hardcoded footer text currently reads *"ANTIFRAGILE INSURANCE is published weekly..."* (visible in all three existing issue pages). Change to *"published monthly."* One-line template fix; future builds inherit it automatically — no need to touch already-published historical pages.

### `templates/index.j2`
Literal copy describing the *current* state of the publication should update now:
- Meta description: "Weekly strategic intelligence..." → "Monthly strategic intelligence..."
- Hero body: "A weekly strategic publication..." → "A monthly strategic publication..."
- About section prose: "It is a weekly argument" → "It is a monthly argument"

`index.html` regenerates via `build.py --all`, so fixing the template is sufficient.

### `build.yml` (GitHub Actions)
No required change — push-triggered on `afi-build/content/**.md`, cadence-agnostic. Optional: a scheduled (`cron`) reminder workflow ahead of each month's last Thursday.

### `build.py` / `afi_parser.py`
Optional: a word-count check that warns (doesn't block) if the generated issue falls outside **7,500–9,000 words**. Catches budget drift before publication rather than at the Auditor stage.

### Issue numbering & historical pages
Continue sequential numbering uninterrupted (next issue is still `issue-006.html`, just monthly from here). Consider a one-line masthead note on the first monthly issue announcing the format change.

*Aside, unrelated to cadence:* `issue-002.html`'s internal `<title>` and content still read "Issue 001" — worth a quick fix while in the templates.

---

## 3. Project Instructions Updates

Add a new section near the top of the project instructions, after "YOUR IDENTITY":

> **PUBLICATION CADENCE**
> AFI publishes monthly, on the last Thursday of each calendar month (see December exception). Target length is 7,500–9,000 words per issue — close to the top of the original weekly range, reflecting AFI's positioning as a premium intelligence publication rather than a newsletter. Canonical word-budget table lives in AFI-WRITER-EDITOR.md, Section 2.4. Special/rapid-response editions (regulatory, catastrophe) may still be issued between scheduled monthly issues; they are labelled "Special Edition" and do not displace the next regular issue.

Other edits:
- Pipeline Sequence (Step 5): "Weekly Intelligence Brief" → "Monthly Intelligence Brief"
- "HOW TO RESPOND TO USER REQUESTS" examples: "Produce this week's issue" → "Produce this month's issue"
- Add to "MANDATORY BEHAVIOUR": **Signal Selection Discipline** — the constraint that matters at monthly cadence is what gets into the Research Brief and the Planning Agent's thesis selection, not how tightly the Writer-Editor compresses prose afterward. Word count stayed close to the original; the volume of raw material to choose from did not.
- "OUTPUT FORMAT" section: require the Writer-Editor to confirm total word count is within 7,500–9,000 before the Auditor pass begins.

---

## 4. README.md / AFI-BUILD-SYSTEM.md

### AFI-BUILD-SYSTEM.md
- Add a cadence line near the top: *"Issues publish monthly, on the last Thursday of each calendar month."*
- Update the example `date:` field in the YAML schema to a last-Thursday date
- Optional: add a `target_word_count` field to the front matter for documentation/validation purposes (7,500–9,000)

### Root `README.md`
Not in the project files, but for the repo's top-level README:
- Tagline/description: "weekly" → "monthly"
- New section: **Publishing schedule** — last Thursday of each month, December exception noted
- Word-count target documented for any future contributor: 7,500–9,000
- Consider a changelog entry documenting the transition date and the previous cadence (see below — this matters for the Memory Agent, not just human readers)

---

## Critical: flag the transition for the Memory Agent

This is the one change that's easy to skip and will cause subtle bugs later, and it's entirely independent of the word-count question. The Memory Agent's longitudinal checks — open predictive claim timelines, fragility score change windows, "repeated in the last N issues" repetition checks — all implicitly assumed **weekly** spacing between issues. Once the cadence changes, "the last 4 issues" suddenly means 4 months instead of 4 weeks, and a claim with a "SHORT (0–18 months)" timeline set under weekly cadence will be checked against a completely different number of *issues* elapsed even though the same amount of *calendar time* has passed.

Add a permanent entry to Register 1 (Issue Archive) or a new "Editorial Operations Log" noting: **the exact issue number and date the cadence changed, and what the prior cadence was.** This lets future Planning Briefs and Auditor passes correctly interpret issue-to-issue gaps instead of silently miscalculating elapsed time.

---

## Suggested rollout order

Because most sections land close to their original structure under Rev. 2, this is a lighter lift than a true rewrite:

1. Update AFI-WRITER-EDITOR.md's master word-budget table first — everything else cites it
2. Update Orchestrator + Planning Agent cadence language, the December rule, and the "emphasis = depth, not length" framing
3. Confirm AFI-RISK-ANALYST.md and AFI-STRATEGIC-ANALYST.md keep their flexible counts (3–5 risks, 2–3 pools) — no structural change needed beyond cadence language
4. Confirm AFI-CATEGORY-ANALYST.md treats all 8 categories uniformly — no tiering to introduce
5. Update Auditor's word-count checklist line and Pass 4 lookback window
6. Add the Memory Agent continuity flag
7. Fix `templates/issue.j2` and `templates/index.j2`, then rebuild
8. Update the project instructions and README.md
9. Produce the first monthly issue as a live test; audit it; recalibrate if any section runs structurally over or under its new band
