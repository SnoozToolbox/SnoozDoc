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
    Predefined report criteria included in Snooz: Arousals Report, Bruxism Report, PLM Report, Respiratory Events Report, Snoring report.
    To look at the report variables and their definitions, see : :ref:`event_report_info_csv`  

* **Temporal Links Report**: 

   The relationship between two selected events within a specified time window, such as the occurrence of event 1 starting before the start of event 2.
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
* PLM Report
* Respiratory Events Report
* Snoring report
* Events report without criteria
		
The selection Criteria window details the criteria defined for the selected report. 

.. note::

   You can also create a new report with your criteria.

.. note::

   By default, only the events reports are generated, but it is possible to generate the list of events included in each report.

	
**3 - Temporal Links**

The length of the time window defining a possible link between 2 events is 0.5 s by default.

Check all the temporal links you want to generate a report for. The temporal link must be defined between 2 events type.

.. warning::

   Make sure the "tsv report" option is checked to generate the temporal links reports.
	
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

* v2.5.0 : Distributed with CEAMS package version 7.3.0 — Snooz beta 3.0.0
    - Removed the unused variable total_sleep_percent from the sleep report.
    - Added time_in_bed_min (TIB): total time between lights-off and lights-on.
    - Added sleep_period_min (SPT): duration between sleep onset and the last scored sleep stage (N1, N2, N3, R).
    - Updated the definition of sleep_efficiency: time spent in sleep stages over TIB x 100.
    - Added sleep_maintenance_efficiency: time spent in sleep stages over SPT x 100.
    - Improve path, filename, and extension handling for sleep cycle warning log file.