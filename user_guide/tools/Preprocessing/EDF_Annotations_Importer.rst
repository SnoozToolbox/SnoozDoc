.. _EDF_Annotations_Importer: 

=============================
Import EDF Plus Annotations
=============================

Description
-----------------

This tool allows you to import annotations from an EDF+ file (from the signal EDF Annotations) and write them into the Snooz accessory .tsv file.

The PSG signals file is mandatory to determine the start time of the recording, which can differ from the start time of the annotations file. Snooz adjusts the start time of the annotations to match the start time of the PSG signals file. 

Snooz supports a single PSG file with its corresponding Snooz accessory .tsv file. Users can import annotations from multiple EDF+ files for the same PSG signal file. The imported annotations are appended to the end of the Snooz accessory .tsv file.

.. warning::

    If you run this tool more than once on the exact same files, delete the Snooz accessory .tsv file to avoid duplicated annotations.

Steps
-----------------

**1 - Input Files**

Add your EDF+ files to import annotations and thier corresponding PSG signal file (EDF or EDF+). 

.. note::

    The order of the EDF+ annotations files and their corresponding PSG signals file must be the same.
