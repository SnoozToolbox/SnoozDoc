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
* Muscle artifact [1] : Segments with burst of activity in the frequency band 20.25-32 Hz, detected using EEG spectral analysis with optional EMG signal enhancement for improved accuracy.

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


Detector Details
-----------------

4.1 - Flatline Detector
~~~~~~~~~~~~~~~~~~~~~~~

The Flatline detector identifies segments of EEG data with abnormally low amplitude signals, indicating periods where the electrode has lost contact, the amplifier has malfunctioned, or the signal pathway is interrupted. These segments appear as nearly flat traces in the raw signal and typically contain minimal power across the standard EEG frequency range.

**Detection Methodology**

The detector uses spectral power estimates computed with Welch's method to identify flatlined segments. The algorithm operates as follows:

1. The EEG signal is divided into overlapping time windows
2. Spectral power is computed for each window using Welch's method
3. The broadband power across the 1-64 Hz frequency range is estimated by integrating the power spectrum
4. Segments where the broadband power falls below a user-defined threshold are flagged as flatlines

**Fixed Parameters**

- **Frequency band**: 1-64 Hz
- **Window length / step**: 6 s / 3 s

**User-defined Parameters**

- **Annotation group**: Output annotation group
- **Event name**: Output annotation name
- **Power threshold**: Flatline detection threshold (µV²; default = 0.25)


4.2 - High Frequency Burst Detector
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The High Frequency Burst detector identifies segments of EEG data containing bursts of high-frequency power (>25 Hz). These artifacts are characterized by sudden increases in spectral power within the high-frequency band and typically reflect electrode artifacts, glitches, or noise bursts that may be caused by poor electrode contact or external electromagnetic interference.

**Detection Methodology**

The detector uses spectral power estimates computed with Welch's method to identify high-frequency burst segments. The algorithm operates as follows:

1. The EEG signal is divided into overlapping time windows
2. Spectral power is computed for each window using Welch's method
3. The power in the high-frequency band (>25 Hz) is estimated by integrating the power spectrum
4. An epoch is flagged as a high-frequency burst when all three complementary thresholds are exceeded:

   - **Criterion A (Fixed threshold)**: The log10-transformed power exceeds a fixed threshold defined as the mean of the main Gaussian component plus a user-defined multiple of its standard deviation (SD). The power distribution is modeled using a three-component Gaussian Mixture Model (GMM) to account for the right-skewed distribution often caused by artifacts.
   
   - **Criterion B (Adaptive threshold)**: The power exceeds a user-defined multiple of the baseline median power computed from a 30-second window surrounding the segment under evaluation.
   
   - **Criterion C (Power ratio threshold)**: The ratio of high-frequency power (25-64 Hz) to broadband power (8-64 Hz) exceeds a user-defined threshold. This criterion helps distinguish true high-frequency bursts from cases where high-frequency activity is masked by strong low-frequency components.

5. An epoch is flagged as an artifact only when all three thresholds are simultaneously exceeded

**Fixed Parameters**

- **Frequency band**: >25 Hz (high-frequency band)
- **Window length / step**: 0.5 s / 0.25 s

**User-defined Parameters**

- **Annotation group**: Output annotation group
- **Event name**: Output annotation name
- **Threshold Criteria**:
  
  - (A) Fixed threshold: mean + X · SD (optimal range: 3-5)
  - (B) Adaptive threshold: X · baseline median (optimal range: 6-10)
  - (C) Power ratio: (25-64 Hz power) / (8-64 Hz power) (optimal range: 0.05-0.4)

.. note::
    To enhance detection quality and reduce false positives, particularly during spindles, alpha activity, or beta bursts, it is recommended to first increase the power ratio threshold (C). This requires a greater proportion of signal power in the 25-64 Hz frequency band before a segment is classified as an artifact, helping to distinguish true high-frequency bursts from low-frequency-dominated signals with incidental high-frequency components.


4.3 - Persistent Noise Detector
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Persistent Noise detector identifies segments of EEG data with outlier high-frequency power (>25 Hz). These artifacts represent periods with sustained or recurring high-frequency noise and typically reflect continuous electromagnetic interference, instrumental noise, or ongoing electrode contact issues that differ from transient bursts.

**Detection Methodology**

The detector uses spectral power estimates computed with Welch's method to identify segments with outlier high-frequency power. The algorithm operates as follows:

1. The EEG signal is divided into overlapping time windows
2. Spectral power is computed for each window using Welch's method
3. The power in the high-frequency band (>25 Hz) is estimated by integrating the power spectrum
4. An epoch is flagged as persistent noise when both complementary thresholds are exceeded:

   - **Criterion A (Fixed threshold)**: The log10-transformed power exceeds a fixed threshold defined as the mean of the main Gaussian component plus a user-defined multiple of its standard deviation (SD). The power distribution is modeled using a three-component Gaussian Mixture Model (GMM) to account for the right-skewed distribution often caused by artifacts.
   
   - **Criterion B (Power ratio threshold)**: The ratio of high-frequency power (25-64 Hz) to broadband power (1-64 Hz) exceeds a user-defined threshold. This criterion helps distinguish true persistent noise from cases where high-frequency activity is masked by strong low-frequency components.

5. An epoch is flagged as an artifact only when both thresholds are simultaneously exceeded

**Fixed Parameters**

- **Frequency band**: >25 Hz (high-frequency band)
- **Window length / step**: 6 s / 3 s

**User-defined Parameters**

- **Annotation group**: Output annotation group
- **Event name**: Output annotation name
- **Threshold Criteria**:
  
  - (A) Fixed threshold: mean + X · SD (optimal range: 3-5)
  - (B) Power ratio: (25-64 Hz power) / (1-64 Hz power) (optimal range: 0.1-0.4)

.. note::
    To reduce false positives, particularly during low-amplitude REM sleep, it is recommended to first increase the power ratio threshold (B). This requires a greater proportion of signal power in the 25-64 Hz frequency band before a segment is classified as an artifact, helping to distinguish true persistent noise from low-frequency-dominated signals with incidental high-frequency components.


4.4 - Power Line Contamination Detector
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Power Line Contamination detector identifies segments of EEG data corrupted by power line interference at 50 or 60 Hz. These artifacts represent electrical contamination from AC power supply and are typically characterized by narrow-band oscillations at the power line frequency, which can obscure genuine EEG activity and interfere with subsequent analysis.

**Detection Methodology**

The detector uses spectral power estimates computed with Welch's method to identify segments with power line contamination. The algorithm operates as follows:

1. The EEG signal is divided into overlapping time windows
2. Spectral power is computed for each window using Welch's method
3. The power at the power line frequency (50 or 60 Hz) is estimated by integrating the power spectrum
4. An epoch is flagged as power line contamination when both complementary thresholds are exceeded:

   - **Criterion A (Fixed threshold)**: The log10-transformed power at the power line frequency exceeds a fixed threshold defined as the mean of the main Gaussian component plus a user-defined multiple of its standard deviation (SD). The power distribution is modeled using a three-component Gaussian Mixture Model (GMM) to account for the right-skewed distribution often caused by artifacts.
   
   - **Criterion B (Power ratio threshold)**: The ratio of power line frequency power (50/60 Hz) to broadband power (1-51/1-61 Hz) exceeds a user-defined threshold. This criterion helps distinguish true power line contamination from cases where power line activity is masked by strong low-frequency components.

5. An epoch is flagged as an artifact only when both thresholds are simultaneously exceeded

**Fixed Parameters**

- **Frequency band**: 50 or 60 Hz (power line frequency, selectable in Detectors Settings)
- **Window length / step**: 6 s / 3 s

**User-defined Parameters**

- **Annotation group**: Output annotation group
- **Event name**: Output annotation name
- **Threshold Criteria**:
  
  - (A) Fixed threshold: mean + X · SD (optimal range: 0-2, where 0 is the mean)
  - (B) Power ratio: (50/60 Hz power) / (1-61/1-51 Hz power) (optimal range: 0.05-0.2)

.. note::
    To reduce false positives, particularly during low-amplitude REM sleep, it is recommended to first increase the power ratio threshold (B). This requires a greater proportion of signal power at the power line frequency before a segment is classified as an artifact, helping to distinguish true power line contamination from low-frequency-dominated signals with incidental power line components.


4.5 - Baseline Variation Detector
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Baseline Variation detector identifies segments of EEG data with elevated power in the low-frequency band (below 0.4 Hz). These artifacts are caused by slow baseline shifts in the signal, typically resulting from physiological variations such as breathing, sweat artifact, or body movement. Baseline variations can obscure genuine EEG activity and interfere with spectral analysis.

**Detection Methodology**

The detector uses spectral power estimates computed with Welch's method to identify segments with outlier low-frequency power. The algorithm operates as follows:

1. Prior to spectral analysis, the EEG signal is low-pass filtered at 0.4 Hz using a 10th-order Butterworth IIR filter in second-order sections (SOS) format, applied with zero-phase filtering (filtfilt)
2. The filtered signal is divided into overlapping time windows
3. Spectral power is computed for each window using Welch's method
4. The power below 0.4 Hz is estimated by integrating the power spectrum
5. An epoch is flagged as baseline variation when the threshold is exceeded:

   - **Fixed threshold**: The log10-transformed power exceeds a fixed threshold defined as the mean of the main Gaussian component plus a user-defined multiple of its standard deviation (SD). The power distribution is modeled using a three-component Gaussian Mixture Model (GMM) to account for the right-skewed distribution often caused by artifacts.

**Fixed Parameters**

- **Frequency band**: Below 0.4 Hz (low-frequency band)
- **Window length / step**: 8 s / 4 s
- **Pre-detection filter**: 10th-order Butterworth low-pass at 0.4 Hz (SOS format, bidirectional zero-phase filtering)

**User-defined Parameters**

- **Annotation group**: Output annotation group
- **Event name**: Output annotation name
- **Threshold Criteria**:
  
  - Fixed threshold: mean + X · SD (optimal range: 3.5-5, default: 4)

.. warning::
    User-defined bandpass filters applied in the "2 - Filter EEG Signals" step may affect power estimates in the 0-0.4 Hz frequency band, potentially impacting baseline variation detection. Verify that your filter settings preserve the low-frequency components relevant to baseline variation detection.

.. note::
    To reduce false positives, particularly during sleep stages with large delta waves, increase the threshold value to require higher deviations from the baseline mean. A value of 5 helps reduce false positives in recordings with prominent low-frequency activity.


4.6 - Muscle Artifact Detector
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Muscle Artifact detector identifies segments of EEG data containing bursts of myogenic activity (muscle-related electrical activity). These artifacts are characterized by high-frequency oscillations in the 20.25-32.0 Hz frequency band, which typically reflect involuntary muscle contractions or tremors. The detector can utilize both EEG and EMG (electromyography) signals to enhance detection accuracy by identifying periods where muscle activity is elevated.

**Detection Methodology**

The detector uses spectral power estimates computed with Welch's method to identify muscle artifact segments. The algorithm operates as follows:

1. The EEG signal (0.3-30 Hz filtered and down sampled to 64 Hz) is divided into overlapping time windows
2. Spectral power is computed for each window using Welch's method
3. The power in the myogenic frequency band (20.25-32.0 Hz) is estimated by integrating the power spectrum
4. A 3-minute local baseline window is used to establish the baseline activity level for comparison
5. An epoch is flagged as a muscle artifact if either Criterion A is met OR both Criteria B and C are met simultaneously:

   - **Criterion A (High-threshold EEG detection)**: The high-frequency activity of the 4-second epoch exceeds the local baseline median by a high factor (default: 4.5× the baseline)
   
   - **Criterion B (EMG threshold)**: The myogenic activity on the EMG signal exceeds a user-defined multiple of the baseline median (default: 4× the baseline)
   
   - **Criterion C (Low-threshold EEG detection)**: The myogenic activity on the EEG signal exceeds a moderate threshold (default: 3.5× the baseline)

**Fixed Parameters**

- **Frequency band**: 20.25-32.0 Hz (myogenic activity range)
- **Window length / step**: 4 s / 2 s
- **Baseline window**: 3 minutes
- **EEG preprocessing**: Bandpass filter (0.3-30 Hz, 6th order Butterworth IIR filter SOS format, bidirectional zero-phase filtering), downsampling (64 Hz)

**User-defined Parameters**

- **Annotation group**: Output annotation group
- **Event name - EEG**: Event name for artifacts detected exclusively from the EEG signal (high-threshold criterion)
- **Event name - EMG use**: Event name for artifacts detected using both EEG and EMG signals (combined criteria)
- **Threshold Criteria**:
  
  - (A) High applied on EEG: X · baseline median (default: 4.5; optimal range: 4-5)
  - (B) Applied on EMG: X · baseline median (default: 4; optimal range: 3-5)
  - (C) Low applied on EEG: X · baseline median (default: 3.5; optimal range: 3-4)

.. note::
    To enhance detection quality and reduce false positives, it is recommended to adjust the threshold values based on the characteristics of your data. Start by increasing the "(A) High applied on EEG" threshold if spindles and alpha waves are being incorrectly flagged as artifacts. Similarly, adjust the "(B) Applied on EMG" and "(C) Low applied on EEG" thresholds if the signal quality varies significantly across your dataset.


References
----------

[1] Brunner, D. et al. (1996) «Muscle artifacts in the sleep EEG: Automated detection and effect on all-night EEG power spectra», Journal of Sleep Research, 5(3), p. 155-164. Disponible sur: https://doi.org/10.1046/j.1365-2869.1996.00009.x.

Version History
-----------------

* v2.1.0 : Distributed with CEAMS package version 7.2.0 — Snooz beta 2.0.1
    - Initial release of the tool.

* v2.6.0 — Distributed with CEAMS package version 7.3.0 / Snooz beta 3.0.0
    - Handle bad channels properly, including those identified in “Inspect EEG Channels.”
    - Provide two sets of default threshold values, depending on the selected sleep stages.
    - Verify alias definitions from step “1 - Input Files” before running the tool.

* v2.7.0 : Distributed with CEAMS package version 7.4.0 — Snooz 1.0.0
    - Add error handling workflow for PSG loading from workspaces and display failed files in the UI.
    - Add error handling workflow for duplicated sleep stages.
    - Supports a list of EMG channels for the muscle artifact detector.

* v2.8.0 : Distributed with CEAMS package version 7.5.0 — Snooz 1.1.0
    - Support artifact detection when no EMG channel is available.
    - Updated the UI to clarify that spectral power estimation is based on the Welch method rather than STFT.
