.. _Artifact_Detection:

===================
Detect Artifact
===================

Description
-----------------

This tool detects artifacts from PSG files.

Detection is performed on the entire recording. However, you can select specific sleep stages to potentially establish a cleaner baseline for the algorithms using a 3-component Gaussian Mixture Model (GMM). It is recommended to select sleep stages where the signal is typically cleaner (i.e. N1, N2, N3, R). 

While sleep stages are mandatory for sleep recordings, artifact detection can be run on any EEG recording if "Unscored" is selected for the sleep stages.

**Types of artifacts**

Different types of artifacts are targeted.

* Flatline : Segments of low power, flatlined signal.
* High Frequency burst : Segments with a burst of high frequency power (>25 Hz).
* Persistent Noise : Segments with high frequency noise (>25 Hz).
* Power Line Contamination : Segments corrupted by 50 or 60 Hz power.
* Baseline Variation (Breathing, Sweat) : Segments with high power in the low frequency band (<0.4 Hz).
* Muscle artifact : Segments with burst of activity in the frequency band 20.25-32 Hz.

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
