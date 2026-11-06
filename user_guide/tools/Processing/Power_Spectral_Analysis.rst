.. _Power_Spectral_Analysis:

===============================
Analyze EEG Spectral Power
===============================

The tool assess the intensity (or power) of a time-domain signal across various frequency bands.

The analysis can be performed on chosen annotations (see :ref:`PSA_per_event_info_csv` for the variable definition) or can be carried out for each sleep stage (see :ref:`PSA_per_stage_info_csv` for the variable definition). 

.. note::

    For the report per sleep stages, you must specify the stages to be incorporated into the analysis, but there is also the possibility to run the tool on "unscored" data.

.. warning::

    The artifacts must be previously detected and saved in the accessory file in order to remove the artifacts from the analysis. 

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

**2 - Events to exclude**
    Select events to exclude from the analysis (i.e. artefacts previously detected and saved in the accessory file).

**3 - Filtering**
    The user must define the bandwidth of the bandpass filter and can optionally add a power-line notch filter.

    Filters are applied to the signals prior to running the tool. 
    The original signals stored in the PSG files remain unchanged.

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

**4 - Section selection**
    Specify the segment of the signal on which you intend to perform the analysis:
        - on chosen annotations
        - for each sleep stage selected by the user
    Additionally, you have the following options:
        1. Run the analysis exclusively on the signal within the sleep cycles.
        2. Run the analysis on the signal within the sleep cycles while excluding NREM periods.
        3. Run the analysis on the signal within the sleep cycles while excluding REM periods.

**5 - Annotations Selection**
    If the analysis is performed on chosen annotations, select them.

**6 - Spectral Settings**
    The analysis is performed by dividing the signal into multiple short windows to estimate spectral power. 
    This procedure is based on Welch’s [1] method, which applies a Fast Fourier Transform (FFT) to each window and averages the resulting periodograms. Define the window length (s) used for each FFT and the step size (s) between consecutive windows.
    
    .. note::

        The frequency bin resolution (Hz) depends of the window length (s) used to perform each FFT.

        Frequency bin resolution : 1 / [fft windows length (s)]
        
        I.e. 1 / 5 s = 0.2 Hz or 1 / 4 s = 0.25 Hz

    It is common to average the power from a few frequency bins in order to estimate the spectral power in a frequency band.
    Define the width (Hz) of the frequency bands you are interested in. 
    Define also the first and last frequency to analyze (the maximum is half the sampling frequency (Hz) of the channels to analyze).

    **Power spectral analysis methods:**

    - **Standard power spectral analysis** 
    
    The power is estimated with the Welch's method for each frequency bin and then averaged across the frequency bins of a frequency band.


    - **Periodic/Aperiodic with IRASA method** 
    
    The periodic/aperiodic power is estimated with the Irregular Resampling Auto-Spectral Analysis (IRASA) method for each frequency bin and then averaged across the frequency bins of a frequency band [2].

    The IRASA method is based on the principle that periodic and aperiodic components of the power spectrum can be separated by resampling the signal at non-integer rates. This method is applied on each selected window of the signal, leading to be more time consuming than the FOOOF method which is applied on the averaged power across the frequency bins of a frequency band.

    IRASA, implemented with yasa library, methods, were implemented with the default parameters of the original publications [2].


    - **Periodic/Aperiodic with FOOOF method** 
    
    The periodic/aperiodic power is estimated with the Fitting Oscillations & One-Over-F (FOOOF) method for the averaged power across the frequency bins of a frequency band [3].

    The FOOOF method is based on the principle that the power spectrum can be decomposed into aperiodic (aperiodic) and periodic (periodic) components by fitting a model to the power spectrum.

    FOOOF, implemented with fooof library, methods, were implemented with the default parameters of the original publications [3].

    .. warning::

        **FOOOF numerical sensitivity and reproducibility**

        FOOOF uses peak detection and numerical optimization to separate periodic
        and aperiodic components. Small numerical differences in the input spectrum
        or fitting calculations can change the detected peaks or fitted parameters,
        particularly for weak, overlapping or near-threshold peaks.

        Results may therefore differ across operating systems, library versions or
        numerical environments, even with the same data and analysis settings.
        Differences need not be limited to the last decimal places: some fits can
        produce noticeably different component powers while retaining similar
        full-model error and R2 scores.

        For reproducibility, record the Snooz and package versions, analysis
        settings and numerical environment. Inspect the spectrum and fitted model
        when results differ substantially; similar quality scores alone do not
        establish equivalent periodic or aperiodic results.

**7 - Output File**
    Whether the analysis is performed per sleep stage or per chosen annotations :  

        Define how to average the spectral power across the recording.

            - Choose "Total" to generate the average through the whole recording.
            - Choose "Distribution per hour" to generate the average for each elapsed clock hour from hour 1 to 9.
            - Choose "Distribution per hour spent in each sleep stage" to generate the average for each stage hour from hour 1 to 9. (Only available if the analysis is performed per sleep stage)
            - Choose "Distribution per sleep cycle" to generate the average per sleep cycle, from sleep cycle 1 to 6.
        
        The maximum number of hours or sleep cycles are defined in the configuration page "Hours and Cycles".
        The starting point is either the first sleep stage or the sleep onset, depending on the settings in "step 4 - Section Selection".
 
    The output file is a .tsv (tab separated values) file. Each line is specific to a subject, a channel and a frequency band. 

    .. warning::
        The output data is added (appended) to the output file, the output file will be modified each time the tool is run.

    **Periodic/aperiodic report**

    If the user selects the periodic/aperiodic power spectral analysis, two separate .tsv report files will be generated, one for the periodic power spectral analysis and one for the aperiodic power spectral analysis.

    **FOOOF report**
    
    The FOOOF periodic and aperiodic reports include columns ending in ``_fit_err`` and ``_fit_r2``. The prefix identifies the analyzed period and, when applicable, the sleep stage. For example, ``clock_h7_W_fit_err`` describes the fit for wakefulness during elapsed clock hour 7.

    These indicators describe the **full fitted model** (periodic and aperiodic
    components combined) over the analyzed frequency range. They do not measure
    the accuracy of an individual peak or of either component separately. The same
    scores are reported in both component reports and repeated across frequency
    band rows for a given subject, channel and analyzed period.

    ``_fit_err``
        Mean absolute difference between the input log10 power spectrum and the
        full fitted model. Lower values indicate a closer fit. The error is
        expressed in log10 power space, not as a percentage or in linear power
        units. It is missing when no fit was performed or no finite error is
        available.

    ``_fit_r2``
        Squared Pearson correlation between the input log10 power spectrum and
        the full fitted model. Values closer to 1 indicate stronger agreement in
        spectral shape, but do not guarantee accurate peak parameters or component
        separation. It is missing when no fit was performed or the metric is
        undefined.

    No quality rejection threshold is applied: these indicators are provided for
    inspection, and a low R2 or high error alone does not exclude the result from
    the report. Missing indicators must not be interpreted as zero error or a
    successful fit.

.. toctree::
   Power_Spectral_Analysis/PSA_per_stage_info_csv
   Power_Spectral_Analysis/PSA_per_event_info_csv

References
----------

[1] Welch, P. D. (1967). The use of fast Fourier transform for the estimation of power spectra: A method based on time averaging over short, modified periodograms. IEEE Transactions on audio and electroacoustics, 15(2), 70-73.

[2] Wen, H., & Liu, Z. (2016). Separating fractal and oscillatory components in the power spectrum of neurophysiological signal. Brain topography, 29(1), 13-26.

[3] Donoghue, T., Haller, M., Peterson, E. J., Varma, P., Sebastian, P., Gao, R., ... & Voytek, B. (2020). Parameterizing neural power spectra into periodic and aperiodic components. Nature neuroscience, 23(12), 1655-1665.


Version History
-----------------

* v2.1.0 : Distributed with CEAMS package version 7.2.0 — Snooz beta 2.0.1
    - Initial release of the tool.

* v2.7.0 : Distributed with CEAMS package version 7.3.0 — Snooz beta 3.0.0
    - Refactored the output report to distinguish between elapsed clock time and sleep-stage time. 
    - Added new variables representing the combined N2 + N3 stages.
    - Added support for duplicated annotation names in different annotation groups.
    - Improve path, filename, and extension handling for sleep cycle warning log file.

* v3.1.0 : Distributed with CEAMS package version 7.4.0 — Snooz 1.0.0
    - Periodic/Aperiodic power spectral analysis is now available in addition to the standard spectral analysis.
    - The output report exports two separate reports for periodic and aperiodic power spectral analysis if the user selects to analyse them.
    - Add error handling workflow for PSG loading from workspaces and display failed files in the UI.
    - Add error handling workflow for duplicated sleep stages in the annotations file.

* v4.6.0 : Distributed with CEAMS package version 7.5.0 — Snooz 1.1.0
    - Fixed the widget enabling/disabling issue in Step 5: Annotation Selection.
    - Replaced occurrences of the term "rhythmic" with "periodic" throughout the UI and output reports.
    - Added support for artifact removal in per-annotation analyses.
    - Added support for analyzing EEG power spectra based on the timing of events detected in another signal (e.g., REM tonic events detected in EOG signals).
    - Added power distribution by hour and by sleep cycle to the spectral analysis per-annotation report.
    - Unified column names across the per-stage and per-event reports.
    - Ensure the multilingual PSG header reader uses UTF-8 encoding to generate valid UTF-8 reports.
    - Made spectral bin selection robust to non-integer sampling rates and support minimum bandwidths as narrow as the frequency-bin resolution. 
    - Optimized the report writing.
    - Fixed minimum FFT window duration checks, particularly for non-integer sampling rates.
    - Fixed filter cutoff validation prior to running the analysis.
    - Fixed workspace loading to keep FOOOF and IRASA settings.
    - Added full-model FOOOF fitting error and squared-correlation indicators to the periodic and aperiodic reports.