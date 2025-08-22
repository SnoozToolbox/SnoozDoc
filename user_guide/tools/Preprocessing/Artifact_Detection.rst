.. _Artifact_Detection:

===================
Detect Artifact
===================

Description
-----------------

This tool detects artifacts from PSG files.

**Types of artifacts**

Different types of artifacts are targeted.

* Flatline : Segments of low power, flatlined signal.
* High Frequency burst : Segments with a burst of high frequency power (>25 Hz).
* Persistent Noise : Segments with high frequency noise (>25 Hz).
* Power Line Contamination : Segments corrupted by 50 or 60 Hz power.
* Baseline Variation (Breathing, Sweat) : Segments with high power in the low frequency band (<0.4 Hz).
* Muscle artifact : Segments with burst of activity in the frequency band 20.25-32 Hz.

Artifact detection performs better when similar sleep stages are selected, as the power distribution can be modeled more accurately.
Some detectors use a 3-component Gaussian Mixture Model (GMM) to estimate the standard deviation of non-corrupted data, 
which is then used to define the threshold value.

.. note::
    We recommend running artifact detection separately for NREM, REM, and Awake stages.
    Threshold values for the different algorithms can be edited; however, two sets of default values are also available.

.. warning::
    Make sure to use different annotation groups or names to avoid confusion when running artifact detection twice.
    The default labels reflect the selected sleep stages and the chosen set of default values.

While sleep stages are mandatory for sleep recordings, artifact detection can also be run on any EEG recording if "Unscored" is selected for the sleep stages.

Steps
-----------------

**1 - Input Files**

Start by opening your PSG files (.edf, .eeg or .sts). 

- The .tsv file is also needed for the EDF format. 

- The .sig file is also needed for Stellate format. 

- The whole NATUS subject folder is also needed for the .eeg format.

**2 - Filter the EEG signals**

The user must define the bandwidth of the bandpass filter and can optionally add a power line notch filter. 

**3 - Detectors Settings**

The user must select the detectors to run and select the sleep stages to potentially establish a cleaner baseline.

.. note::

    Look at the "Artifact Detection" home page and the "Detectors Settings" step for more information. 
