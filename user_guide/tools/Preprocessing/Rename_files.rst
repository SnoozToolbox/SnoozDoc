.. _Rename_files: 

===================
Rename files
===================

Description
-----------------

Rename a list of files based on user-defined renaming rules.  A common use case is renaming accessory files to ensure they match the corresponding PSG recording.

.. note::

    In many tools included in Snooz, users add the PSG files, and Snooz automatically searches for an accessory file within the same folder that shares the same filename.

Steps
-----------------

**1 - Input Files**

Start by selecting the files you want to rename. You can choose multiple files at once, and you can also filter by file extension.

Define the renaming rules : 

    - **File Extension**: Specify the extension of the files to rename. Leave this field empty to rename all selected files.
    - **Characters to Keep**: Indicate the number of characters to retain from the original name. Select "all" to keep the full original name.
    - **Pattern to Remove**: Enter a pattern to remove from the original filename (e.g., remove "_annotations" to rename "subject01_annotations.txt" as "subject01.txt").
    - **Prefix to Add**: Add a prefix to the original filename (e.g., "visit1-" to rename "subject01.tsv" to "visit1-subject01.tsv").
    - **Suffix to Add**: Add a suffix to the original filename (e.g., "-visit1" to rename "subject01.tsv" to "subject01-visit1.tsv").
    - **Keep the Original File**: Check this option to save a copy of the file before renaming it. If unchecked, the original file will be overwritten with the new name.

Output Files : 

    The renamed files will be saved in the same folder as the original files.
