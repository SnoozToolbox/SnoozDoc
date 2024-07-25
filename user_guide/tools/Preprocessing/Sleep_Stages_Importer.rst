.. _Sleep_Stages_Importer:

======================
Sleep Stages Importer
======================

Description
-----------------

Tool to import sleep stages from a text file (.csv, .tsv, .txt) into the accessory .tsv file for Snooz.

.. warning::

    **File format**  

    PSG files are mandatory, and the only supported format is .edf. The sleep stages file must cover the entire recording, filling gaps with 'Unscored' stages.  One sleep stage per row. The file can include extraneous columns.  Missing stages will be filled with "Unscored" stages at the end to match the recording length.

Steps
-----------------

**1 - Input PSG Files**

Add your PSG files (.edf). 

**2 - Input Stages Files**

Add one sleep stages text file per PSG file from step 1 and define the text file format.

Define the original sleep stage labels from the text file to import to ensure proper renaming for the Snooz format.

.. warning::

    The user will be informed in the log if no sleep stages file is found for a PSG file or if any original label for sleep stages is missing from the renaming table.
	