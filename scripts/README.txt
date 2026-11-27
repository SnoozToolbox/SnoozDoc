Four scripts were created to keep the documentation synchronized with the source code.

1. generate_module_docs.py:
    Run this script to:
    1. Update the version and category of each module after applying your modifications.
    2. Create a raw documentation entry for your newly added module in modules.rst and in the corresponding table.

2. sync_module_descriptions.py:
    Run this script to:
    1. Sync module descriptions from modules.rst to category index files.

3. generate_tool_docs.py:
    Run this script to:
    1. Skip tools that already have a .rst page (no metadata updates).
    2. Create a raw .rst skeleton for any tool that has no page yet.
    3. Append new pages to the existing category toctrees.

4. generate_app_docs.py:
    Run this script to:
    1. Skip apps that already have a .rst page under user_guide/tools.
    2. Create a raw .rst skeleton for any app that has no page yet.
    3. Append new pages to the existing category toctrees (apps live under user_guide/tools).

----------------------------------------------------------------------
Paths
----------------------------------------------------------------------
All four scripts resolve paths from the repo layout automatically
(SnoozDoc next to snooz-package-ceams). No hardcoded machine paths:

    <workspace>/SnoozDoc
    <workspace>/snooz-package-ceams

SCRIPT_DIR is Path(__file__).resolve().parent (the scripts/ folder),
SNOOZDOC_ROOT is its parent, and WORKSPACE_ROOT is the parent of that.

----------------------------------------------------------------------
How to run
----------------------------------------------------------------------
From the SnoozDoc/scripts directory:

    python .\generate_module_docs.py
    python .\sync_module_descriptions.py
    python .\generate_tool_docs.py
    python .\generate_app_docs.py

Or from the SnoozDoc root:

    python .\scripts\generate_module_docs.py
    python .\scripts\sync_module_descriptions.py
    python .\scripts\generate_tool_docs.py
    python .\scripts\generate_app_docs.py

Note:
    Tool/app page filenames that do not match item_name are listed in
    DOC_FILE_MAP inside generate_tool_docs.py / generate_app_docs.py.
    Add an entry there if you rename a historical page, or if a new item
    should use a custom filename instead of {item_name}.rst.
