.. _Sleep_Stages_Importer:

===============================
Import Sleep Stage Text Vector
===============================

Tool to import sleep stages from a text file (.csv, .tsv, .txt) into the accessory .tsv file for Snooz.

.. warning::

    **File format**  

    PSG files are mandatory, and the only supported format is .edf. The sleep stages file must cover the entire recording, filling gaps with 'Unscored' stages.  One sleep stage per row. The file can include extraneous columns.  When the file is shorter than the recording, the last epochs keep their stage in the accessory file ("Unscored" when it had none). A file longer than the recording is not imported.

Steps
-----------------

**1 - Input PSG Files**

Add your PSG files (.edf). 

**2 - Input Stages Files**

Add one sleep stages text file per PSG file from step 1 and define the text file format.

Define the original sleep stage labels from the text file to import to ensure proper renaming for the Snooz format.

.. warning::

    The user will be informed in the log if no sleep stages file is found for a PSG file or if any original label for sleep stages is missing from the renaming table.


Version History
-----------------

* v2.1.0 : Distributed with CEAMS package version 7.2.0 — Snooz beta 2.0.1
    - Initial release of the tool.

* v2.3.0 : Distributed with CEAMS package version 7.3.0 — Snooz beta 3.0.0
    - Update UI description for 'number of rows to skip' in text importers.
    - UI improvements for consistent tool and input file descriptions.
    - Improve path, filename, and extension handling.

* v2.3.1 : Distributed with CEAMS package version 7.5.0 — Snooz Toolbox 1.1.0
    - Fixed the "Original Label" text that was cut in the Input Stages Files step.
    - Updated the forms to the new look of Snooz Toolbox 1.1.0 (Inter font, light and dark themes).

* v2.3.2 : Distributed with CEAMS package version 7.6.0 — Snooz Toolbox 1.2.0
    - Redesigned the pages and the step descriptions of the tool, including the settings view of the Sleep Stages Importer module. The list of sleep stages files shows the file names (the whole path in a tooltip).
    - Corrected the introduction: when the file is shorter than the recording, the last epochs keep their stage in the accessory file.
    - Fixed the Input Stages Files step: cancelling the file dialog emptied the list, and Clear all left empty rows.
