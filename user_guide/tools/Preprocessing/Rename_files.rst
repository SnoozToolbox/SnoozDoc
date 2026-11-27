.. _Rename_files: 

===================
Rename files
===================

Rename a list of files based on user-defined renaming rules.  A common use case is renaming accessory files to ensure they match the corresponding PSG recording.

.. note::

    In many tools included in Snooz, users add the PSG files, and Snooz automatically searches for an accessory file within the same folder that shares the same filename.

Steps
-----------------

**1 - Input Files**

Choose the files to rename. Any kind of file can be renamed, for example accessory files (.tsv) or text files (.txt). Choosing files again replaces the list.

Define the renaming rules. Snooz applies them to the name of each file, without its extension, in this order, then puts the extension back:

    - **Pattern to remove**: every occurrence of the pattern is removed from the name (e.g., remove "_annotations" to rename "subject01_annotations.txt" as "subject01.txt").
    - **Characters to keep**: only the first characters of the name are kept. Check "All" to keep the whole name.
    - **Prefix**: added at the start of the name (e.g., "visit1-" to rename "subject01.tsv" to "visit1-subject01.tsv").
    - **Suffix**: added at the end of the name (e.g., "-visit1" to rename "subject01.tsv" to "subject01-visit1.tsv").

For example, ``subject01_annotations_v2.tsv`` with the pattern ``_annotations``, 9 characters to keep and the prefix ``visit1_`` becomes ``visit1_subject01.tsv``.

**File extension** selects the files of the list to rename: only the files with this extension are renamed. Leave it empty to rename all the files.

**Keep the original file**: when checked, each file is copied under its new name and the original file stays. When unchecked, each file is renamed.

Output Files :

    The new files are written in the same folder as the original files. Each file copied or renamed is listed in the log.

.. warning::

    Check that no file in the folder already has one of the new names, and that two files of the list do not get the same new name (for example with too few characters to keep). Such a file can be replaced.


Version History
-----------------

* v2.0.0 : Distributed with CEAMS package version 7.2.0 — Snooz beta 2.0.1
    - Initial release of the tool.

* v2.1.0 : Distributed with CEAMS package version 7.3.0 — Snooz beta 3.0.0
    - Fixed workspace loading to properly display files to rename.

* v2.1.1 : Distributed with CEAMS package version 7.5.0 — Snooz Toolbox 1.1.0
    - Updated the forms to the new look of Snooz Toolbox 1.1.0 (Inter font, light and dark themes).

* v2.1.2 : Distributed with CEAMS package version 7.6.0 — Snooz Toolbox 1.2.0
    - Redesigned the pages and the step description of the tool.
    - Corrected the description of "Keep the original file": when unchecked, the file is renamed, not overwritten.
