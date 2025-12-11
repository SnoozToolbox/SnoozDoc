.. _Spindle_detection_A7:

===============================
Detect Spindles with A7
===============================

A spindle is "a train of distinct waves with frequency 11-16 Hz (most commonly 12-14 Hz) with a duration ≥0.5 s, usually maximal in amplitude using central derivations" [1]

This tool allows for the detection of spindles in specific sleep stages using the algorithms from (Lacourse et al. 2019) [2].

The algorithm computes the absolute power (mean square) in the sigma band, the relative sigma power based on the power spectral density (PSD), and the covariance and correlation between the sigma-filtered and unfiltered EEG signals over sliding windows (0.3 s length with a 0.1 s step). 
It then detects a spindle if the 4 features extracted from EEG exceed their respective threshold (1.25 μV2, 1.6 x STD, 1.3 x STD and 69%).

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

      See :ref:`spindle_A7_cohort_info_csv` for the variable definition. 

Filtering Information
---------------------------

Before spindle detection, the EEG signal is band-pass filtered to 0.3-30 Hz (10th order, but halved before the forward/backward pass) and downsampled to 100 Hz as preprocessing steps.
During feature extraction, the EEG signal is further band-pass filtered in the sigma band (default: 11-16 Hz) with a 20th-order filter.

The filters used in both cases are Butterworth designs implemented in second-order sections (SOS) and applied with bidirectional zero-phase filtering.
This approach preserves the desired magnitude response while eliminating phase distortion.

**Bandpass filter parameters:**

- Type: IIR bandpass
- Family: Butterworth
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

.. warning::
   
   Artefacts must be previously detected and saved in the accessory file.

**3 - Detection Settings**

| The user must define the following parameters:
|  **Spindle Duration**: Define the minimum and maximum duration of retained spindles.  
|  **Sleep Stage**: Choose the sleep stage(s) in which to detect spindles.
|  **Sleep Cycle**: Optionally detect spindles only within sleep cycles.
|  **REM Period**: Optionally exclude REM periods from the analysis.

**- A7 Settings**

This configuration page allows you to define a custom frequency band for spindle detection (e.g., a custom sigma band).

By default, the sigma band is defined as **11-16 Hz**.

The features calculated for spindle detection are as follows:
   | **Absolute Sigma Power**: 
   |  log10(mean squared sigma power)
   | **Relative Sigma Power**: 
   |  z-score(log10(PSD: sigma-band Hz / PSD: 4.5-30 Hz))
   | **Sigma Covariance**: 
   |  z-score(log10(cov(EEG: 0.3-30 Hz, EEG: sigma-band Hz)))
   | **Sigma Correlation**:  
   |  cov(EEG: 0.3-30 Hz, EEG: sigma-band Hz) / (std(EEG: 0.3-30 Hz) * std(EEG: sigma-band Hz))

.. warning::
   
   The spindle detection thresholds are preset and validated specifically for the sigma frequency band of 11-16 Hz.
   If you change the frequency band from these default values, you must define new thresholds to ensure accurate spindle detection.

**4 - Output Files**

Select which reports to generate.


Report
-----------------

.. toctree::
   Spindle_detector_A7/spindle_A7_cohort_info_csv
      

References
-----------------

[1] Iber, C., American Academy of Sleep Medicine, 2007. The AASM Manual for the Scoring of Sleep and Associated Events: Rules, Terminology and Technical Specifications. American Academy of Sleep Medicine. 

[2] Lacourse, K., Delfrate, J., Beaudry, J., Peppard, P., Warby, S.C., 2019. A sleep spindle detection algorithm that emulates human expert spindle scoring. Journal of Neuroscience Methods 316, 3–11. https://doi.org/10.1016/j.jneumeth.2018.08.014


Version History
-----------------

* v2.1.0 : Distributed with CEAMS package version 7.2.0 — Snooz beta 2.0.1
    - Initial release of the tool.

* v3.2.0 : Distributed with CEAMS package version 7.3.0 — Snooz beta 2.1.0 
    - Supports a user defined sigma band.
    - Refactored the output report to distinguish between elapsed clock time and sleep-stage time. 
    - Added new variables representing the combined N2 + N3 stages.
    - Events are discarded during non-specific channel artifacts.
