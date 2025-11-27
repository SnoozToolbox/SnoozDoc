.. _Spindle_detection_Martin:

===============================
Detect Spindles with Martin
===============================

A spindle is "a train of distinct waves with frequency 11-16 Hz (most commonly 12-14 Hz) with a duration ≥0.5 s, usually maximal in amplitude using central derivations" [1]

This tool allows for the detection of spindles in specific sleep stages using the algorithms from Martin et al. (2013) [2].

The single parameter of the algorithm, "the percentile threshold," is editable, with the default value set to 95.

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

      See :ref:`spindle_Martin_cohort_info_csv` for the variable definition. 

Filtering Information
---------------------------

During feature extraction, the EEG signal is band-pass filtered in the sigma band (11.1-14.9 Hz; 30th order).
The filter is a Butterworth design implemented in second-order sections (SOS) and applied using bidirectional zero-phase filtering.
This approach preserves the desired magnitude response while eliminating phase distortion.

**Bandpass filter parameters:**

- Type: IIR bandpass
- Family: Butterworth
- Frequency band: 11.1-14.9 Hz
- Order: 30 (internally halved before the forward and backward passes)
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

**4 - Output Files**

Select which reports to generate.

Report
-----------------

.. toctree::
   Spindle_detector_Martin/spindle_Martin_cohort_info_csv
      
References
-----------------

   [1] Iber, C., American Academy of Sleep Medicine, 2007. The AASM Manual for the Scoring of Sleep and Associated Events: Rules, Terminology and Technical Specifications. American Academy of Sleep Medicine. 

   [2] N. Martin et al., “Topography of age-related changes in sleep spindles,” Neurobiol. Aging, vol. 34, no. 2, pp. 468-476, Feb. 2013, doi: 10.1016/j.neurobiolaging.2012.05.020. 

