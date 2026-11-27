"""
generate_tool_docs.py
=====================
Creates missing tool documentation pages from CEAMSTools.json.

Run from the SnoozDoc repo:
    python scripts/generate_tool_docs.py

What it does
------------
1. Reads CEAMSTools.json for the current tool list.
2. For every tool that already has a .rst page: does nothing.
3. For every NEW tool (no .rst yet):
   - Creates a skeleton .rst with TODOs and step placeholders from the tool JSON.
   - Appends the page to the category toctree (Preprocessing / Processing /
     Postprocessing).
"""

from __future__ import annotations

import json
import re
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
SNOOZDOC_ROOT = SCRIPT_DIR.parent
WORKSPACE_ROOT = SNOOZDOC_ROOT.parent

CEAMS_BASE = WORKSPACE_ROOT / "snooz-package-ceams" / "tools" / "CEAMSTools"
OUTPUT_BASE = SNOOZDOC_ROOT / "user_guide" / "tools"

# Historical doc filenames that do not match item_name.
# New tools fall back to ``{Category}/{item_name}.rst``.
DOC_FILE_MAP: dict[str, str] = {
    "ConvertDOMINO": "Preprocessing/DominoScreen_Converter.rst",
    "ConvertEDFbrowser": "Preprocessing/EDFbrowser_Converter.rst",
    "ConvertXMLCompumedics": "Preprocessing/XML_Converter.rst",
    "DetectArtifacts": "Preprocessing/Artifact_Detection.rst",
    "DetectREMsYASA": "Preprocessing/DetectREMsYASA.rst",
    "EditAnnotations": "Preprocessing/Annotations_Editor.rst",
    "EditPathsInSnoozWorkspace": "Preprocessing/EditPathsInSnoozWorkspace.rst",
    "ExtractAnnotation": "Preprocessing/Extract_Annotations.rst",
    "ImportEDFPlusAnnotations": "Preprocessing/EDF_Annotations_Importer.rst",
    "ImportTextAnnotations": "Preprocessing/Import_Annotations_from_Text.rst",
    "ImportSleepStagesVector": "Preprocessing/Sleep_Stages_Importer.rst",
    "RenameFiles": "Preprocessing/Rename_files.rst",
    "ScoreSleepStagesYASA": "Preprocessing/YASA_Automatic_Sleep_Scoring.rst",
    "ValidateSnoozTSVFile": "Preprocessing/ValidateSnoozTSVFile.rst",
    "AnalyzeEEGConnectivity": "Processing/Analyze_EEG_connectivity.rst",
    "PowerSpectralAnalysis": "Processing/Power_Spectral_Analysis.rst",
    "SlowWaveDetection": "Processing/Slow_wave_detection.rst",
    "SpindleDetectionA7": "Processing/Spindle_detection_A7.rst",
    "SpindleDetectionMartin": "Processing/Spindle_detection_Martin.rst",
    "SpindleDetectionSumo": "Processing/Spindle_detection_SUMO.rst",
    "OxygenSaturationReport": "Processing/Oxygen_saturation_report.rst",
    "SleepBouts": "Processing/Sleep_Bouts.rst",
    "SleepCycleExport": "Processing/Sleep_cycles_export.rst",
    "SleepReport": "Processing/Sleep_Report.rst",
    "SlowWaveClassification": "Postprocessing/Slow_wave_classifier.rst",
    "CompareEventsFromPSG": "Postprocessing/Compare_PSG_events.rst",
    "PSACohortReview": "Postprocessing/PSA_Cohort_Review.rst",
    "DetectionsCohortReview": "Postprocessing/Detections_Cohort_Review.rst",
    "PSAImages": "Postprocessing/Visualize_EEG_Spectral_Power.rst",
    "SlowWaveImages": "Postprocessing/Slow_Wave_Images_Generator.rst",
}

TOOL_NAME_RE = re.compile(r"\*\*Tool name:\*\*\s+``([^`]+)``")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def category_folder(menu_category: str) -> str:
    """'1-Preprocessing' -> 'Preprocessing'."""
    return re.sub(r"^\d+-", "", menu_category).strip()


def read_json() -> list[dict]:
    """Return list of tool dicts from CEAMSTools.json."""
    data = json.loads((CEAMS_BASE / "CEAMSTools.json").read_text(encoding="utf-8"))
    package_version = data.get("package_version", "")
    tools: list[dict] = []
    for item in data["items"]:
        if item.get("item_type") != "tool":
            continue
        hooks = item["item_hooks"][0]["parameters"]
        tools.append({
            "name": item["item_name"],
            "label": hooks["menu_label"],
            "category": hooks["menu_category"],
            "version": item["item_version"],
            "package_version": package_version,
        })
    return tools


def read_tool_steps(tool: dict) -> list[str]:
    """Return step display names from the tool's own JSON, if available."""
    tool_json = CEAMS_BASE / tool["name"] / f"{tool['name']}.json"
    if not tool_json.exists():
        return []
    data = json.loads(tool_json.read_text(encoding="utf-8"))
    steps = data.get("tool_params", {}).get("steps", [])
    names: list[str] = []
    for step in steps:
        name = (step.get("name") or "").strip()
        if name and name.lower() not in {"introduction", "intro"}:
            names.append(name)
    return names


def index_existing_by_tool_name() -> dict[str, Path]:
    """Scan docs for pages that already declare **Tool name:** ``X``."""
    found: dict[str, Path] = {}
    if not OUTPUT_BASE.exists():
        return found
    skip = {"tools.rst", "Preprocessing.rst", "Processing.rst", "Postprocessing.rst"}
    for path in OUTPUT_BASE.rglob("*.rst"):
        if path.name in skip:
            continue
        match = TOOL_NAME_RE.search(path.read_text(encoding="utf-8-sig", errors="replace"))
        if match:
            found[match.group(1)] = path
    return found


def rst_path(tool: dict, by_name: dict[str, Path]) -> Path:
    """Resolve the .rst path for a tool (existing mapping or default)."""
    if tool["name"] in DOC_FILE_MAP:
        return OUTPUT_BASE / DOC_FILE_MAP[tool["name"]]
    if tool["name"] in by_name:
        return by_name[tool["name"]]
    folder = category_folder(tool["category"])
    return OUTPUT_BASE / folder / f"{tool['name']}.rst"


# ---------------------------------------------------------------------------
# Create pages
# ---------------------------------------------------------------------------

def create_skeleton_rst(tool: dict, path: Path) -> None:
    """Write a new tool page matching the style of existing tool docs."""
    label = tool["label"]
    anchor = path.stem
    steps = read_tool_steps(tool)
    adorn = "=" * max(len(label), 3)

    lines: list[str] = [
        f".. _{anchor}:",
        "",
        adorn,
        label,
        adorn,
        "",
        "TODO: Add a short description of this tool.",
        "",
        "Steps",
        "-----------------",
        "",
    ]

    if steps:
        for i, step_name in enumerate(steps, start=1):
            lines += [
                f"**{i} - {step_name}**",
                "",
                "TODO: Describe this step.",
                "",
            ]
    else:
        lines += [
            "**1 - Input Files**",
            "",
            "TODO: Describe how to select input files.",
            "",
            "**2 - Settings**",
            "",
            "TODO: Describe the main settings for this tool.",
            "",
        ]

    lines += [
        "Version History",
        "-----------------",
        "",
        f"* v{tool['version']} : Distributed with CEAMS package version {tool['package_version']}",
        "    - Initial release of the tool.",
        "",
    ]

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"  [NEW]     {path.relative_to(OUTPUT_BASE)}")


def ensure_toctree_entry(tool: dict, path: Path) -> bool:
    """Append the page basename to the category index toctree if missing."""
    folder = category_folder(tool["category"])
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
    if not (CEAMS_BASE / "CEAMSTools.json").exists():
        raise SystemExit(
            f"CEAMSTools.json not found at:\n  {CEAMS_BASE / 'CEAMSTools.json'}\n"
            "Expected snooz-package-ceams as a sibling of SnoozDoc."
        )

    tools = read_json()
    by_name = index_existing_by_tool_name()

    print(f"Found {len(tools)} tools in CEAMSTools.json.\n")

    new_count = 0
    toc_count = 0
    existing_count = 0

    for tool in tools:
        path = rst_path(tool, by_name)
        if path.exists():
            existing_count += 1
            continue

        create_skeleton_rst(tool, path)
        new_count += 1
        if ensure_toctree_entry(tool, path):
            toc_count += 1

    print()
    print("Done.")
    print(f"  {existing_count} existing page(s) left unchanged.")
    if new_count:
        print(f"  {new_count} new skeleton(s) created.")
    else:
        print("  No new tools found.")
    if toc_count:
        print(f"  {toc_count} category toctree(s) updated.")


if __name__ == "__main__":
    main()
