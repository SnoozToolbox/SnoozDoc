"""Sync module descriptions from modules.rst to category index files."""
import re
from pathlib import Path

MODULES_RST = Path(r"E:\CEAMS\snooz_workspace\SnoozDoc\user_guide\modules\modules.rst")
MODULES_DIR = MODULES_RST.parent

CATEGORY_DIRS = {
    "Connectivity Analysis": "connectivity_analysis",
    "Detectors": "detectors",
    "Events Analysis": "events_analysis",
    "Events Utilities": "events_utilities",
    "Files I/O": "files_i_o",
    "Hypnogram Analysis": "hypnogram_analysis",
    "Parameters": "parameters",
    "Signal Processing": "signal_processing",
    "Statistics": "statistics",
}


def parse_modules_rst(text: str) -> dict[str, dict]:
    """Parse anchor -> {label, category, version, description} from modules.rst table."""
    modules = {}
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        ref_match = re.match(
            r"\s*\*\s+-\s+:ref:`([^<]+)\s*<([^>]+)>`", lines[i]
        )
        if ref_match and i + 3 < len(lines):
            label = ref_match.group(1).strip()
            anchor = ref_match.group(2).strip()
            category = lines[i + 1].strip().removeprefix("- ").strip()
            version = lines[i + 2].strip().removeprefix("- ").strip()
            description = lines[i + 3].strip().removeprefix("- ").strip()
            modules[anchor] = {
                "label": label,
                "category": category,
                "version": version,
                "description": description,
            }
            i += 4
            continue
        i += 1
    return modules


def update_category_index(index_path: Path, category: str, modules: dict[str, dict]) -> bool:
    text = index_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    out = []
    changed = False
    i = 0
    while i < len(lines):
        ref_match = re.match(
            r"(\s*\*\s+-\s+:ref:`([^<]+)\s*<([^>]+)>`)", lines[i]
        )
        if ref_match and i + 2 < len(lines):
            anchor = ref_match.group(3).strip()
            out.append(lines[i])
            out.append(lines[i + 1])
            if anchor in modules:
                new_desc = modules[anchor]["description"]
                old_desc = lines[i + 2].strip().removeprefix("- ").strip()
                out.append(f"     - {new_desc}")
                if old_desc != new_desc:
                    changed = True
            else:
                out.append(lines[i + 2])
            i += 3
            continue
        out.append(lines[i])
        i += 1

    if changed:
        index_path.write_text("\n".join(out) + "\n", encoding="utf-8")
    return changed


def main():
    modules_text = MODULES_RST.read_text(encoding="utf-8")
    modules = parse_modules_rst(modules_text)
    print(f"Parsed {len(modules)} module descriptions from modules.rst")

    updated = []
    for category, folder in CATEGORY_DIRS.items():
        index_path = MODULES_DIR / folder / "index.rst"
        if not index_path.exists():
            print(f"Missing: {index_path}")
            continue
        if update_category_index(index_path, category, modules):
            updated.append(index_path)
            print(f"Updated: {index_path.relative_to(MODULES_DIR)}")

    if not updated:
        print("All category index files are already in sync.")
    else:
        print(f"Synced {len(updated)} category index file(s).")


if __name__ == "__main__":
    main()
