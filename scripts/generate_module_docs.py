"""
generate_module_docs.py
=======================
Keeps SnoozDoc/user_guide/modules in sync with CEAMSModules.json.

Run:
    python scripts/generate_module_docs.py

What it does
------------
1. Reads CEAMSModules.json for the current module list, versions and categories.
2. For every module that already has a .rst file:
   - Updates the **Package:** and **Version:** header lines if they changed.
   - Everything else is left untouched so manual edits are preserved.
3. For every NEW module (no .rst yet):
   - Creates a skeleton .rst pre-filled with plug names and TODO placeholders.
4. Always rebuilds modules.rst and every category index.rst.
   Descriptions shown in the tables come from each module's Overview section.
"""

import json
import re
from collections import defaultdict
from pathlib import Path

CEAMS_BASE = Path(r"E:\CEAMS\snooz_workspace\snooz-package-ceams\modules\CEAMSModules")
OUTPUT_BASE = Path(r"E:\CEAMS\snooz_workspace\SnoozDoc\user_guide\modules")


# ---------------------------------------------------------------------------
# Small helpers
# ---------------------------------------------------------------------------

def slugify(text: str) -> str:
    """'Signal Processing' -> 'Signal_Processing'  (safe for anchors/paths)."""
    return re.sub(r"[^a-zA-Z0-9]+", "_", text).strip("_")


def category_slug(category: str) -> str:
    """'Signal Processing' -> 'signal_processing'  (folder name)."""
    return slugify(category).lower()


def rst_path(module: dict) -> Path:
    """Absolute path where this module's .rst file lives (or will be created)."""
    return OUTPUT_BASE / category_slug(module["category"]) / f"{module['name']}.rst"


# ---------------------------------------------------------------------------
# Read CEAMSModules.json
# ---------------------------------------------------------------------------

def read_json() -> tuple[str, list[dict]]:
    """
    Parse CEAMSModules.json and return (package_version, list_of_module_dicts).
    Each dict has: name, label, category, version, package_version.
    """
    data = json.loads((CEAMS_BASE / "CEAMSModules.json").read_text(encoding="utf-8"))
    package_version = data.get("package_version", "")
    modules = []
    for item in data["items"]:
        if item["item_type"] != "module":
            continue
        hooks = item["item_hooks"][0]["parameters"]
        modules.append({
            "name": item["item_name"],
            "label": hooks["module_label"],
            "category": hooks["module_category"],
            "version": item["item_version"],
            "package_version": package_version,
        })
    return package_version, modules


# ---------------------------------------------------------------------------
# Read InputPlug / OutputPlug names from the .py file
# ---------------------------------------------------------------------------

def read_plugs(module: dict) -> tuple[list[str], list[str]]:
    """
    Scan the module's .py file and return ([input_names], [output_names]).
    Preserves declaration order, skips duplicates.
    """
    py_file = CEAMS_BASE / module["name"] / f"{module['name']}.py"
    if not py_file.exists():
        return [], []
    content = py_file.read_text(encoding="utf-8", errors="replace")

    def extract(pattern: str) -> list[str]:
        seen: set[str] = set()
        result: list[str] = []
        for m in re.finditer(pattern, content):
            name = m.group(1)
            if name not in seen:
                seen.add(name)
                result.append(name)
        return result

    return extract(r"InputPlug\('([^']+)'"), extract(r"OutputPlug\('([^']+)'")


# ---------------------------------------------------------------------------
# Load saved descriptions from the current modules.rst
# ---------------------------------------------------------------------------

def load_saved_descriptions() -> dict[str, str]:
    """
    Parse the 'All modules' list-table in modules.rst and return a dict of
    {module_name: description} for every module that already has an entry.

    The table rows look like:
        * - :ref:`Label <module_modulename>`
          - Category
          - Version
          - Description text here
    """
    modules_rst = OUTPUT_BASE / "modules.rst"
    if not modules_rst.exists():
        return {}

    descriptions: dict[str, str] = {}
    lines = modules_rst.read_text(encoding="utf-8").splitlines()
    i = 0
    while i < len(lines):
        # Detect the start of a data row: a :ref: link line
        ref_match = re.match(r"\s+\*\s+-\s+:ref:`[^<]+<module_(\w+)>`", lines[i])
        if ref_match:
            module_name_lower = ref_match.group(1)   # e.g. "amplitudedetector"
            # The description is 3 lines further down (category, version, description)
            if i + 3 < len(lines):
                desc_line = lines[i + 3].strip()
                if desc_line.startswith("- "):
                    desc_line = desc_line[2:].strip()
                if desc_line:
                    descriptions[module_name_lower] = desc_line
            i += 4
            continue
        i += 1
    return descriptions


def get_description(module: dict, saved: dict[str, str]) -> str:
    """
    Return the description to use for a module in tables.
    Source priority:
      1. Saved description from modules.rst (manually maintained).
      2. Module label (fallback for brand-new modules not yet in modules.rst).
    """
    key = slugify(module["name"]).lower()
    return saved.get(key, module["label"])


# ---------------------------------------------------------------------------
# Create a skeleton .rst for a brand-new module
# ---------------------------------------------------------------------------

def create_skeleton_rst(module: dict) -> None:
    """
    Write a new .rst with structural placeholders.
    The user fills in the Overview description, formats, defaults, etc.
    """
    name = module["name"]
    label = module["label"]
    anchor = f"module_{slugify(name).lower()}"
    inputs, outputs = read_plugs(module)

    lines: list[str] = [
        f".. _{anchor}:",
        "",
        label,
        "=" * len(label),
        "",
        f"**Module name:** ``{name}``",
        "",
        f"**Package:** CEAMSModules {module['package_version']}",
        "",
        f"**Version:** {module['version']}",
        "",
        "Overview",
        "--------",
        "",
        "TODO: Add a short description of this module.",
        "",
        "Inputs",
        "------",
        "",
    ]

    if inputs:
        lines += [
            ".. list-table::",
            "   :widths: 15 20 12 53",
            "   :header-rows: 1",
            "   :align: left",
            "   :class: left-align-caption wrap-table",
            "",
            "   * - Input",
            "     - Format",
            "     - Default",
            "     - Description",
        ]
        for inp in inputs:
            lines += [f"   * - ``{inp}``", "     - —", "     - —", "     - TODO"]
        lines.append("")
    else:
        lines += ["This module has no inputs.", ""]

    lines += ["Outputs", "-------", ""]

    if outputs:
        lines += [
            ".. list-table::",
            "   :widths: 15 20 65",
            "   :header-rows: 1",
            "   :align: left",
            "   :class: left-align-caption wrap-table",
            "",
            "   * - Output",
            "     - Format",
            "     - Description",
        ]
        for out in outputs:
            lines += [f"   * - ``{out}``", "     - —", "     - TODO"]
        lines.append("")
    else:
        lines += ["This module has no outputs.", ""]

    lines += [
        "Usage in a process",
        "------------------",
        "",
        "1. Open **Dev Tools -> New process** in Snooz.",
        f"2. In the Module Library, find **{label}** under the **{module['category']}** category.",
        "3. Drag the module onto the process canvas.",
        "4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).",
        "5. Connect outputs to downstream modules as needed.",
        "6. Double-click the module to configure parameters in the **Settings** tab.",
        "7. Run the process and inspect results in the **Results** tab.",
        "",
        ".. note::",
        "",
        "   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.",
        "",
    ]

    path = rst_path(module)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"  [NEW]     {module['category']}/{name}.rst")


# ---------------------------------------------------------------------------
# Patch the header of an existing .rst (version / package only)
# ---------------------------------------------------------------------------

def patch_rst_header(module: dict) -> bool:
    """
    Replace only the **Package:** and **Version:** lines in an existing .rst.
    Returns True if the file was actually changed.
    """
    path = rst_path(module)
    original = path.read_text(encoding="utf-8")

    updated = re.sub(
        r"\*\*Package:\*\* CEAMSModules [^\n]+",
        f"**Package:** CEAMSModules {module['package_version']}",
        original,
    )
    updated = re.sub(
        r"\*\*Version:\*\* [^\n]+",
        f"**Version:** {module['version']}",
        updated,
    )

    if updated != original:
        path.write_text(updated, encoding="utf-8")
        print(f"  [PATCHED] {module['category']}/{module['name']}.rst  (version/package updated)")
        return True
    return False


# ---------------------------------------------------------------------------
# Rebuild category index.rst  (always regenerated)
# ---------------------------------------------------------------------------

def build_category_rst(category: str, modules: list[dict], saved: dict[str, str]) -> None:
    """Write the index.rst for one category."""
    slug = category_slug(category)
    sorted_modules = sorted(modules, key=lambda m: m["label"].lower())

    lines: list[str] = [
        category,
        "=" * len(category),
        "",
        ".. toctree::",
        "   :maxdepth: 1",
        "",
    ]
    for m in sorted_modules:
        lines.append(f"   {m['name']}")
    lines.append("")

    lines += [
        "Quick reference",
        "---------------",
        "",
        ".. list-table::",
        "   :widths: 25 15 60",
        "   :header-rows: 1",
        "   :align: left",
        "   :class: left-align-caption wrap-table",
        "",
        "   * - Module",
        "     - Version",
        "     - Description",
    ]
    for m in sorted_modules:
        anchor = f"module_{slugify(m['name']).lower()}"
        desc = get_description(m, saved)
        lines += [
            f"   * - :ref:`{m['label']} <{anchor}>`",
            f"     - {m['version']}",
            f"     - {desc}",
        ]
    lines.append("")

    path = OUTPUT_BASE / slug / "index.rst"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


# ---------------------------------------------------------------------------
# Rebuild modules.rst  (always regenerated)
# ---------------------------------------------------------------------------

def build_modules_rst(modules: list[dict], saved: dict[str, str]) -> None:
    """Write the top-level modules.rst (master table of all modules)."""
    by_category: dict[str, list[dict]] = defaultdict(list)
    for m in modules:
        by_category[m["category"]].append(m)

    lines: list[str] = [
        ".. _modules:",
        "",
        "Modules",
        "=======",
        "",
        "This guide documents all the necessary information needed to use the modules "
        "in the **CEAMSModules** package.",
        "Modules are the building blocks of Snooz processes. Each module performs",
        "a specific operation on signals, events, files, or parameters.",
        "",
        "Modules are grouped by category as they appear in the Snooz Module Library.",
        "Select a category below to browse module documentation.",
        "",
        "How to use modules",
        "------------------",
        "",
        "1. In Snooz, go to **Dev Tools -> New process**.",
        "2. Open the **Module Library** and enable the **CEAMSModules** package if needed.",
        "3. Drag modules from a category onto the process canvas.",
        "4. Connect module inputs and outputs to define your analysis pipeline.",
        "5. Configure each module via its **Settings** tab and run the process.",
        "",
        "For a hands-on introduction to processes and modules, "
        "see :doc:`/dev_guide/explore_ex`.",
        "",
        "Categories",
        "----------",
        "",
        ".. toctree::",
        "   :maxdepth: 2",
        "   :caption: Module categories:",
        "",
    ]
    for cat in sorted(by_category.keys()):
        lines.append(f"   {category_slug(cat)}/index")
    lines.append("")

    lines += [
        "All modules",
        "-----------",
        "",
        ".. list-table::",
        "   :widths: 25 20 15 40",
        "   :header-rows: 1",
        "   :align: left",
        "   :class: left-align-caption wrap-table",
        "",
        "   * - Module",
        "     - Category",
        "     - Version",
        "     - Description",
    ]
    for m in sorted(modules, key=lambda x: (x["category"], x["label"].lower())):
        anchor = f"module_{slugify(m['name']).lower()}"
        desc = get_description(m, saved)
        lines += [
            f"   * - :ref:`{m['label']} <{anchor}>`",
            f"     - {m['category']}",
            f"     - {m['version']}",
            f"     - {desc}",
        ]
    lines.append("")

    (OUTPUT_BASE / "modules.rst").write_text("\n".join(lines), encoding="utf-8")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    _package_version, modules = read_json()

    print(f"Found {len(modules)} modules in CEAMSModules.json.\n")

    # Load descriptions saved in the current modules.rst BEFORE rebuilding it.
    # This preserves any manual edits the user has made to that table.
    saved_descriptions = load_saved_descriptions()

    # --- Process each module ---
    new_count = 0
    patched_count = 0
    for module in modules:
        if rst_path(module).exists():
            if patch_rst_header(module):
                patched_count += 1
        else:
            create_skeleton_rst(module)
            new_count += 1

    # --- Rebuild aggregate files ---
    by_category: dict[str, list[dict]] = defaultdict(list)
    for m in modules:
        by_category[m["category"]].append(m)

    for category, cat_modules in by_category.items():
        build_category_rst(category, cat_modules, saved_descriptions)

    build_modules_rst(modules, saved_descriptions)

    # --- Summary ---
    print()
    print("Done.")
    if new_count:
        print(f"  {new_count} new skeleton(s) created.")
    if patched_count:
        print(f"  {patched_count} existing file(s) patched (version/package updated).")
    else:
        print("  No version/package changes detected.")
    print(f"  Rebuilt: modules.rst + {len(by_category)} category index.rst files.")


if __name__ == "__main__":
    main()
