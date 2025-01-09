.. _Extract_Annotations:

====================
Extract Annotations
====================

Description
-----------------

To extract (selected) annotations from EDF(.tsv), Natus(.ent) or Stellate(.sts) and write them in a Snooz .tsv file.

.. warning::

    If you extract annotations from a .tsv file, make sure to add a suffix to the output file to avoid overwriting the original .tsv file that includes all the annotations.

Steps
-----------------

**1 - Input Files**

Start by opening your PSG files (.edf, .eeg or .sts). 

- The .tsv file is also needed for the EDF format. 

- The .sig file is also needed for Stellate format. 

- The whole NATUS subject folder is also needed for the .eeg format.

**2 - Select Annotations**

Select the annotations to save in the ouput .tsv file for each PSG recordings. 

.. note::

    You can select multiple files from the PSG Files list to display the annotations for more than one file at a time.

**3 - Output Files**

The extracted annotations are written in the same directory as the input file.  
The output file is named as the input file with the suffix defined by the user.

.. warning::

    The time elapsed is only for debug purpose and is not included in the Snooz accessory format.
    Snooz does not support the time elapsed as part of its accessory file.  
    If you want to use the generated file as accessory file in Snooz, make sure to uncheck the option to add the "Time Elapsed".
