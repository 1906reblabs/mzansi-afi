# ANTIFRAGILE INSURANCE

**Weekly strategic intelligence for the South African insurance industry.**

One thesis per issue. Nine sections. Nothing published without Auditor clearance.  
Built on a ten-agent AI pipeline. Content in Markdown. HTML generated automatically.

---

## Live Publication

Served via GitHub Pages from the root of the `main` branch.

| Issue | Title | Date |
|---|---|---|
| [003](issue-003.html) | When the Constitutional Scaffolding Shakes | 19 May 2026 |
| [002](issue-002.html) | Issue 002 | May 2026 |
| [001](issue-001.html) | The Cities That Insurance Cannot Hold | May 2026 |

---

## Repository Structure

```
mzansi-afi/
│
├── .github/
│   └── workflows/
│       └── build.yml          ← Auto-builds HTML whenever content changes
│
├── afi-build/                 ← Build system (not served by GitHub Pages)
│   ├── afi_parser.py          ← Parses .md content files into template context
│   ├── build.py               ← CLI build runner
│   ├── requirements.txt       ← Python dependencies (Jinja2, Markdown, PyYAML)
│   ├── content/               ← LLM-generated content files (what you edit)
│   │   ├── index.md           ← Homepage content — update issues: block each week
│   │   ├── issue-001.md       ← Issue 001 content
│   │   ├── issue-002.md       ← Issue 002 content
│   │   └── issue-003.md       ← Issue 003 content
│   └── templates/             ← Jinja2 HTML templates (write-once, never edit)
│       ├── index.j2           ← Homepage template
│       └── issue.j2           ← Issue page template
│
├── index.html                 ← Generated — do not edit by hand
├── issue-001.html             ← Generated — do not edit by hand
├── issue-002.html             ← Generated — do not edit by hand
├── issue-003.html             ← Generated — do not edit by hand
│
└── README.md
```

> **Rule:** Only ever edit files inside `afi-build/content/`.  
> Everything in the repo root (`*.html`) is generated automatically.

---

## How the Build Pipeline Works

```
LLM generates              Python processes           Jinja2 renders
──────────────────         ──────────────────────     ─────────────────────
content/index.md    →      afi_parser.parse_index()   →   index.j2   →  index.html
content/issue-NNN.md →     afi_parser.parse_issue()   →   issue.j2   →  issue-NNN.html
```

The LLM writes only the `.md` content files — structured YAML front matter for all data, Markdown body for prose. The parser, templates, and build runner are written once and never need to change (unless the publication's design changes).

### Token efficiency

| Task | Old approach | New approach | Saving |
|---|---|---|---|
| Generate one issue | ~18,000 tokens (full HTML) | ~4,500 tokens (Markdown) | **~75%** |
| Update homepage | ~8,000 tokens (full HTML) | ~200 tokens (YAML edit) | **~97%** |
| Build HTML | ~18,000 tokens | 0 tokens (Python, ~60ms) | **100%** |

---

## Automated Build (GitHub Actions)

The workflow in `.github/workflows/build.yml` runs automatically whenever any file in `afi-build/content/` is pushed to `main`.

**Trigger conditions:**
- Push to `main` with changes to `afi-build/content/**.md`
- Push to `main` with changes to `afi-build/templates/**.j2`
- Push to `main` with changes to `afi-build/afi_parser.py`
- Manual trigger via the GitHub Actions UI

**What the workflow does:**
1. Checks out the repository
2. Installs Python 3.11 and dependencies from `afi-build/requirements.txt`
3. Runs `python3 build.py --all --output-dir ..` (writes HTML to repo root)
4. Commits and pushes any changed HTML files as `github-actions[bot]`

The commit message includes `[skip ci]` to prevent an infinite build loop.

---

## Producing a New Issue

### Step 1 — Generate the content file

Ask the AI pipeline to produce `content/issue-NNN.md` using the schema below.  
This is the only file the LLM writes. No HTML. No CSS.

### Step 2 — Update the homepage content

In `afi-build/content/index.md`, add the new issue to the top of the `issues:` YAML block:

```yaml
issues:
  - number: "004"
    date: "26 May 2026"
    title: "Your New Issue Title"
    thesis: "Single sentence weekly thesis."
    href: "issue-004.html"
    is_latest: true

  - number: "003"           # ← change is_latest to false
    ...
    is_latest: false
```

Also update `hero.eyebrow`, `hero.deco_number`, `hero.cta_primary_href`, `latest.*`, `nav.cta`, and `next_issue_number`.

### Step 3 — Push to GitHub

```bash
git add afi-build/content/
git commit -m "content: add issue 004"
git push
```

The GitHub Action takes it from there. Within ~30 seconds, `issue-004.html` and an updated `index.html` will be committed to the repo and live on GitHub Pages.

### Step 4 — Build locally (optional)

```bash
cd afi-build
pip install -r requirements.txt
python3 build.py --all          # writes to afi-build/output/
python3 build.py --issue 004    # single issue only
```

---

## Issue Content File Schema

Every issue is a single Markdown file: `afi-build/content/issue-NNN.md`

```
─────────────────────────────────────────────────────────────────────────────
YAML FRONT MATTER  (structured data — everything the template loops over)
─────────────────────────────────────────────────────────────────────────────
---
issue_number:  "004"
date:          "26 May 2026"
title:         "Full issue title"
thesis:        "Single sentence weekly thesis."
lens:          "Regulatory"
audit_score:   87
contrarian_consensus: "The consensus belief being challenged..."

fragility_scores:
  aggregate: 6.8
  health:         {score: 9, trend: "↑", text: "...", breaks_first: "..."}
  commercial:     {score: 8, trend: "↑", text: "...", breaks_first: "..."}
  short_term:     {score: 7, trend: "→", text: "...", breaks_first: "..."}
  reinsurance:    {score: 7, trend: "↑", text: "...", breaks_first: "..."}
  life:           {score: 6, trend: "→", text: "...", breaks_first: "..."}
  specialised:    {score: 6, trend: "↑", text: "...", breaks_first: "..."}
  microinsurance: {score: 5, trend: "→", text: "...", breaks_first: "..."}
  insurtech:      {score: 6, trend: "↑", text: "...", breaks_first: "..."}

black_swans:
  - name: "Short title (3–5 words)"
    tag: "Political"
    timeline: "Medium — 12–30 months"
    underestimation: "..."
    scenario: "..."
    amplifiers: "..."
    opportunity: "..."

profit_pools:
  - title: "Pool Title"
    subtitle: "One-line mechanism"
    conventional_view: "..."
    actual_economics: "..."
    why_hidden: "..."
    best_positioned: "..."
    risk: "..."

second_order:
  callout: "The trend being analysed this week."
  first_title:    "First-Order Effects — Obvious (0–6 months)"
  first_content:  "Paragraph text. Supports **bold**."
  second_title:   "Second-Order Effects — Non-Obvious (6–24 months)"
  second_content: "Multi-paragraph text. **Bold headings** supported."
  third_title:    "Third-Order Effects — Structural Implications (2–7 years)"
  third_content:  "Paragraph text."
  pivot:          "The strategic pivot point sentence."

recommendations:
  insurers:
    - move: "Short action title"
      body: "What to do specifically."
      why_now: "Why this week, not next month."
  brokers:
    - move: "..."
      body: "..."
      why_now: "..."
  regulators:
    - move: "..."
      body: "..."
      why_now: "..."

categories:
  life:
    contrarian:  "..."
    risk:        "..."
    opportunity: "..."
  health:
    contrarian:  "..."
    risk:        "..."
    opportunity: "..."
  short_term:    {contrarian: "...", risk: "...", opportunity: "..."}
  commercial:    {contrarian: "...", risk: "...", opportunity: "..."}
  specialised:   {contrarian: "...", risk: "...", opportunity: "..."}
  reinsurance:   {contrarian: "...", risk: "...", opportunity: "..."}
  microinsurance:{contrarian: "...", risk: "...", opportunity: "..."}
  insurtech:     {contrarian: "...", risk: "...", opportunity: "..."}
---

─────────────────────────────────────────────────────────────────────────────
MARKDOWN BODY  (prose sections — rendered to HTML by the parser)
─────────────────────────────────────────────────────────────────────────────

## Executive Brief
150–200 words. Three paragraphs: thesis statement, why this week,
who wins and who loses. Supports **bold** and *italic*.

## The Contrarian Take
200–250 words. Three paragraphs: the counter-argument, the evidence,
the strategic implication. Supports **bold** for emphasis.

## Closing Line
One sentence only. Maximum 30 words. No exclamation marks.
```

---

## Ten-Agent Production Pipeline

Every issue is produced by a coordinated AI pipeline before the content file is written.

| Step | Agent | Produces |
|---|---|---|
| 01 | Memory Agent | Pre-production brief — prior issues, open claims, fragility trends |
| 02 | Planning Agent | Weekly thesis, section emphasis map, agent briefing packages |
| 03 | Orchestrator | Thesis distribution, quality gates |
| 04 | RAG Agent | Evidence retrieval from 7 knowledge domains (on demand) |
| 05 | Research Intelligence | Weekly Intelligence Brief across 6 signal domains |
| 06 | Risk Analyst | Black Swan Watch (§2), Fragility Index (§3) |
| 07 | Category Analyst | Category Intelligence §5A–5H |
| 08 | Strategic Analyst | Hidden Profit Pools (§4), Second-Order Effects (§6), Recommendations (§7) |
| 09 | Writer-Editor | Executive Brief (§1), Contrarian Take (§8), Closing Line (§9), full editorial pass |
| 10 | Auditor Agent | 7-pass quality audit — nothing publishes without clearance |

The pipeline outputs a single `.md` content file. The build system converts it to HTML.

---

## Four Intellectual Frameworks

Every agent applies these frameworks. They are not referenced decoratively — they determine what gets written and what gets cut.

**Taleb — Antifragility & Tail Risk**  
Classify systems as fragile, robust, or antifragile. Prioritise the shape of distributions over their means. Identify who has skin in the game.

**Thiel — Monopoly, Secrets & Zero-to-One**  
Find the "secret" — the thing that is true but that most of the industry has not accepted. The Contrarian Take is a Thiel question answered weekly.

**Systems — Feedback Loops & Nonlinearity**  
Map reinforcing and balancing loops. Second-order effects are not optional analysis — they are the core of AFI's predictive value.

**Kahneman — Behavioral Economics**  
Policyholders, brokers, and underwriters do not behave as rational agents. Identify the specific biases producing the mispricings and hidden profit pools that AFI exists to surface.

---

## Setup

### GitHub Pages configuration

1. Go to **Settings → Pages**
2. Source: **Deploy from a branch**
3. Branch: `main` / `/ (root)`
4. Save

The site will be live at `https://<your-username>.github.io/mzansi-afi/`

### Local development

```bash
git clone https://github.com/<your-username>/mzansi-afi.git
cd mzansi-afi/afi-build
pip install -r requirements.txt
python3 build.py --all          # generates HTML into afi-build/output/
python3 build.py --all --output-dir ..   # generates HTML into repo root
```

---

## Disclaimer

ANTIFRAGILE INSURANCE does not constitute financial, legal, or regulatory advice.  
All analysis represents original editorial judgement.
