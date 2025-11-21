.. _Extract_Annotations:

==========================
Extract Snooz Annotations 
==========================

Description
-----------------

To extract (selected) annotations from EDF(.tsv), Stellate(.sts) or (for CEAMS users) Natus(.ent) and write them in a Snooz .tsv file.

.. warning::

    If you extract annotations from a .tsv file, make sure to add a suffix to the output file to avoid overwriting the original .tsv file that includes all the annotations.

Steps
-----------------

**1 - Input Files**

PSG files including header and events are needed. Start by opening your PSG files (.edf, .sts or .eeg). 

- **European Data Format (EDF)** : 
  
  The corresponding .tsv file is required with the .edf. Both files must be saved in the same directory and share the exact same filename.

- **Stellate format (up to version 6.2)** : 
  
  The corresponding .sig file is required with the .sts. Both files must be saved in the same directory and share the exact same filename.

- **NATUS format (version 9.1)** : 
  
  (*CEAMS users only*) The entire NATUS subject folder is required.

For more details on accepted formats, see :ref:`accepted_format`.

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
