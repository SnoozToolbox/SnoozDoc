.. _Spindle_detection_SUMO:

===============================
Detect Spindles with SUMO
===============================

A spindle is "a train of distinct waves with frequency 11-16 Hz (most commonly 12-14 Hz) with a duration ≥0.5 s, usually maximal in amplitude using central derivations" [1]

.. This tool allows for the detection of spindles in specific sleep stages using the algorithms from (Kaulen et al. 2022) [2].

This tool detects sleep spindles in specific sleep stages using SUMO (Slim U-Net trained on MODA), a deep learning model inspired by the U-Net architecture (Kaulen et al. 2022) [2]. 
SUMO leverages deep convolutional networks to process minimally preprocessed EEG signals, achieving a higher level of agreement with expert consensus.
By automating the spindle identification process with superior precision, SUMO facilitates large-scale spindle studies while reducing the impact of intra- and inter-rater variability observed in manual scoring.

The spindle events detected are added into the accessory file (.tsv, .STS or .ent).

The event information is :

   * **group** : the group of the event.
   * **name** : the name of the event.
   * **start_sec** : the onset of the event in seconds (time elapsed from the lights off).
   * **duration_sec** : The duration of the event in seconds.
   * **channels** : The list of channels on which the events occurs.

Two additional output reports are available : 
   
   **1. Spindle characteristics by event level**
      Files with the signal characteristic of each spindle event. One file per recording, one row per event.

      The characteristics included are : 

         * Duration (s)
         * Dominent frequency (Hz), where spectral energy is maximum
         * Average frequency (Hz) counting peaks
         * Peak-to-peak amplitude (µV)
         * Root Mean Square (rms) amplitude (µV)

   **2. Spindle characteristics averaged by subject level**
      A file with the spindle characteristics averaged per subject.  One file for the cohort, one row per channel.

      The characteristics included are : 

      * spindle count
      * the average spindle characteristics listed above
         - total (all selected stages)
         - per sleep stage
         - per sleep cycle
         - per clock hour
         - per hour spent in each sleep stage

      See :ref:`spindle_SUMO_cohort_info_csv` for the variable definition. 

Filtering Information
---------------------------

Before spindle detection, the EEG signal is band-pass filtered to 0.3-30 Hz (10th order, but halved before the forward/backward pass) and downsampled to 100 Hz as preprocessing steps.
The filter is a Butterworth designs implemented in second-order sections (SOS) and applied with bidirectional zero-phase filtering.
This approach preserves the desired magnitude response while eliminating phase distortion.

**Bandpass filter parameters:**

- Type: IIR bandpass
- Family: Butterworth
- Frequency band: 0.3-30 Hz
- Order: 10 (internally halved before the forward/backward pass)
- Form: second-order sections (SOS)
- Application: bidirectional zero-phase filtering (filtfilt)

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

**2 - Non valid events**

Select events to disable the spindle detection.

.. note::

   If artefacts have not already been identified and saved in the accessory file, it is recommended to use the :ref:`Artifact_Detection` tool in the *Preprocessing* module before running SUMO for better detection accuracy.  

**3 - Detection Settings**

| The user must define the following parameters:
|  **Spindle Duration**: Define the minimum and maximum duration of retained spindles.  
|  **Sleep Stage**: Choose the sleep stage(s) in which to detect spindles.
|  **Sleep Cycle**: Optionally detect spindles only within sleep cycles.
|  **REM Period**: Optionally exclude REM periods from the analysis.

**4 - Output Files**

   Select which reports to generate.

Report
-----------------

.. toctree::
   Spindle_detector_SUMO/spindle_SUMO_cohort_info_csv
      

References
-----------------

   [1] Iber, C., American Academy of Sleep Medicine, 2007. The AASM Manual for the Scoring of Sleep and Associated Events: Rules, Terminology and Technical Specifications. American Academy of Sleep Medicine. 

   [2] Kaulen, L., Schwabedal, J.T., Schneider, J., Ritter, P. and Bialonski, S., 2022. Advanced sleep spindle identification with neural networks. Scientific reports, 12(1), p.7686. https://doi.org/10.1038/s41598-022-11210-y  


Version History
-----------------

The version history of this tool is as follows:

* v2.0.1 : Distributed with CEAMS package version 7.2.0 - Snooz beta 2.0.1
    - Initial release of the tool.

* v2.5.0 : Distributed with CEAMS package version 7.3.0 - Snooz beta 2.1.0
    - Major update : 
