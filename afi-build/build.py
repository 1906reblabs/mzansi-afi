#!/usr/bin/env python3
"""
build.py
────────
AFI static site builder.

Usage
─────
  python3 build.py                   # build everything (index + all issues)
  python3 build.py --all             # same
  python3 build.py --index           # build index.html only
  python3 build.py --issue 003       # build one issue by number
  python3 build.py --dry-run         # parse + render, print to stdout, no files written

How it works
────────────
  1. afi_parser.parse(content/file.md)   ->  context dict
  2. jinja2_env.get_template(*.j2)       ->  template object
  3. template.render(**context)          ->  HTML string
  4. Write to output/

File layout expected
────────────────────
  afi-build/
    afi_parser.py
    build.py
    content/
      index.md
      issue-001.md
      issue-002.md
      ...
    templates/
      index.j2
      issue.j2
    output/         <-- generated HTML appears here
"""

from __future__ import annotations

import argparse
import glob
import sys
import time
from pathlib import Path

import jinja2

sys.path.insert(0, str(Path(__file__).parent))
import afi_parser

# ── Paths ─────────────────────────────────────────────────────────────────────

BASE      = Path(__file__).parent
CONTENT   = BASE / "content"
TEMPLATES = BASE / "templates"
OUTPUT    = BASE / "output"

OUTPUT.mkdir(exist_ok=True)

# ── Jinja2 environment ────────────────────────────────────────────────────────

def _make_env() -> jinja2.Environment:
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(str(TEMPLATES)),
        autoescape=jinja2.select_autoescape(["html", "j2"]),
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
    )
    env.filters["enumerate"] = enumerate
    return env

ENV = _make_env()

# ── Build functions ────────────────────────────────────────────────────────────

def build_index(dry_run: bool = False) -> str | None:
    """Parse content/index.md -> output/index.html"""
    src = CONTENT / "index.md"
    if not src.exists():
        raise FileNotFoundError(f"Missing: {src}")
    ctx  = afi_parser.parse_index(src)
    html = ENV.get_template("index.j2").render(**ctx)
    if dry_run:
        print(html)
        return None
    out = OUTPUT / "index.html"
    out.write_text(html, encoding="utf-8")
    return str(out)


def build_issue(number: str, dry_run: bool = False) -> str | None:
    """Parse content/issue-NNN.md -> output/issue-NNN.html"""
    padded = number.zfill(3)
    src    = CONTENT / f"issue-{padded}.md"
    if not src.exists():
        raise FileNotFoundError(f"Missing: {src}")
    ctx  = afi_parser.parse_issue(src)
    html = ENV.get_template("issue.j2").render(**ctx)
    if dry_run:
        print(html)
        return None
    out = OUTPUT / f"issue-{padded}.html"
    out.write_text(html, encoding="utf-8")
    return str(out)


def build_all(dry_run: bool = False) -> list[str]:
    """Build index + every issue-NNN.md found in content/"""
    built = []

    result = build_index(dry_run)
    if result:
        built.append(result)

    for src in sorted(glob.glob(str(CONTENT / "issue-*.md"))):
        num = Path(src).stem.split("-")[-1]   # "issue-003" -> "003"
        result = build_issue(num, dry_run)
        if result:
            built.append(result)

    return built


# ── CLI ───────────────────────────────────────────────────────────────────────

def main() -> None:
    p = argparse.ArgumentParser(description="AFI static site builder")
    g = p.add_mutually_exclusive_group()
    g.add_argument("--all",   action="store_true", help="Build index + all issues (default)")
    g.add_argument("--index", action="store_true", help="Build index only")
    g.add_argument("--issue", metavar="NNN",       help="Build one issue, e.g. --issue 003")
    p.add_argument("--dry-run", action="store_true", help="Print HTML to stdout, no files written")
    args = p.parse_args()

    t0 = time.perf_counter()

    # Default (no flags) = --all
    if args.index:
        pages = [r for r in [build_index(args.dry_run)] if r]
    elif args.issue:
        pages = [r for r in [build_issue(args.issue, args.dry_run)] if r]
    else:
        pages = build_all(args.dry_run)

    elapsed = (time.perf_counter() - t0) * 1000

    if not args.dry_run:
        print(f"\n✓  Built {len(pages)} page(s) in {elapsed:.1f}ms\n")
        for path in pages:
            size_kb = Path(path).stat().st_size / 1024
            print(f"   {path}  ({size_kb:.1f} KB)")
        print("\n   Pipeline:  content/*.md  ->  afi_parser  ->  templates/*.j2  ->  output/")


if __name__ == "__main__":
    main()
