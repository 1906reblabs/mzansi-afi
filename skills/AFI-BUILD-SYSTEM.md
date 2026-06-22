# AFI BUILD SYSTEM

## Publishing schedule

Issues publish monthly, on the **last Thursday of each calendar month** (exception: if the last Thursday of December falls within the final week of the month, publish on the preceding Thursday instead). Target length per issue: **7,500–9,000 words** — see AFI-WRITER-EDITOR.md, Section 2.4 for the section-by-section budget.

## What the LLM generates each month

Two Markdown files only. No HTML. No CSS. No templates.

### 1. content/issue-NNN.md  (~400–650 lines, depending on prose density within YAML string fields)
The full issue content in structured Markdown + YAML front matter.
The build system converts this to issue-NNN.html automatically.

### 2. content/index.md  (5-line edit only)
Add the new issue entry to the `issues:` YAML block at the top.
Everything else in the file is unchanged.

## Build command (run after generating content)
    cd /home/claude/afi-build && python3 build.py --all

## File naming
    issue-001.html, issue-002.html, issue-003.html ...
    Always zero-padded to 3 digits.

## Issue content schema (YAML front matter)

    ---
    issue_number: "006"
    date: "30 July 2026"
    title: "Full Issue Title Here"
    thesis: "Single sentence monthly thesis."
    lens: "Political / Regulatory"
    audit_score: 84
    target_word_count: 8200
    
    fragility_scores:
      health:        {score: 9, trend: "↑", breaks_first: "..."}
      commercial:    {score: 8, trend: "↑", breaks_first: "..."}
      short_term:    {score: 8, trend: "↑", breaks_first: "..."}
      reinsurance:   {score: 7, trend: "↑", breaks_first: "..."}
      life:          {score: 6, trend: "→", breaks_first: "..."}
      specialised:   {score: 6, trend: "↑", breaks_first: "..."}
      microinsurance:{score: 5, trend: "→", breaks_first: "..."}
      insurtech:     {score: 6, trend: "↑", breaks_first: "..."}
      aggregate:     6.9
    
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
    
    recommendations:
      insurers:
        - move: "Short title"
          body: "..."
          why_now: "..."
      brokers:
        - move: "Short title"
          body: "..."
          why_now: "..."
      regulators:
        - move: "Short title"
          body: "..."
          why_now: "..."
    
    categories:
      life:
        contrarian: "..."
        risk: "..."
        opportunity: "..."
      health:
        contrarian: "..."
        risk: "..."
        opportunity: "..."
      # ... repeat for all 8
    ---
    
    ## Executive Brief
    [180–220 words prose]
    
    ## Second-Order Effects
    ### Trend Name
    [Causal chain narrative]
    
    ## The Contrarian Take
    [210–260 words prose]
    
    ## Closing Line
    [Single sentence, max 30 words]

**Notes on the schema:**
- `date`: must be the actual last Thursday of the target month (or the December-exception date) — not an arbitrary date within the month.
- `target_word_count`: optional, documentation-only at present. Set it to the figure the Writer-Editor verified at Section 2.6 (final assembled total, 7,500–9,000). Not currently enforced by `build.py`, but reserved for a future word-count validation step.

## Build system files (in GitHub repo, not project files)
    afi-build/
    ├── afi_parser.py        Parser (issue + index)
    ├── build.py             Build runner
    ├── content/             Generated content files
    └── templates/
        ├── index.j2         Index page template
        └── issue.j2         Issue page template
