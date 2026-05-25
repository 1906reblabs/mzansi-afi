#!/usr/bin/env python3
"""
build.py
────────
AFI static site builder.

Usage
─────
  python3 build.py                          # build everything (index + all issues)
  python3 build.py --all                    # same as above
  python3 build.py --index                  # build index.html only
  python3 build.py --issue 003              # build one issue by number
  python3 build.py --all --output-dir ..    # write HTML to parent directory (CI use)
  python3 build.py --dry-run                # parse + render, print to stdout

How it works
────────────
  1. afi_parser.parse(content/file.md)  →  context dict
  2. jinja2_env.get_template(*.j2)      →  template object
  3. template.render(**context)         →  HTML string
  4. Write to --output-dir (default: ./output/)

Repo layout expected
────────────────────
  afi-build/
    afi_parser.py
    build.py
    requirements.txt
    content/
      index.md
      issue-001.md  ...
    templates/
      index.j2
      issue.j2
    output/          ← default local output (ignored by git)
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

def build_index(output_dir: Path, dry_run: bool = False) -> str | None:
    """Parse content/index.md → <output_dir>/index.html"""
    src = CONTENT / "index.md"
    if not src.exists():
        raise FileNotFoundError(f"Missing content file: {src}")
    ctx  = afi_parser.parse_index(src)
    html = ENV.get_template("index.j2").render(**ctx)
    if dry_run:
        print(html)
        return None
    out = output_dir / "index.html"
    out.write_text(html, encoding="utf-8")
    return str(out)


def build_issue(number: str, output_dir: Path, dry_run: bool = False) -> str | None:
    """Parse content/issue-NNN.md → <output_dir>/issue-NNN.html"""
    padded = number.zfill(3)
    src    = CONTENT / f"issue-{padded}.md"
    if not src.exists():
        raise FileNotFoundError(f"Missing content file: {src}")
    ctx  = afi_parser.parse_issue(src)
    html = ENV.get_template("issue.j2").render(**ctx)
    if dry_run:
        print(html)
        return None
    out = output_dir / f"issue-{padded}.html"
    out.write_text(html, encoding="utf-8")
    return str(out)


def build_all(output_dir: Path, dry_run: bool = False) -> list[str]:
    """Build index + every issue-NNN.md found in content/"""
    built = []

    result = build_index(output_dir, dry_run)
    if result:
        built.append(result)

    for src in sorted(glob.glob(str(CONTENT / "issue-*.md"))):
        num    = Path(src).stem.split("-")[-1]   # "issue-003" → "003"
        result = build_issue(num, output_dir, dry_run)
        if result:
            built.append(result)

    return built

# ── CLI ───────────────────────────────────────────────────────────────────────

def main() -> None:
    p = argparse.ArgumentParser(description="AFI static site builder")

    # What to build
    g = p.add_mutually_exclusive_group()
    g.add_argument("--all",   action="store_true",
                   help="Build index + all issues (default when no flag given)")
    g.add_argument("--index", action="store_true",
                   help="Build index.html only")
    g.add_argument("--issue", metavar="NNN",
                   help="Build one issue by number, e.g. --issue 003")

    # Output + debug
    p.add_argument("--output-dir", metavar="PATH", default=None,
                   help="Directory to write HTML files into "
                        "(default: ./output/ — use .. to write to repo root in CI)")
    p.add_argument("--dry-run", action="store_true",
                   help="Render to stdout only, write no files")

    args = p.parse_args()

    # Resolve output directory
    if args.output_dir:
        output_dir = Path(args.output_dir).resolve()
    else:
        output_dir = BASE / "output"

    if not args.dry_run:
        output_dir.mkdir(parents=True, exist_ok=True)

    t0 = time.perf_counter()

    if args.index:
        pages = [r for r in [build_index(output_dir, args.dry_run)] if r]
    elif args.issue:
        pages = [r for r in [build_issue(args.issue, output_dir, args.dry_run)] if r]
    else:
        pages = build_all(output_dir, args.dry_run)

    elapsed = (time.perf_counter() - t0) * 1000

    if not args.dry_run:
        print(f"\n✓  Built {len(pages)} page(s) in {elapsed:.1f}ms")
        print(f"   Output → {output_dir}\n")
        for path in pages:
            size_kb = Path(path).stat().st_size / 1024
            print(f"   {Path(path).name:<30} {size_kb:.1f} KB")
        print()
        print("   Pipeline:  content/*.md  →  afi_parser  →  templates/*.j2  →  HTML")


if __name__ == "__main__":
    main()
