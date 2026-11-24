.. _DetectREMsYASA:

===============================
Detect REM events with YASA
===============================

This tool utilizes the Yet Another Spindle Algorithm (YASA) rapid eye movements (REMs) detector algorithm. It also classifies the detected REMs into phasic and tonic mini-epochs.

Algorithm Details
------------------

This algorithm uses the idea from the methodologies proposed in [1] and [2], primarily building upon Agarwal’s [2] approach, which applies amplitude thresholding to the negative product of the LOC and ROC filtered signals.
Using this technique, the algorithm identifies signal peaks and extracts key features, including the duration of the REM period, the peak absolute values of ROC and LOC, as well as the absolute rise and fall slopes for both signals.

If the user selects the "Remove outliers" option (Detector Step), the outliers are detected with an Isolation Forest (scikit-learn) and removed from the detected REMs. This step is only applied when at least 50 REMs are detected.

.. note:: With the sleep stages (Scored, in Detector Step), a REM event is retained when the epoch at one third of its duration from its start, or at one third of its duration from its end, is scored REM sleep (R). Other events are discarded. (This rule is important when a REM event is detected at the transition of two sleep stages.)

**- Usage points:**
   - All output parameters of this algorithm are computed using the filtered LOC and ROC signals. The filtering process is based on the REM frequency band defined in the Detector Step.
   - For optimal results, the user should apply this detection only to artifact-free REM sleep data.


The example of the REMs events in two EOG channels left and right are shown in **Figure 1**.

.. image:: ./DetectREMsYASA/Eyes_movement.png
   :width: 700
   :alt: Example of REMs events
   :align: center
.. rst-class:: center-caption


**Figure 1:** The example of REMs events in two EOG channels left and right

Input
-----
PSG files including header and events are needed.

- **European Data Format (EDF)** : 
  
  The corresponding .tsv file is required. Both files must be saved in the same directory and share the exact same filename.

- **Stellate format (up to version 6.2)** : 
  
  The corresponding .sig file is required with the .sts. Both files must be saved in the same directory and share the exact same filename.

- **NATUS format (version 9.1)** : 
  
  (*CEAMS users only*) The entire NATUS subject folder is required.

For more details on accepted formats, see :ref:`accepted_format`.

.. note:: Annotation files are not required for the functionality of this tool. However, if provided, they must include sleep staging. The REMs report is only generated with the sleep stages (Scored, in Detector Step). Without them (Unscored), the tool performs REMs detection solely based on the algorithm's detection criteria, on the whole recording.

.. note:: If you do not have annotation files, we highly recommend using the "Score Sleep Stages with YASA" tool first to generate an annotation file, and then running this tool for more reliable REMs detection.


Channels:
This tool requires the selection of 2 EOG channels per recording for REMs detection.

Detector Step
----------------
In this step the user can set the parameters for the detection of REMs using YASA. The following parameters can be adjusted:
   - **REMs event group**: The group category in the annotation file (default is "REM").
   - **REMs event name**: The name of the event in the annotation file (default is "YASA_REM").
   - **Amplitude**: Minimum and maximum amplitude of the peak of the REM.
   - **Duration**: Minimum and maximum duration of the REM.
   - **REM frequency**: Minimum and maximum frequency of the REM.
   - **Relative prominence**: Scales the minimum prominence threshold as a fraction of minimum amplitude. (e.g., 0.5 means peaks must stand out by at least half of the minimum amplitude).
   - **Remove outliers**: If checked, the algorithm will remove outliers detected by the IsolationForest model. Note that this step will only be applied if at least 50 REMs are detected.
   - **Sleep stages selection**: If "Scored" is selected, the algorithm will only consider the REM sleep (R) epochs for detection, and the REMs report is generated. If "Unscored" is selected, the algorithm detects the REMs on the whole recording, without the sleep stages, and no REMs report is generated.


Mini-epochs Classification Step
--------------------------------
In this step, the user can set the parameters for the classification of REMs into phasic and tonic mini-epochs.

General definition:
   - **Tonic REM**: Corresponds to more stable REM activity with minimal eye movements and lower physiological variability.
   - **Phasic REM**: is characterized by bursts of rapid eye movements, transient muscle activity, and increased neural and autonomic activation. This separation enables more detailed investigation of REM sleep dynamics and related biomarkers.

Mini-epochs classification parameters:
   - **Mini-epoch event group**: The group category in the annotation file (default is "REM").
   - **Phasic/Tonic event name**: The name of the event in the annotation file (default is "EOG_Phasic" and "EOG_Tonic").
   - **Length of mini-epoch**: The duration of the mini-epoch in seconds (default is 3 seconds).


Output
------
The REMs detected events and the phasic and tonic mini-epochs are added in the annotations files (.tsv, .sts or .ent) depending of the format used.
If the annotations file already includes events with the same group and name as the events to be added, the existing entries will be removed before adding the new ones.

Each event is defined by : 
   1. group : The group where the events are added (i.e. REM).
   2. name : The name of the event (i.e. YASA_REM)
   3. start_sec : The onset of the event in second. 
   4. duration_sec : The duration of the event in second.
   5. channels : The list of channels on which the event occurs.

The tool also provides two folders of **REMs characteristics** (rems_characteristics) and **REMs sleep stages** (rems_sleep_stages), saved in the folder of the cohort report, including some parameters for each specific REM event for more detailed analysis. 

The **characteristics folder** includes two files:
   - **Event file** : Contains all events in Snooz annotation format.
   - **Summary file** : contains the following characteristics of the REMs:
      - LOC and ROC absolute amplitude at REM peak (in uV)
      - LOC and ROC absolute rise and fall slopes (in uV/s)
      - Start, end, duration, and peak of each REM event (in seconds)

Report
----------------
.. toctree::
   DetectREMsYASA/REMs_Per-event_Report_info
   DetectREMsYASA/REMs_Per-subject_Report_info


References
----------
[1] Yetton, B. D., et al. (2016). Automatic detection of rapid eye movements (REMs):A machine learning approach. Journal of neuroscience methods, 259, 72-82.

[2] Agarwal, R., et al. (2005). Detection of rapid-eye movements in sleep studies. IEEE Transactions on biomedical engineering, 52(8), 1390-1396.

Version History
-----------------

* v2.0.0 : Distributed with CEAMS package version 7.0.0 — Snooz beta 2.0.0
   - Initial release of the tool.

* v3.3.0 : Distributed with CEAMS package version 7.3.0 — Snooz beta 3.0.0
   - Added the REMs report to the tool output.
   - Updated the tool UI to be more user-friendly.
   - Fixed reporting of events starting at sleep stage transitions.
   - Improved path, filename, and extension handling for the sleep cycle warning log file.

* v3.4.0 : Distributed with CEAMS package version 7.4.0 — Snooz 1.0.0
   - Added an error-handling workflow for PSG loading from workspaces and displayed failed files in the UI.
   - Added an error-handling workflow for duplicated sleep stages.

* v3.6.2 : Distributed with CEAMS package version 7.5.0 — Snooz Toolbox 1.1.0
   - Added the mini-epoch classification step to the tool.
   - Added the cohort-level (per-subject) REM activity report to the tool output.
   - Added the per-event characteristics dictionary file for the REM characteristics report.
   - Ensured that the multilingual PSG header reader uses UTF-8 encoding to generate valid UTF-8 reports.
   - Updated the forms to the new look of Snooz Toolbox 1.1.0 (Inter font, light and dark themes).

* v3.6.3 : Distributed with CEAMS package version 7.6.0 — Snooz Toolbox 1.2.0
   - Redesigned the pages and the step descriptions of the tool, including those shared with other tools (Sleep Cycles, Input Files), with a new illustration of the REM events. The references are in APA style, with a DOI link.
   - Corrected the descriptions of the outlier removal (Algorithm's Details) and of the location of the REM characteristics folder, saved next to the cohort report (Output File).
   - Removed the Parameters Description step: the detection criteria are described in the tooltips of Detector Step.
