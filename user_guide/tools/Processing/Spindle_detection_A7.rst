.. _Spindle_detection_A7:

===============================
Spindle Detection (A7)
===============================

Description
-----------------

A spindle is "a train of distinct waves with frequency 11–16 Hz (most commonly 12–14 Hz) with a duration ≥0.5 s, usually maximal in amplitude using central derivations" [1]

This tool allows for the detection of spindles in specific sleep stages using the algorithms from (Lacourse et al. 2019) [2].

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

      See :ref:`spindle_A7_cohort_info_csv` for the variable definition. 

Steps
-----------------

**1 - Input Files**

   Start by opening your PSG files (.edf, .eeg or .sts).

   * The .tsv file is also needed for the EDF format.

   * The .sig file is also needed for Stellate format.

   * The whole NATUS subject folder is also needed for the .eeg format.

**2 - Non valid events**

   Select events to disable the spindle detection.

   .. warning::
      
      Artefacts must be previously detected and saved in the accessory file.

**3 - Spindle Detector**

   - Define the minimum and maximum duration of kept spindles.

   - Define in which sleep stage you want to detect spindles.  

   - You can also choose to detect spindle in the sleep cycles only or to exclude sleep periods from the analysis.

   **- A7 Settings**

      In this section, you can specify a custom frequency range for spindle detection. The algorithm will compute its features based on the range defined here.
      
      By default, the values are set to 11–16 Hz (sigma band), the standard frequency range for spindle detection.
      
      The calculated features for spindle detection are as follows:

      * **Absolute power in specified frequency band**: log10(mean squared band power)

      * **Relative band power**: z-score(log10(PSA: desired frequency band Hz / PSA:4.5-30Hz))

      * **Specified frequency band covariance**: z-score(log10(cov(EEG:0.3-30Hz, EEG: desired frequency band Hz)))

      * **specified frequency band correlation**:  cov(EEG:0.3-30Hz, EEG: desired frequency band Hz) / (std(EEG:0.3-30Hz) * std(EEG:desired frequency band Hz))

   .. warning::
      
      The spindle detection thresholds are pre-set and validated specifically for the sigma frequency band (11-16 Hz). If you change the frequency band from the default values, you must define new thresholds to ensure accurate spindle detection.

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

