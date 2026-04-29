.. _Artifact_Detection:

=====================
Detect EEG Artifacts
=====================

This tool detects artifacts on EEG channels from PSG files.

**Types of artifacts**

Different types of artifacts are targeted.

* Flatline : Segments of low power, flatlined signal.
* High Frequency burst : Segments with a burst of high frequency power (>25 Hz).
* Persistent Noise : Segments with high frequency noise (>25 Hz).
* Power Line Contamination : Segments corrupted by 50 or 60 Hz power.
* Baseline Variation (Breathing) : Segments with high power in the low frequency band (<0.4 Hz).
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

Start by opening your PSG files (.edf, .sts or .eeg). 

- **European Data Format (EDF)** : 
  
  The corresponding .tsv file is required with .edf. Both files must be saved in the same directory and share the exact same filename.

- **Stellate format (up to version 6.2)** : 
  
  The corresponding .sig file is required with the .sts. Both files must be saved in the same directory and share the exact same filename.

- **NATUS format (version 9.1)** : 
  
  (*CEAMS users only*) The entire NATUS subject folder is required.

For more details on accepted formats, see :ref:`accepted_format`.

**2 - Filter the EEG signals**

The user must define the bandwidth of the bandpass filter and can optionally add a power-line notch filter.

Filters are applied to the EEG signals prior to running the detectors to focus on the relevant frequency bands for artifact detection. 
The original signals stored in the PSG files remain unchanged; only the filtered signals are used internally by the detectors.

The filter is a Butterworth design implemented in second-order-section (SOS) form and applied using bidirectional zero-phase filtering. 
This approach preserves the requested magnitude response while eliminating phase distortion.

**Bandpass filter parameters:**

- Type : IIR bandpass
- Family : Butterworth
- Order : 6 (internally halved before the forward/backward pass)
- Form : second-order sections (SOS)
- Application : bidirectional zero-phase filtering (filtfilt)

**Notch filter parameters:**

- Type : IIR stopband
- Family : Butterworth
- Order : 20 (internally halved before the forward/backward pass)
- Form : second-order sections (SOS)
- Application : bidirectional zero-phase filtering (filtfilt)


**3 - Detectors Settings**

The user must select the detectors to run and select the sleep stages to potentially establish a cleaner baseline.

.. note::

    Look at the "Artifact Detection" home page and the "Detectors Settings" step for more information.


Version History
-----------------

* v2.1.0 : Distributed with CEAMS package version 7.2.0 — Snooz beta 2.0.1
    - Initial release of the tool.

* v2.6.0 — Distributed with CEAMS package version 7.3.0 / Snooz beta 3.0.0
    - Handle bad channels properly, including those identified in “Inspect EEG Channels.”
    - Provide two sets of default threshold values, depending on the selected sleep stages.
    - Verify alias definitions from step “1 - Input Files” before running the tool.