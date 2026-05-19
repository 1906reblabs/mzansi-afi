"""
afi_parser.py
─────────────
Parses AFI Markdown content files into Jinja2 template context dicts.

Two file types supported — auto-detected from YAML front matter:

  content/index.md          → parse_index()   → rendered by templates/index.j2
  content/issue-NNN.md      → parse_issue()   → rendered by templates/issue.j2

Both file types use the same structure:
  - YAML front matter between --- delimiters (structured data)
  - Markdown body (prose sections that need rich-text rendering)

Public API
──────────
  parse(path)          Auto-detect file type and parse.
  parse_index(path)    Parse an index content file.
  parse_issue(path)    Parse an issue content file.
"""

from __future__ import annotations

import re
import sys
import textwrap
from pathlib import Path
from typing import Any

import yaml
import markdown
from markdown.extensions.tables import TableExtension
from markdown.extensions.attr_list import AttrListExtension


# ── Markdown renderer ──────────────────────────────────────────────────────────

_MD = markdown.Markdown(
    extensions=[TableExtension(), AttrListExtension(), "fenced_code", "nl2br"]
)


def _md(text: str) -> str:
    """Render Markdown string to HTML, resetting parser state each call."""
    if not text or not text.strip():
        return ""
    _MD.reset()
    return _MD.convert(textwrap.dedent(text).strip())


# ── Front-matter splitter ──────────────────────────────────────────────────────

_FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n(.*)", re.DOTALL)


def _split(raw: str) -> tuple[dict[str, Any], str]:
    """Split YAML front matter from Markdown body. Returns (front_dict, body_str)."""
    m = _FM_RE.match(raw)
    if not m:
        raise ValueError(
            "Content file must begin with a YAML front matter block (--- ... ---)\n"
            f"Got: {raw[:120]!r}"
        )
    return yaml.safe_load(m.group(1)) or {}, m.group(2)


# ── Body section splitter ──────────────────────────────────────────────────────

def _sections(body: str) -> dict[str, str]:
    """Return {h2_title: body_text} for every ## heading in the body."""
    out: dict[str, str] = {}
    parts = re.split(r"^## (.+)$", body, flags=re.MULTILINE)
    it = iter(parts[1:])
    for title, content in zip(it, it):
        out[title.strip()] = content.strip()
    return out


# ── Category metadata (fixed order A-H) ───────────────────────────────────────

_CAT_ORDER = [
    "life", "health", "short_term", "commercial",
    "specialised", "reinsurance", "microinsurance", "insurtech",
]

_CAT_META = {
    "life":           {"letter": "A", "name": "Life Insurance",
                       "subtitle": "The Longevity Trade"},
    "health":         {"letter": "B", "name": "Health / Medical Schemes",
                       "subtitle": "Healthcare Convexity"},
    "short_term":     {"letter": "C", "name": "Short-Term: Personal Lines",
                       "subtitle": "Everyday Risk Is Not Normal"},
    "commercial":     {"letter": "D", "name": "Commercial Insurance",
                       "subtitle": "Corporate Fragility Map"},
    "specialised":    {"letter": "E", "name": "Specialised Insurance",
                       "subtitle": "Edge Markets"},
    "reinsurance":    {"letter": "F", "name": "Reinsurance",
                       "subtitle": "The System Behind the System"},
    "microinsurance": {"letter": "G", "name": "Microinsurance",
                       "subtitle": "Mass Market Experiments"},
    "insurtech":      {"letter": "H", "name": "Insurtech / Emerging Models",
                       "subtitle": "Zero-to-One Insurance"},
}


def _frag_class(score: int | float) -> str:
    if score >= 8: return "high"
    if score >= 6: return "med"
    return "low"


# ── Pipeline agent data (static) ──────────────────────────────────────────────

_AGENTS = [
    {"step": "Step 01", "name": "Memory Agent",         "deco": "M",
     "role": "Maintains five persistent registers of prior issue history, claim "
             "performance, fragility score trends, and contrarian positions taken."},
    {"step": "Step 02", "name": "Planning Agent",        "deco": "P",
     "role": "Selects the weekly thesis, designs the section emphasis map, and "
             "produces individual briefing packages for every downstream agent."},
    {"step": "Step 03", "name": "Orchestrator",          "deco": "O",
     "role": "Distributes the thesis, manages context passing between agents, "
             "and enforces quality gates before final assembly."},
    {"step": "Step 04", "name": "RAG Agent",             "deco": "R",
     "role": "Evidence engine. Manages seven knowledge domains and responds to "
             "structured evidence queries from any agent at any pipeline stage."},
    {"step": "Step 05", "name": "Research Intelligence", "deco": "RI",
     "role": "Scans six signal domains - regulatory, macro, climate, political, "
             "market, and behavioural - to produce the Weekly Intelligence Brief."},
    {"step": "Step 06", "name": "Risk Analyst",          "deco": "RA",
     "role": "Produces Section 2 (Black Swan Watch) and Section 3 (Fragility Index) "
             "using Taleb's tail-risk and antifragility frameworks."},
    {"step": "Step 07", "name": "Category Analyst",      "deco": "CA",
     "role": "Produces eight category intelligence sections (5A-5H) covering every "
             "major SA insurance segment. One contrarian insight, one risk, one "
             "opportunity per category."},
    {"step": "Step 08", "name": "Strategic Analyst",     "deco": "SA",
     "role": "Produces Hidden Profit Pools (4), Second-Order Effects (6), and "
             "Strategic Recommendations (7). The argument's strategic conclusion."},
    {"step": "Step 09", "name": "Writer-Editor",         "deco": "WE",
     "role": "Writes the title, Executive Brief, Contrarian Take, and Closing Line. "
             "Full editorial pass enforcing voice, eliminating repetition, assembling "
             "the final document."},
    {"step": "Step 10", "name": "Auditor Agent",         "deco": "AU",
     "role": "Seven-pass quality audit: factual accuracy, logical consistency, "
             "specificity, longitudinal consistency, regulatory accuracy, intellectual "
             "honesty, and publication readiness."},
]


# ── parse_index ────────────────────────────────────────────────────────────────

def parse_index(content_path: str | Path) -> dict[str, Any]:
    """Parse content/index.md -> context dict for templates/index.j2."""
    raw  = Path(content_path).read_text(encoding="utf-8")
    front, body = _split(raw)
    secs = _sections(body)

    # Pillars: "- **Title** - Body text"
    pillars = []
    for line in secs.get("Publication Pillars", "").splitlines():
        line = line.strip()
        if not line.startswith("-"):
            continue
        m = re.match(r"-\s*\*\*(.+?)\*\*\s*[-\u2014\u2013]+\s*(.+)", line)
        if m:
            pillars.append({"title": m.group(1).strip(), "body": m.group(2).strip()})

    # Nine sections table
    pub_sections = []
    for line in secs.get("Nine Sections, One Argument", "").splitlines():
        line = line.strip()
        if (not line.startswith("|")
                or line.startswith("| Section")
                or set(line.replace("|", "").replace("-", "").strip()) == set()):
            continue
        cells = [c.strip() for c in line.split("|") if c.strip()]
        if len(cells) >= 3:
            pub_sections.append({"number": cells[0], "title": cells[1], "body": cells[2]})

    # Frameworks: ### Thinker - Concept
    frameworks = []
    for chunk in re.split(r"^### ", secs.get("Four Frameworks, Applied Relentlessly", ""),
                          flags=re.MULTILINE):
        chunk = chunk.strip()
        if not chunk:
            continue
        header, _, fw_body = chunk.partition("\n")
        m = re.match(r"(.+?)\s*[-\u2014\u2013]+\s*(.+)", header)
        if m:
            frameworks.append({
                "thinker": m.group(1).strip(),
                "concept": m.group(2).strip(),
                "body":    fw_body.strip(),
            })

    return {
        "site":              front.get("site_name", "Antifragile Insurance"),
        "tagline":           front.get("site_tagline", ""),
        "description":       front.get("site_description", ""),
        "nav":               front.get("nav", {}),
        "hero":              front.get("hero", {}),
        "latest":            front.get("latest", {}),
        "issues":            front.get("issues", []),
        "next_issue_number": front.get("next_issue_number", ""),
        "reg_badges":        front.get("reg_badges", []),
        "about_html":        _md(secs.get("About the Publication", "")),
        "pillars":           pillars,
        "pub_sections":      pub_sections,
        "frameworks":        frameworks,
        "agents":            _AGENTS,
    }


# ── parse_issue ────────────────────────────────────────────────────────────────

def parse_issue(content_path: str | Path) -> dict[str, Any]:
    """Parse content/issue-NNN.md -> context dict for templates/issue.j2."""
    raw  = Path(content_path).read_text(encoding="utf-8")
    front, body = _split(raw)
    secs = _sections(body)

    # Fragility scores
    frag_raw  = front.get("fragility_scores", {})
    aggregate = frag_raw.get("aggregate", 0)
    frag_list = []
    for key in _CAT_ORDER:
        if key not in frag_raw:
            continue
        val   = frag_raw[key]
        score = val.get("score", 0)
        frag_list.append({
            "key":          key,
            "name":         _CAT_META[key]["name"],
            "subtitle":     _CAT_META[key]["subtitle"],
            "score":        score,
            "trend":        val.get("trend", "->"),
            "text":         val.get("text", ""),
            "breaks_first": val.get("breaks_first", ""),
            "bar_pct":      f"{score * 10}%",
            "color_class":  _frag_class(score),
        })
    frag_list.sort(key=lambda x: x["score"], reverse=True)

    # Categories
    cats_raw   = front.get("categories", {})
    categories = []
    for key in _CAT_ORDER:
        if key not in cats_raw:
            continue
        meta = _CAT_META[key]
        cat  = cats_raw[key]
        categories.append({
            "key":        key,
            "letter":     meta["letter"],
            "label":      f"§ 5{meta['letter']} — {meta['name']}",
            "name":       meta["name"],
            "subtitle":   meta["subtitle"],
            "contrarian": cat.get("contrarian", ""),
            "risk":       cat.get("risk", ""),
            "opportunity":cat.get("opportunity", ""),
        })

    # Second-order effects
    so = front.get("second_order", {})
    second_order = {
        "callout":      so.get("callout", ""),
        "first_title":  so.get("first_title",  "First-Order Effects — Obvious (0-6 months)"),
        "first_html":   _md(so.get("first_content",  "")),
        "second_title": so.get("second_title", "Second-Order Effects — Non-Obvious (6-24 months)"),
        "second_html":  _md(so.get("second_content", "")),
        "third_title":  so.get("third_title",  "Third-Order Effects — Structural Implications (2-7 years)"),
        "third_html":   _md(so.get("third_content",  "")),
        "pivot":        so.get("pivot", ""),
    }

    # Recommendations
    recs_raw = front.get("recommendations", {})
    recommendations = {
        "insurers":   recs_raw.get("insurers",   []),
        "brokers":    recs_raw.get("brokers",     []),
        "regulators": recs_raw.get("regulators",  []),
    }

    return {
        # Metadata
        "issue_number": front.get("issue_number", ""),
        "date":         front.get("date", ""),
        "title":        front.get("title", ""),
        "thesis":       front.get("thesis", ""),
        "lens":         front.get("lens", ""),
        "audit_score":  front.get("audit_score", 0),

        # Structured sections
        "black_swans":          front.get("black_swans", []),
        "fragility_scores":     frag_list,
        "aggregate_score":      aggregate,
        "profit_pools":         front.get("profit_pools", []),
        "categories":           categories,
        "second_order":         second_order,
        "recommendations":      recommendations,

        # Contrarian
        "contrarian_consensus": front.get("contrarian_consensus", ""),

        # Prose (rendered Markdown from body)
        "exec_brief_html":  _md(secs.get("Executive Brief", "")),
        "contrarian_html":  _md(secs.get("The Contrarian Take", "")),
        "closing_line":     secs.get("Closing Line", "").strip(),
    }


# ── Auto-detect and route ──────────────────────────────────────────────────────

def parse(content_path: str | Path) -> dict[str, Any]:
    """Auto-detect file type (index vs issue) and call the right parser."""
    raw   = Path(content_path).read_text(encoding="utf-8")
    front, _ = _split(raw)
    return parse_issue(content_path) if "issue_number" in front else parse_index(content_path)


# ── CLI (debug) ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import json

    path = sys.argv[1] if len(sys.argv) > 1 else "content/index.md"

    def _ser(obj: Any) -> Any:
        if isinstance(obj, dict): return {k: _ser(v) for k, v in obj.items()}
        if isinstance(obj, list): return [_ser(i) for i in obj]
        return obj

    print(json.dumps(_ser(parse(path)), indent=2, ensure_ascii=False))
