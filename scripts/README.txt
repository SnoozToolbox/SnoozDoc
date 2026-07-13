Two scripts were created to keep the documentation synchronized with the source code.

1. generate_module_docs.py:
    Run this script to:
    1. Update the version and category of each module after applying your modifications.
    2. Create a raw documentation entry for your newly added module in modules.rst and in the corresponding table.

2. sync_module_descriptions.py:
    Run this script to:
    1. Sync module descriptions from modules.rst to category index files.

To run these scripts, first open generate_module_docs.py and modify these paths:
    CEAMS_BASE = Path(r"E:\CEAMS\snooz_workspace\snooz-package-ceams\modules\CEAMSModules")
    OUTPUT_BASE = Path(r"E:\CEAMS\snooz_workspace\SnoozDoc\dev_guide\modules")

Then run the script in the terminal:
python .\generate_module_docs.py

Afterward, open sync_module_descriptions.py and edit this path:
    MODULES_RST = Path(r"E:\CEAMS\snooz_workspace\SnoozDoc\dev_guide\modules\modules.rst")

Then run the script in the terminal:
python .\sync_module_descriptions.py


