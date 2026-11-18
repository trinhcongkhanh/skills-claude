#!/usr/bin/env python3
"""Validate every skill in plugins/*/skills/ and the marketplace/plugin manifests.

Checks:
  - SKILL.md exists (exact case) in each skill folder
  - YAML frontmatter has `name` and `description`
  - `name` is kebab-case, matches the folder, <= 64 chars, no "claude"/"anthropic"
  - `description` is non-empty, <= 1024 chars, no angle brackets
  - no README.md inside skill folders
  - every .json file in the repo parses
Exit code 1 on any error.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KEBAB = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
errors: list[str] = []


def parse_frontmatter(text: str) -> dict:
    """Minimal parser for simple `key: value` frontmatter (no nested YAML needed)."""
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    data = {}
    for line in text[4:end].splitlines():
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip()
    return data


skill_dirs = sorted(p for p in ROOT.glob("plugins/*/skills/*") if p.is_dir())
if not skill_dirs:
    errors.append("no skills found under plugins/*/skills/")

for skill in skill_dirs:
    rel = skill.relative_to(ROOT)
    skill_md = skill / "SKILL.md"
    if not skill_md.is_file():
        errors.append(f"{rel}: missing SKILL.md (exact case)")
        continue
    if (skill / "README.md").exists():
        errors.append(f"{rel}: README.md not allowed inside a skill folder")

    fm = parse_frontmatter(skill_md.read_text(encoding="utf-8"))
    name, desc = fm.get("name", ""), fm.get("description", "")

    if not name:
        errors.append(f"{rel}: frontmatter missing `name`")
    elif not KEBAB.match(name) or len(name) > 64:
        errors.append(f"{rel}: name '{name}' must be kebab-case, max 64 chars")
    elif name != skill.name:
        errors.append(f"{rel}: name '{name}' must match folder '{skill.name}'")
    if re.search(r"claude|anthropic", name, re.I):
        errors.append(f"{rel}: name must not contain 'claude' or 'anthropic'")

    if not desc:
        errors.append(f"{rel}: frontmatter missing `description`")
    elif len(desc) > 1024:
        errors.append(f"{rel}: description is {len(desc)} chars (max 1024)")
    if "<" in desc or ">" in desc:
        errors.append(f"{rel}: description must not contain angle brackets")

    print(f"  ok  {name or rel}  ({len(desc)} chars description)")

for jf in ROOT.rglob("*.json"):
    if ".git" in jf.parts or "node_modules" in jf.parts:
        continue
    try:
        json.loads(jf.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"{jf.relative_to(ROOT)}: invalid JSON ({exc})")

if errors:
    print("\nValidation FAILED:")
    for e in errors:
        print(f"  x {e}")
    sys.exit(1)
print(f"\nValidation passed: {len(skill_dirs)} skills.")
