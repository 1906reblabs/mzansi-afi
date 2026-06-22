---
name: AFI-SYSTEM-README
description: Master documentation for the ANTIFRAGILE INSURANCE (AFI) multi-agent publication system. Read this first to understand how all five skill agents fit together, in what order to invoke them, and how to maintain publication quality across issues.
---

# ANTIFRAGILE INSURANCE (AFI)
## Multi-Agent Publication System — Architecture Guide

---

## SYSTEM OVERVIEW

AFI is produced by a pipeline of **nine specialist agents** — five analytical, one orchestrating, one planning, one memory, one retrieval, and one auditing. Each agent owns a distinct cognitive layer of the publication. No single agent can produce the full publication — the quality emerges from the pipeline.

```
┌──────────────────────────────────────────────────────────────────┐
│  AFI-MEMORY-AGENT (persistent across all issues)                  │
│  Registers: Issue Archive · Claim Log · Fragility History ·       │
│  Coverage Map · Performance Dashboard                             │
└────────────┬─────────────────────────────────────────────────────┘
             │ Pre-Production Memory Brief
┌────────────▼─────────────────────────────────────────────────────┐
│  AFI-PLANNING-AGENT                                               │
│  Thesis selection · Section emphasis map · Agent briefing pkgs    │
└────────────┬─────────────────────────────────────────────────────┘
             │ Issue Brief
┌────────────▼─────────────────────────────────────────────────────┐
│  AFI-ORCHESTRATOR                                                 │
│  Sets thesis · Briefs agents · Quality gates                      │
└──────┬──────────────────────────────────────────────────────┬────┘
       │                                                      │
       │  ┌───────────────────────────────────────────────┐  │
       │  │  AFI-RAG-AGENT (on-demand, throughout pipeline)│  │
       │  │  7 knowledge domains · Evidence retrieval ·    │  │
       │  │  Active regulatory/market/climate triggers     │  │
       │  └───────────────────────────────────────────────┘  │
       │                                                      │
┌──────▼────────────┐                                         │
│ AFI-RESEARCH-     │                                         │
│ INTELLIGENCE      │                                         │
│ 6 signal domains  │                                         │
└──────┬────────────┘                                         │
       │ Intelligence Brief                                   │
┌──────▼────────────────┐                                     │
│ AFI-RISK-ANALYST      │                                     │
│ Sections 2 & 3        │                                     │
└──────┬────────────────┘                                     │
       │                                                      │
┌──────▼───────────────────────┐                              │
│ AFI-CATEGORY-ANALYST         │                              │
│ Section 5 (A–H)              │                              │
└──────┬───────────────────────┘                              │
       │                                                      │
┌──────▼──────────────────┐                                   │
│ AFI-STRATEGIC-ANALYST   │                                   │
│ Sections 4, 6, 7        │                                   │
└──────┬──────────────────┘                                   │
       │                                                      │
┌──────▼──────────┐                                           │
│ AFI-WRITER-     │                                           │
│ EDITOR          │                                           │
│ Secs 0,1,8,9    │                                           │
│ Full edit       │                                           │
└──────┬──────────┘                                           │
       │ Final assembled document                             │
┌──────▼──────────────────────────────────────────────────────▼────┐
│  AFI-AUDITOR-AGENT                                                │
│  7 audit passes · Blocking issues · Publication decision          │
│  → Memory Agent post-publication update                           │
└───────────────────────────────────────────────────────────────────┘
                              │
                       ┌──────▼──────┐
                       │  PUBLISHED   │
                       │  AFI ISSUE   │
                       └─────────────┘
```

---

## AGENT DIRECTORY

| Skill File | Agent Role | Pipeline Position |
|---|---|---|
| `AFI-MEMORY-AGENT.md` | Institutional memory, cross-issue continuity, 5 persistent registers | Pre-production + post-publication |
| `AFI-PLANNING-AGENT.md` | Issue planning, thesis selection, section emphasis, agent briefing packages | First (before Orchestrator) |
| `AFI-ORCHESTRATOR.md` | Master coordinator, thesis distribution, quality gatekeeper | Second |
| `AFI-RAG-AGENT.md` | Knowledge base management, evidence retrieval across 7 domains | On-demand throughout pipeline |
| `AFI-RESEARCH-INTELLIGENCE.md` | Intelligence gathering across 6 signal domains | Third |
| `AFI-RISK-ANALYST.md` | Black Swan Watch, Fragility Index (Sections 2 & 3) | Fourth |
| `AFI-CATEGORY-ANALYST.md` | Eight insurance category deep-dives (Section 5 A–H) | Fifth |
| `AFI-STRATEGIC-ANALYST.md` | Hidden Profit Pools, Second-Order Effects, Recommendations (Sections 4, 6, 7) | Sixth |
| `AFI-WRITER-EDITOR.md` | Framing sections + full editorial assembly (Sections 0, 1, 8, 9) | Seventh |
| `AFI-AUDITOR-AGENT.md` | 7-pass quality audit, publication decision, Memory Agent update instructions | Last (post-assembly) |

---

## INVOCATION SEQUENCE

**Always invoke in this exact order:**

```
0. AFI-MEMORY-AGENT         → Produces Pre-Production Memory Brief
1. AFI-PLANNING-AGENT       → Receives Memory Brief → Produces Issue Brief + agent briefing packages
2. AFI-ORCHESTRATOR         → Receives Issue Brief → Distributes thesis + briefs to all agents
   [AFI-RAG-AGENT]          → Available on-demand to any agent from this point forward
3. AFI-RESEARCH-INTELLIGENCE → Receives Research Brief → Produces Weekly Intelligence Brief
4. AFI-RISK-ANALYST         → Receives Intelligence Brief + Risk Brief → Produces Sections 2 & 3
5. AFI-CATEGORY-ANALYST     → Receives all above + Category Brief → Produces Section 5 (A–H)
6. AFI-STRATEGIC-ANALYST    → Receives all above + Strategic Brief → Produces Sections 4, 6, 7
7. AFI-WRITER-EDITOR        → Receives all above + Writer Brief → Produces Sections 0,1,8,9 + edits all
8. AFI-AUDITOR-AGENT        → Receives final document + Issue Brief + Memory Brief + RAG log → Audits
   [AFI-MEMORY-AGENT]       → Post-publication: updates all 5 registers with Auditor instructions
```

**Context passing is mandatory.** Each agent must receive all prior agent outputs, not just its immediate predecessor's output. The Strategic Analyst, in particular, must have read both the Risk Analysis and the Category Intelligence before producing its sections.

---

## THE WEEKLY THESIS

The weekly thesis is the intellectual spine of every issue. It is a single, defensible, non-obvious claim about the SA insurance industry. Everything in the publication either supports, extends, or provides evidence for this claim.

**Thesis quality criteria:**
- Specific: names a mechanism, not just a trend
- Debatable: a smart executive could disagree
- Consequential: if true, someone should do something different
- Timely: connected to something happening right now

**Examples:**
> "South African personal lines insurers are systematically underpricing household underinsurance risk because their sum-insured models are calibrated to declared values, not replacement costs — creating a latent R200B+ liability that one inflationary shock will surface."

> "The coming NHI implementation will not reduce medical scheme membership — it will bifurcate the market into a state-adjacent minimum benefit utility and a premium product priced on exclusivity, with current open schemes caught in the unprofitable middle."

> "South Africa's microinsurance regulatory framework has created a licensing regime that protects incumbents more than it enables innovation — the R2bn embedded insurance opportunity is being captured by the least regulated participants in the value chain."

---

## PUBLICATION STRUCTURE (FULL)

```
0.  Title                          — AFI-WRITER-EDITOR
1.  Executive Brief                — AFI-WRITER-EDITOR
2.  Black Swan Watch               — AFI-RISK-ANALYST
3.  Fragility Index                — AFI-RISK-ANALYST
4.  Hidden Profit Pools            — AFI-STRATEGIC-ANALYST
5.  Category Intelligence (A–H)   — AFI-CATEGORY-ANALYST
    A. Life Insurance
    B. Health / Medical Schemes
    C. Short-Term (Personal Lines)
    D. Commercial Insurance
    E. Specialised Insurance
    F. Reinsurance
    G. Microinsurance
    H. Insurtech / Emerging Models
6.  Second-Order Effects           — AFI-STRATEGIC-ANALYST
7.  Strategic Recommendations      — AFI-STRATEGIC-ANALYST
8.  The Contrarian Take            — AFI-WRITER-EDITOR
9.  Closing Line                   — AFI-WRITER-EDITOR
```

---

## INTELLECTUAL FRAMEWORKS (ALL AGENTS APPLY)

Every agent in the pipeline applies these four frameworks. They are not optional analytical tools — they are the cognitive DNA of AFI.

### 1. Taleb: Antifragility & Tail Risk
- Systems are not just "risky" or "safe" — they are fragile (hurt by disorder), robust (neutral), or antifragile (gain from disorder)
- The goal is not to eliminate risk but to identify and exploit asymmetry
- Fat tails: the shape of the distribution matters more than its mean
- Skin in the game: who bears the consequences of the risks they create?

**Application in AFI:** Every Fragility Index score, every Black Swan Watch entry, and every Strategic Recommendation should be evaluated through this lens. Is the recommendation making the system more antifragile, or just less fragile?

### 2. Thiel: Monopoly, Secrets & Zero-to-One
- Real value is created by companies that do something no one else does (zero-to-one), not by competition (one-to-n)
- "Secrets" are things that are true but that most people don't believe — including about insurance economics
- The best businesses are monopolies disguised as competitive markets

**Application in AFI:** Hidden Profit Pools should identify monopoly dynamics. Category opportunities should distinguish zero-to-one innovations from derivative competition. The Contrarian Take is explicitly Thiel's "important truth that few agree with you on."

### 3. Systems Thinking: Feedback Loops & Nonlinearity
- Linear models underestimate nonlinear outcomes
- Feedback loops (reinforcing and balancing) drive emergent behaviour
- Small changes at leverage points produce disproportionate system-wide effects

**Application in AFI:** Second-Order Effects is the formal systems thinking section, but the lens applies everywhere. What reinforcing loops are accelerating fragility? What balancing loops are providing resilience? Where are the leverage points?

### 4. Behavioral Economics: Irrational Actors in Insurance
- Policyholders, brokers, and underwriters do not behave as rational economic agents
- Key biases: loss aversion (over-insure some risks, ignore others), present bias (underprice long-term risks), herding (correlated underwriting errors), availability bias (price recent events too heavily, ignore unseen risks)
- These biases create persistent mispricings that are the source of many hidden profit pools

**Application in AFI:** Hidden Profit Pools section should always identify at least one behavioral source of mispricing. Category Intelligence should regularly surface irrational policyholder or underwriter behaviour as a distinct risk or opportunity.

---

## STYLE GUIDE (ALL AGENTS)

### Voice
- Confident and direct. No hedging.
- Analytical but readable. No jargon without purpose.
- Slightly provocative. Every issue should make at least one powerful person uncomfortable.
- Not sensationalist. Provocation must be earned with evidence.

### Forbidden phrases
| Avoid | Replace with |
|---|---|
| "could potentially" | [the direct claim] |
| "it could be argued" | "the argument is" or just make the argument |
| "in today's landscape" | [delete] |
| "digital transformation" | [specify what is actually being digitised] |
| "at a crossroads" | [specify the choice] |
| "may be at risk" | "is fragile" or "faces [specific risk]" |
| "research suggests" | [specific evidence or direct assertion] |
| "going forward" | [delete] |

### Numbers and specificity
- Always prefer a specific number over a directional claim where evidence exists
- If no specific number is available, say so explicitly and give the directional claim
- Do not invent numbers. Estimated ranges with stated uncertainty are acceptable.

### Paragraph length
- Maximum 4 sentences per paragraph in most sections
- Executive Brief: 2–3 sentences per paragraph
- Contrarian Take: 3–4 sentences per paragraph
- Second-Order Effects: up to 5 sentences per paragraph (more discursive)

---

## THEMATIC ROTATION

To prevent repetition across issues, the Orchestrator rotates the primary analytical lens:

| Issue Theme | Core Lens | Featured Trend in Section 6 |
|---|---|---|
| Regulatory | FSCA/PA/COFI | Conduct reform second-order effects |
| Climate | Physical + transition risk | Property underwriting restructuring |
| Political | ANC/GNU/expropriation | Commercial risk repricing |
| Technology | AI, fraud, insurtech | Distribution disintermediation |
| Macro | Rand, rates, inflation | Technical reserve adequacy |
| Behavioral | Consumer distress, fraud | Moral hazard and lapse dynamics |

Never use the same primary lens in consecutive issues.

---

## QUALITY GATES (ORCHESTRATOR ENFORCES)

Before the Writer-Editor produces the final document, the Orchestrator checks:

✅ Does every section connect to the weekly thesis?  
✅ Is there at least one claim a senior executive would push back on?  
✅ Are there specific numbers, names, or mechanisms in every section?  
✅ Is South Africa the primary context in every section?  
✅ Is any insight repeated across sections? (Assign to one, remove from others)  
✅ Does the Contrarian Take contradict a specific, widely-held belief?  
✅ Are all strategic recommendations actionable within 12 months?  
✅ Is the closing line memorable in isolation?  

---

## REGULATORY AWARENESS (ALL AGENTS)

All agents must be aware of the SA insurance regulatory framework:

| Regulator | Mandate | Key Focus for AFI |
|---|---|---|
| **FSCA** (Financial Sector Conduct Authority) | Market conduct, treating customers fairly, intermediary oversight | COFI Bill, TCF, conduct enforcement, product approval |
| **Prudential Authority (PA)** | Solvency, capital adequacy, systemic risk | SAM framework, capital buffers, reinsurance oversight |
| **Council for Medical Schemes (CMS)** | Medical scheme regulation | NHI interface, PMBs, scheme solvency |
| **Competition Commission** | Market competition | Distribution concentration, bancassurance dominance |
| **National Treasury** | Tax policy, retirement reform | Insurance product tax treatment, retirement annuity regulation |

Agents should reference specific regulatory instruments (e.g., "PA Directive 5 of 2022," "FSCA Communication 5 of 2023") where available. Generic "regulatory risk" references are insufficient.

---

*AFI Multi-Agent System — Architecture v1.0*  
*Designed for weekly publication cadence. All agents operate in sequence, not in parallel.*
