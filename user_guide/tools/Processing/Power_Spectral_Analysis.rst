.. _Power_Spectral_Analysis:

===============================
Power Spectral Analysis (PSA)
===============================

Description
-----------------

The PSA is an algorithm designed to assess the intensity of a time-domain signal across various frequency bands.

The PSA can be performed on chosen annotations (see :ref:`PSA_per_event_info_csv` for the variable definition) or can be carried out for each sleep stage (see :ref:`PSA_per_stage_info_csv` for the variable definition). 

.. note::

    For the report per sleep stages, you must specify the stages to be incorporated into the PSA, but there is also the possibility to run the PSA on "unscored" data.

.. warning::

    The artifacts must be previously detected and saved in the accessory file in order to remove the artifacts from the analysis. 

Steps
-----------------

**Common settings**
    Define the sleep cycles criteria for your study. 

**1 - Input Files**
    Start by opening your PSG files (.edf, .eeg or .sts).

    * The .tsv file is also needed for the EDF format.

    * The .sig file is also needed for Stellate format.

    * The whole NATUS subject folder is also needed for the .eeg format.

**2 - Events to exclude**
    Select events to exclude from the PSA (i.e. artefacts previously detected and saved in the accessory file).

**3 - Filtering**
    Define the appropriate filtering to match your research analyses.

**4 - Section selection**
    Specify the segment of the signal on which you intend to perform the PSA.
        - The PSA can be performed on chosen annotations.
        - The PSA can be carried out for each sleep stage. You must specify the stages to be incorporated into the PSA.
    Additionally, you have the following options:
        1. Run the PSA exclusively on the signal within the sleep cycles.
        2. Run the PSA on the signal within the sleep cycles while excluding NREM periods.
        3. Run the PSA on the signal within the sleep cycles while excluding REM periods.

**5 - Annotations Selection**
    If the PSA is performed on chosen annotations, select them.

**6 - Spectral Settings**
    The PSA is performed through many short windows in order to estimate the spectral power.  
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
    If the PSA is performed per sleep stage :  

        Define how to average the spectral power across the recording.

            - Choose "Total" to generate the average through the whole recording.
            - Choose "Distribution per hour" to generate the average for each elapsed hour (clock hour) from hour 1 to 12. The starting point is the sleep onset.
            - Choose "Distribution per sleep cycle" to generate the average per sleep cycle, from sleep cycle 1 to 6.  The starting point is the sleep onset.

    The output file is a .tsv (tab separated values) file. Each line is specific to a subject, a channel and a frequency band. 


.. warning::
    
    The PSA data is added (appended) to the output file, the output file will be modified each time the PSA tool is run.


Report
---------

.. toctree::
   Power_Spectral_Analysis/PSA_per_stage_info_csv
   Power_Spectral_Analysis/PSA_per_event_info_csv
