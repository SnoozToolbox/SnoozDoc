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
    The analysis is performed through many short windows in order to estimate the spectral power.  
    The procedure is called Short Time Fourier Transform (STFT).
    Define the window length (s) used to perform each FFT (Fast Fourier Transform) and at which window steps (s) each FFT is performed.
    
    .. note::

        The frequency bin resolution (Hz) depends of the window length (s) used to perform each FFT.

        Frequency bin resolution : 1 / [fft windows length (s)]
        
        I.e. 1 / 5 s = 0.2 Hz or 1 / 4 s = 0.25 Hz

    It is common to average the power from a few frequency bins in order to estimate the spectral power in a frequency band.
    Define the width (Hz) of the frequency bands you are interested in. 
    Define also the first and last frequency to analyze (the maximum is half the sampling frequency (Hz) of the channels to analyze).

**7 - Output File**
    If the analysis is performed per sleep stage :  

        Define how to average the spectral power across the recording.

            - Choose "Total" to generate the average through the whole recording.
            - Choose "Distribution per hour" to generate the average for each elapsed clock hour from hour 1 to 9.
            - Choose "Distribution per hour spent in each sleep stage" to generate the average for each stage hour from hour 1 to 9.
            - Choose "Distribution per sleep cycle" to generate the average per sleep cycle, from sleep cycle 1 to 6.
        
        The maximum number of hours or sleep cycles are defined in the configuration page "Hours and Cycles".
        The starting point is either the first sleep stage or the sleep onset, depending on the settings in "step 4 - Section Selection".
 
    The output file is a .tsv (tab separated values) file. Each line is specific to a subject, a channel and a frequency band. 

.. warning::
    
    The output data is added (appended) to the output file, the output file will be modified each time the tool is run.

Report
---------

.. toctree::
   Power_Spectral_Analysis/PSA_per_stage_info_csv
   Power_Spectral_Analysis/PSA_per_event_info_csv


Version History
-----------------

* v2.1.0 : Distributed with CEAMS package version 7.2.0 — Snooz beta 2.0.1
    - Initial release of the tool.

* v2.5.0 : Distributed with CEAMS package version 7.3.0 — Snooz beta 2.1.0
    - Refactored the output report to distinguish between elapsed clock time and sleep-stage time. 
    - Added new variables representing the combined N2 + N3 stages.
