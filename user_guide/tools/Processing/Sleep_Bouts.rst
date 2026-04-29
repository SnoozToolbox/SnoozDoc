.. _Sleep_Bouts:

===============================
Report Sleep Bouts
===============================

This tool reports statistics about Sleep bouts from Polysomnography (PSG) files.

Sleep bouts are defined as continuous periods of three sleep stage combinations : 

   1. Continuous period of N2 and N3 stages
   2. Continuous period of N2, N3 and REM stages
   3. Continuous period of REM stage alone

To see the complete list of variables included in the report, see :ref:`Sleep_bouts_report_csv`.

Steps
-----------------

| **Common settings** 
| Define the sleep cycles criteria for your study. 
| For more information, see :ref:`Sleep_Cycles_definition`.

**1 - Input Files**

Start by opening your PSG files (.edf, .sts or .eeg). 

- **European Data Format (EDF)** : 
  
  The corresponding .tsv file is required with .edf. Both files must be saved in the same directory and share the exact same filename.

- **Stellate format (up to version 6.2)** : 
  
  The corresponding .sig file is required with the .sts. Both files must be saved in the same directory and share the exact same filename.

- **NATUS format (version 9.1)** : 
  
  (*CEAMS users only*) The entire NATUS subject folder is required.

For more details on accepted formats, see :ref:`accepted_format`.

**2 - Output Files**
    
The output is a TSV (Tab Separated Values) file containing one row per recording, including the ten longest sleep bouts, 
as well as the mean and standard deviation of both the ten longest and all sleep bouts for each combination listed above.

See :ref:`Sleep_bouts_report_csv` for the variable definition. 

Report
---------

.. toctree::
   Report_Sleep_Bouts/Sleep_bouts_report_csv


Version History
-----------------

* v2.1.0 : Distributed with CEAMS package version 7.2.0 — Snooz beta 2.0.1
    - Initial release of the tool.

* v2.2.0 : Distributed with CEAMS package version 7.3.0 — Snooz beta 3.0.0
    - UI improvements for consistent tool and input file descriptions.