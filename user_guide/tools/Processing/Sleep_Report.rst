.. _Sleep_Report:

===============================
Sleep Report
===============================

Description
-----------------

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

**Common settings**

	Sleep Cycles : define how the sleep cycles are delimited in your study. The "Minimum criteria" is selected by default. 

**1 - Input Files**

Start by opening your PSG files (.edf, .eeg or .sts).

* The .tsv file is also needed for the EDF format.

* The .sig file is also needed for Stellate format.

* The whole NATUS subject folder is also needed for the .eeg format.

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
   