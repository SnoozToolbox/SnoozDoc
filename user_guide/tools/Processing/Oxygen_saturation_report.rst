.. _Oxygen_saturation_report:

=========================
Oxygen Saturation Report
=========================

Description
-----------------

A tool to analyze the oxygen saturation, detect oxygen desaturations and export :ref:`Oxygen_saturation_report_csv`.
Sleep staging is essential because oxygen saturation is particularly relevant during sleep.

.. warning::

    Invalid sections must be annotated in the accessory file before running this tool.  The :ref:`Oxymeter` viewer can be used to mark the invalid section. 

.. note::

    Optionally, the user can choose to save the oxygen saturation graph for each continuous recording session.

Steps
-----------------

**1 - Input Files**

Start by opening your PSG files (.edf, .eeg or .sts).

* The .tsv file is also needed for the EDF format.

* The .sig file is also needed for Stellate format.

* The whole NATUS subject folder is also needed for the .eeg format.


**2 - Invalid sections**

Invalid sections must be annotated in the accessory file before running this tool.
The user needs to select the annotations to be removed from the oxygen saturation analysis.


**3 - Detection Settings**

The user needs to define the criteria for the oxygen desaturation, including the level drop, maximum duration of the drop, and the minimum time the drop is maintained.


**4 - Output Files**

The Oxygen Saturation Report comprises 2 main categories:

    1. Oxygen saturation variables : minumim, maximum and average oxygen saturation per thirds, halves, sleep cycles and sleep stages.
   
    2. Oxygen desaturation drop variables : oxygen desaturation count, average duration (sec), percentage of sleep time and index (count per sleep hour) for the total sleep time and each sleep stage.
 
These variables are stored in the Oxygen Saturation Report, with one line per recording. Each new recording is appended to the report file.
The user needs to define the file to save the Oxygen Saturation Report.


Report
---------

.. toctree::
   Oxygen_saturation_report/Oxygen_saturation_report_csv

   