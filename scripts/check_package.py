#!/usr/bin/env python3
"""Keep the public plugin package valid for every store and free of secrets.

Run from the repo root: python3 scripts/check_package.py
Needs `jsonschema` (Agent Plugins 1.0.0 schemas are vendored in scripts/schemas).
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MCP_URL = "https://accounting.igdrasil.se/api/mcp"
NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SECRET = re.compile(r"sk-ant-|sk-[A-Za-z0-9]{20}|ghp_|github_pat_|Bearer [A-Za-z0-9]|CLIENT_SECRET|BEGIN [A-Z ]*PRIVATE KEY")


def load(rel, problems):
    try:
        return json.loads((ROOT / rel).read_text())
    except (OSError, json.JSONDecodeError) as error:
        problems.append(f"{rel}: {error}")
        return {}


def check(problems):
    claude = load(".claude-plugin/plugin.json", problems)
    portable = load("plugin.json", problems)
    claude_mcp = load(".mcp.json", problems)
    portable_mcp = load("mcp.json", problems)

    import jsonschema  # noqa: PLC0415 - optional dependency, fail loudly here
    for doc, schema in [(portable, "plugin"), (portable_mcp, "mcp")]:
        validator = jsonschema.Draft202012Validator(
            json.loads((ROOT / f"scripts/schemas/{schema}.schema.json").read_text()))
        problems += [f"{schema}.json: {'/'.join(map(str, e.path)) or '(root)'}: {e.message}"
                     for e in validator.iter_errors(doc)]

    for label, doc in [("Claude", claude), ("portable", portable)]:
        name = doc.get("name", "")
        if not (NAME.match(name) and len(name) <= 64):
            problems.append(f"{label} plugin name {name!r} must be kebab-case, <=64 chars")
        for field in ("description", "version", "author", "license"):
            if not doc.get(field):
                problems.append(f"{label} plugin.json missing {field}")
    if claude.get("version") != portable.get("version"):
        problems.append("plugin versions differ between .claude-plugin/plugin.json and plugin.json")

    for label, doc in [(".mcp.json", claude_mcp), ("mcp.json", portable_mcp)]:
        server = (doc.get("mcpServers") or {}).get("igdrasil") or {}
        if server.get("url") != MCP_URL:
            problems.append(f"{label}: igdrasil url must be {MCP_URL}")
        if "headers" in server:
            problems.append(f"{label}: remote servers must not carry headers")
    if (claude_mcp.get("mcpServers") or {}).get("igdrasil", {}).get("type") != "http":
        problems.append(".mcp.json: igdrasil type must be http")

    interface = ((portable.get("extensions") or {}).get("com.openai") or {}).get("interface") or {}
    for field in ("logo", "composerIcon"):
        if not interface.get(field) or not (ROOT / interface[field]).is_file():
            problems.append(f"plugin.json interface.{field} must point at a file in the repo")

    if len((ROOT / "README.md").read_text().split()) < 40:
        problems.append("README.md must have at least 40 words")
    if not (ROOT / "LICENSE").is_file():
        problems.append("LICENSE is missing")

    skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
    if not skills:
        problems.append("no skills/*/SKILL.md found")
    for skill in skills:
        head = skill.read_text().split("---")
        front = head[1] if len(head) > 2 else ""
        if f"name: {skill.parent.name}" not in front or "description:" not in front:
            problems.append(f"{skill.relative_to(ROOT)}: frontmatter needs name matching dir + description")

    for path in ROOT.rglob("*"):
        if path.is_file() and ".git" not in path.parts and path.suffix in {".json", ".md", ".py", ".yml", ".yaml", ""}:
            if path.name == "check_package.py":
                continue
            if SECRET.search(path.read_text(errors="ignore")):
                problems.append(f"{path.relative_to(ROOT)}: looks like it contains a secret")


def main():
    problems = []
    check(problems)
    for problem in problems:
        print(f"FAIL {problem}")
    print("OK" if not problems else f"{len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
