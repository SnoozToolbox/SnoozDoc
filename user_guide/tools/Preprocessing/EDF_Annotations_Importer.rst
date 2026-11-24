.. _EDF_Annotations_Importer: 

=============================
Import Annotations from EDF+ 
=============================

This tool allows you to import annotations from an EDF+ file (from the signal EDF Annotations) and write them into the Snooz accessory .tsv file.

The PSG signals file is mandatory to determine the start time of the recording, which can differ from the start time of the annotations file. Snooz adjusts the start time of the annotations to match the start time of the PSG signals file. 

Snooz supports a single PSG file with its corresponding Snooz accessory .tsv file. Users can import annotations from multiple EDF+ files for the same PSG signal file. The imported annotations are added to the Snooz accessory .tsv file. The annotations already in the file with the same group and name are replaced, and the imported sleep stages replace the existing sleep stages.

.. warning::

    Running this tool again replaces the annotations with the same group and name in the Snooz accessory .tsv file.

Steps
-----------------

**1 - Input Files**

Add your EDF+ files to import annotations and thier corresponding PSG signal file (EDF or EDF+). 

.. note::

    The order of the EDF+ annotations files and their corresponding PSG signals file must be the same.


Version History
-----------------

* v2.0.0 : Distributed with CEAMS package version 7.2.0 — Snooz beta 2.0.1 (and later)
    - Initial release of the tool.

* v2.1.0 : Distributed with CEAMS package version 7.3.0 — Snooz beta 3.0.0
    - Supports the new optional time elapsed column.

* v2.1.1 : Distributed with CEAMS package version 7.5.0 — Snooz Toolbox 1.1.0
    - Updated the forms to the new look of Snooz Toolbox 1.1.0 (Inter font, light and dark themes).

* v2.1.2 : Distributed with CEAMS package version 7.6.0 — Snooz Toolbox 1.2.0
    - Redesigned the pages and the step descriptions of the tool, including the settings view of the EDF Annotations Reader module.
    - Corrected the introduction: the annotations removed before the import are those with the same group and name, on every channel.
    - Fixed the Input Files Step: cancelling the file dialog emptied the list, and Clear all left empty rows.
