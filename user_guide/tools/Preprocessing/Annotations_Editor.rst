.. _Annotations_Editor: 

========================
Edit Snooz Annotations
========================

This tool allows you to delete or edit annotations in batches. Useful for making annotations across a cohort more concise. 

.. warning::

    At runtime the annotations in the original files will be overwritten if you ask any change via this tool.
    Make a copy of your annotations files (.tsv, .STS or .ent).

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


**2 - Remove or edit annotations**

The annotations included in your cohort are displayed so you can remove or edit them.
Press 'Export' to display all the changes that will be applied at runtime.

.. note::

    Look at the "Annotations Editor" home page for more information.


Version History
-----------------

* v2.1.0 : Distributed with CEAMS package version 7.2.0 — Snooz beta 2.0.1
    - Initial release of the tool.

* v2.2.0 : Distributed with CEAMS package version 7.3.0 — Snooz beta 2.1.0
    - UI improvements for consistent tool and input file descriptions.
