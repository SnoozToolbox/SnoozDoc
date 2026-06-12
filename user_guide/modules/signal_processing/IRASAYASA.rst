.. _module_irasayasa:

IRASA YASA
==========

**Module name:** ``IRASAYASA``

**Package:** CEAMSModules 7.4.0

**Version:** 0.0.0

Overview
--------

Spectral power decomposition using IRASA algorithm (Iterative Rational Autocorrelation Decomposition Analysis).

This class implements signal decomposition to separate rhythmic (periodic/oscillatory) components from arhythmic (aperiodic/broadband) components of EEG or other time-series signals. The algorithm uses the YASA library's IRASA implementation to perform the spectral decomposition.

Inputs
------

.. list-table::
   :widths: 25 20 15 50
   :header-rows: 1
   :align: left
   :class: left-align-caption wrap-table

   * - Input
     - Format
     - Default
     - Description
   * - ``signals``
     - list of SignalModel objects
     - —
     - | - signal.samples : numpy array of shape (N_samples,) containing the raw signal data
       | - signal.sample_rate : float, sampling rate of the signal in Hz
       | - signal.channel : str, channel label/name for identification
       | - signal.start_time : float, start time of the signal in seconds (optional)
   * - ``win_len_sec``
     - float or str
     - —
     - | Window length in seconds for the spectral analysis (e.g., 4.0)
       | Determines the time-frequency resolution of the analysis.
   * - ``win_step_sec``
     - float or str
     - —
     - | Window step/overlap in seconds between consecutive FFT windows.
       | Controls the temporal resolution of the PSD computation.
   * - ``window_name``
     - str
     - —
     - | Name of the windowing function to apply before FFT (e.g., 'hann', 'hamming', 'blackman').
       | Reduces spectral leakage from windowing effects.
   * - ``first_freq``
     - float or str
     - —
     - | Lower frequency boundary (Hz) for the IRASA decomposition analysis.
       | Only frequency components within [first_freq, last_freq] are analyzed.
   * - ``last_freq``
     - float or str
     - —
     - | Upper frequency boundary (Hz) for the IRASA decomposition analysis.
       | Only frequency components within [first_freq, last_freq] are analyzed.
   * - ``flag``
     - bool or str, optional (default: False)
     - False
     - It does nothing right now and can be used in the future to control whether to bypass the computation or not.

Outputs
-------

.. list-table::
   :widths: 25 20 65
   :header-rows: 1
   :align: left
   :class: left-align-caption wrap-table

   * - Output
     - Format
     - Description
   * - ``rhythmic_psd``
     - list of dicts
     - | List of dictionaries (one per input signal) containing rhythmic spectral components.
       | Each dictionary contains:
       | - 'psd' : numpy array of shape (N_epochs, N_freq_bins)
       | Rhythmic power spectral density (periodic component ratio)
       | - 'freq_bins' : numpy array of shape (N_freq_bins,)
       | Frequency bins in Hz corresponding to the PSD spectrum
       | - 'win_len' : float
       | Window length used for FFT in seconds
       | - 'win_step' : float
       | Window step/overlap in seconds
       | - 'sample_rate' : float
       | Sampling rate of the original signal in Hz
       | - 'chan_label' : str
       | Channel label from the input signal
       | - 'start_time' : float
       | Start time of the signal in seconds
       | - 'end_time' : float
       | End time of the signal in seconds
       | - 'duration' : float
       | Total duration of the signal in seconds
       | - 'flag' : str (value: 'rhythmic')
       | Flag indicating this is the rhythmic component
   * - ``arhythmic_psd``
     - list of dicts
     - | List of dictionaries (one per input signal) containing arhythmic spectral components.
       | Each dictionary has identical structure to rhythmic_psd but with:
       | - 'psd' : numpy array of shape (N_epochs, N_freq_bins)
       | Arhythmic power spectral density (aperiodic component)
       | - 'flag' : str (value: 'arhythmic')
       | Flag indicating this is the arhythmic component

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **IRASA YASA** under the **Signal Processing** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.
