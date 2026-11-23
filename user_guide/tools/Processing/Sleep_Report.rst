.. _Sleep_Report:

===============================
Report Sleep Variables
===============================

**Sleep Report, Events Sleep Report, and Temporal Links Report**

This tool generates three types of reports:

* **Sleep Report**

   The distribution of sleep stages across sleep cycles, thirds, and halves of the night. It also highlights the transitions between different sleep stages.
   To look at the report variables and their definitions, see : :ref:`sleep_report_info_csv`  


* **Events Sleep Report**

    A breakdown of selected events based on the report criteria, categorized by sleep stage, cycle, and thirds and halves of the night.  
    Predefined report criteria included in Snooz: Arousals Report, Bruxism Report, four PLM reports, Respiratory Events Report, Snoring report and events reports without criteria.
    To look at the report variables and their definitions, see : :ref:`event_report_info_csv`  

* **Temporal Links Report**: 

   The events of two events reports that occur together: one event starts within the analysis window (0.5 s by default) after the start or the end of the other, or the two events overlap. For example, arousals that start just after the end of respiratory events.
   To look at the report variables and their definitions, see : :ref:`temporal_links_report_info_csv`  


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

**2 - Events Report**

The annotations included in your accessory files are listed in order to allow you to select groups of events or directly names of events. 

.. note::

   It is also possible to "Combine events" to create a new group of events.
	
An events report must be added to an event group or name
   
The scrolling menu lists the predefined events report : 

* Arousals Report
* Bruxism Report
* PLMS Report-sleep only
* PLM Total Report-recording time
* PLM Report-awake in sleep period
* PLM Report-before sleep onset
* Respiratory Events Report
* Snoring report
* Events report without criteria-sleep only
* Events report without criteria-EOG_Phasic
* Events report without criteria-EOG_Tonic
		
The selection Criteria window details the criteria defined for the selected report. 

.. note::

   You can also create a new report with your criteria.

.. note::

   By default, only the events reports are generated, but it is possible to generate the list of events included in each report.

	
**3 - Temporal Links**

Check the pairs of events reports to link, among the events reports added in step 2. The events of the 1st report are called events 1, and the events of the 2nd report events 2.

The analysis window (0.5 s by default) is the maximum delay between the start or the end of an event and the start of the linked event. Two events are linked when:

* **After a start**: one event starts within the analysis window after the start of the other.
* **After an end**: one event starts within the analysis window after the end of the other.
* **Overlap**: the two events overlap in time (the analysis window is not used).

For each case, in both orders (events 1 then events 2, and events 2 then events 1), the report gives the number of links, the index per hour and the percentage of events 1 and events 2 linked, plus the mean delay (s) after a start or an end. It also counts the events linked in at least one case.

The index per hour uses the total sleep time, or the period of the events reports: the recording time (bruxism, PLM recording time), the time before sleep onset, or the time awake in the sleep period.

.. warning::

   Make sure the "Temporal links reports (.tsv)" option is checked to generate the temporal links reports.
	
**4 - Generate Reports**

The "Sleep Reports" are .tsv files.  Each row corresponds to a PSG recording and each column to a variable.

Each variable is defined in the _info.tsv file generated with the report, see pages below:


Report
-----------------

.. toctree::
   Sleep_Report/sleep_report_info_csv
   Sleep_Report/event_report_info_csv
   Sleep_Report/temporal_links_report_info_csv


Version History
-----------------

* v2.1.0 : Distributed with CEAMS package version 7.2.0 — Snooz beta 2.0.1
    - Initial release of the tool.

* v2.6.0 : Distributed with CEAMS package version 7.3.0 — Snooz beta 3.0.0
    - Removed the unused variable total_sleep_percent from the sleep report.
    - Added time_in_bed_min (TIB): total time between lights-off and lights-on.
    - Added sleep_period_min (SPT): duration between sleep onset and the last scored sleep stage (N1, N2, N3, R).
    - Updated the definition of sleep_efficiency: time spent in sleep stages over TIB x 100.
    - Added sleep_maintenance_efficiency: time spent in sleep stages over SPT x 100.
    - Improved path, filename, and extension handling for sleep cycle warning log file.
    - Fixed Subject Info synchronization between the UI and sleep report output.

* v2.9.1 : Distributed with CEAMS package version 7.5.0 — Snooz Toolbox 1.1.0
    - Added new events report without criteria-EOG_phasic and without criteria-EOG_tonic.
    - Ensured the multilingual PSG header reader uses UTF-8 encoding to generate valid UTF-8 reports.
    - Fixed an issue where the sex value in the UI did not match the exported report.
    - Added `id1` and `id2` fields to event and temporal link reports.
    - Fixed event list filename generation when using filtered selection groups and names.
    - Fixed cleanup of the temporal link model in the UI.
    - Updated the forms to the new look of Snooz Toolbox 1.1.0 (Inter font, light and dark themes).

* v2.9.2 : Distributed with CEAMS package version 7.6.0 — Snooz Toolbox 1.2.0
    - Redesigned the pages and the step descriptions of the tool, including the Sleep Cycles page shared with other tools.
    - Corrected the introduction: the report filenames start with the prefix (not a suffix), and the list of the predefined events reports.
    - Clarified the definition of the temporal links in the introduction and in the Temporal Links step.