.. _Spindle_detection_SUMO:

===============================
Spindle Detection (SUMO)
===============================

Description
-----------------

A spindle is "a train of distinct waves with frequency 11–16 Hz (most commonly 12–14 Hz) with a duration ≥0.5 s, usually maximal in amplitude using central derivations" [1]

.. This tool allows for the detection of spindles in specific sleep stages using the algorithms from (Kaulen et al. 2022) [2].

This tool enables the automated detection of sleep spindles in specific sleep stages using SUMO (Slim U-Net trained on MODA), a deep learning model inspired by the U-Net architecture (Kaulen et al. 2022) [2]. 
SUMO is designed to approximate expert consensus annotations derived from the Massive Online Data Annotation (MODA) project, which aggregates scores from multiple human experts to enhance reliability. Unlike traditional feature-based spindle detection methods, SUMO leverages deep convolutional networks to process minimally preprocessed EEG signals, achieving a higher level of agreement with expert consensus than previous algorithms, such as A7. 
The model has been shown to surpass expert-level accuracy, particularly in challenging cases, such as older individuals whose spindle characteristics are more difficult to detect. By automating the spindle identification process with superior precision, SUMO facilitates large-scale spindle studies while reducing the impact of intra- and inter-rater variability observed in manual scoring.

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

      See :ref:`spindle_SUMO_cohort_info_csv` for the variable definition. 

Steps
-----------------

**1 - Input Files**

   Start by opening your PSG files (.edf, .eeg or .sts).

   * The .tsv file is also needed for the EDF format.

   * The .sig file is also needed for Stellate format.

   * The whole NATUS subject folder is also needed for the .eeg format.

**2 - Non valid events**

   Select events to disable the spindle detection.

   .. note::

      If artefacts have not already been identified and saved in the accessory file, it is recommended to use the :ref:`Artifact_Detection` tool in the *Preprocessing* module before running SUMO for better detection accuracy.  

**3 - Spindle Detector**

   Define the minimum and maximum duration of kept spindles.  
   Define in which sleep stage you want to detect spindles.  
   You can also choose to detect spindle in the sleep cycles only or to exclude sleep periods from the analysis.

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


