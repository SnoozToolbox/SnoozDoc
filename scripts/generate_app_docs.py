"""
generate_app_docs.py
====================
Creates missing app documentation pages from CEAMSApps.json.

Apps are documented alongside tools under the same category folders
(Preprocessing / Processing / Postprocessing).

Run from the SnoozDoc repo:
    python scripts/generate_app_docs.py

What it does
------------
1. Reads CEAMSApps.json for the current app list.
2. For every app that already has a .rst page: does nothing.
3. For every NEW app (no .rst yet):
   - Creates a skeleton .rst with TODOs.
   - Appends the page to the category toctree.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
SNOOZDOC_ROOT = SCRIPT_DIR.parent
WORKSPACE_ROOT = SNOOZDOC_ROOT.parent

CEAMS_BASE = WORKSPACE_ROOT / "snooz-package-ceams" / "apps" / "CEAMSApps"
OUTPUT_BASE = SNOOZDOC_ROOT / "user_guide" / "tools"

# Historical doc filenames that do not match item_name.
# New apps fall back to ``{Category}/{item_name}.rst``.
DOC_FILE_MAP: dict[str, str] = {
    "EEGInspector": "Preprocessing/EEGInspector.rst",
    "Oximeter": "Preprocessing/Oximeter.rst",
}

APP_NAME_RE = re.compile(r"\*\*App name:\*\*\s+``([^`]+)``")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def category_folder(menu_category: str) -> str:
    """'1-Preprocessing' -> 'Preprocessing'."""
    return re.sub(r"^\d+-", "", menu_category).strip()


def read_json() -> list[dict]:
    """Return list of app dicts from CEAMSApps.json."""
    data = json.loads((CEAMS_BASE / "CEAMSApps.json").read_text(encoding="utf-8"))
    package_version = data.get("package_version", "")
    apps: list[dict] = []
    for item in data["items"]:
        if item.get("item_type") != "app":
            continue
        hooks = item["item_hooks"][0]["parameters"]
        apps.append({
            "name": item["item_name"],
            "label": hooks["menu_label"],
            "category": hooks["menu_category"],
            "version": item["item_version"],
            "package_version": package_version,
        })
    return apps


def index_existing_by_app_name() -> dict[str, Path]:
    """Scan docs for pages that already declare **App name:** ``X``."""
    found: dict[str, Path] = {}
    if not OUTPUT_BASE.exists():
        return found
    skip = {"tools.rst", "Preprocessing.rst", "Processing.rst", "Postprocessing.rst"}
    for path in OUTPUT_BASE.rglob("*.rst"):
        if path.name in skip:
            continue
        match = APP_NAME_RE.search(path.read_text(encoding="utf-8-sig", errors="replace"))
        if match:
            found[match.group(1)] = path
    return found


def rst_path(app: dict, by_name: dict[str, Path]) -> Path:
    """Resolve the .rst path for an app (existing mapping or default)."""
    if app["name"] in DOC_FILE_MAP:
        return OUTPUT_BASE / DOC_FILE_MAP[app["name"]]
    if app["name"] in by_name:
        return by_name[app["name"]]
    folder = category_folder(app["category"])
    return OUTPUT_BASE / folder / f"{app['name']}.rst"


# ---------------------------------------------------------------------------
# Create pages
# ---------------------------------------------------------------------------

def create_skeleton_rst(app: dict, path: Path) -> None:
    """Write a new app page matching the style of existing app docs."""
    label = app["label"]
    anchor = path.stem
    folder = category_folder(app["category"])
    adorn = "=" * max(len(label), 3)

    lines: list[str] = [
        f".. _{anchor}:",
        "",
        adorn,
        label,
        adorn,
        "",
        "TODO: Add a short description of this app.",
        "",
        "**Open a file**",
        "",
        f'Navigate to the Snooz menu **"{folder}" → "{label}"**, and click on "Open File".',
        "",
        "**Usage**",
        "",
        "TODO: Describe the main workflow for this app.",
        "",
        "Version History",
        "-----------------",
        "",
        f"* v{app['version']} : Distributed with CEAMS package version {app['package_version']}",
        "    - Initial release of the app.",
        "",
    ]

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"  [NEW]     {path.relative_to(OUTPUT_BASE)}")


def ensure_toctree_entry(app: dict, path: Path) -> bool:
    """Append the page basename to the category index toctree if missing."""
    folder = category_folder(app["category"])
    index_path = OUTPUT_BASE / folder / f"{folder}.rst"
    if not index_path.exists():
        print(f"  [WARN]    Missing category index: {index_path.relative_to(OUTPUT_BASE)}")
        return False

    entry = path.stem
    text = index_path.read_text(encoding="utf-8-sig")
    if re.search(rf"(?m)^\s*{re.escape(entry)}\s*$", text):
        return False

    lines = text.splitlines()
    toctree_idx = next((i for i, line in enumerate(lines) if line.strip().startswith(".. toctree::")), None)
    if toctree_idx is None:
        print(f"  [WARN]    No toctree in {index_path.relative_to(OUTPUT_BASE)}")
        return False

    i = toctree_idx + 1
    while i < len(lines) and (lines[i].strip().startswith(":") or not lines[i].strip()):
        i += 1
    last_entry = i - 1
    while i < len(lines) and lines[i].strip():
        last_entry = i
        i += 1

    lines.insert(last_entry + 1, f"    {entry}")
    index_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"  [TOC]     Added {entry} to {folder}/{folder}.rst")
    return True


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    if not (CEAMS_BASE / "CEAMSApps.json").exists():
        raise SystemExit(
            f"CEAMSApps.json not found at:\n  {CEAMS_BASE / 'CEAMSApps.json'}\n"
            "Expected snooz-package-ceams as a sibling of SnoozDoc."
        )

    apps = read_json()
    by_name = index_existing_by_app_name()

    print(f"Found {len(apps)} apps in CEAMSApps.json.\n")

    new_count = 0
    toc_count = 0
    existing_count = 0

    for app in apps:
        path = rst_path(app, by_name)
        if path.exists():
            existing_count += 1
            continue

        create_skeleton_rst(app, path)
        new_count += 1
        if ensure_toctree_entry(app, path):
            toc_count += 1

    print()
    print("Done.")
    print(f"  {existing_count} existing page(s) left unchanged.")
    if new_count:
        print(f"  {new_count} new skeleton(s) created.")
    else:
        print("  No new apps found.")
    if toc_count:
        print(f"  {toc_count} category toctree(s) updated.")


if __name__ == "__main__":
    main()
