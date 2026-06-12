.. _module_stft:

Stft
====

**Module name:** ``Stft``

**Package:** CEAMSModules 7.4.0

**Version:** 2.0.0

Overview
--------

Compute the STFT (right-side only) on the signal split into sliding windows. Different normalizations of the FFT output are available. The normalization determines how the spectral values should be interpreted (sinusoidal amplitude estimation, integrated spectral power, or spectral density).

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
     - a list of SignalModel
     - —
     - | signal.samples : The actual signal data as numpy list
       | signal.sample_rate : sampling rate of the signal (used for STFT)
       | signal.channel : current channel label
   * - ``win_len_sec``
     - float
     - 1
     - window length in seconds (amount of data used for each FFT)
   * - ``win_step_sec``
     - float
     - 1
     - window step in seconds (interval between successive FFT computations)
   * - ``zeros_pad``
     - bool, optional
     - False
     - | Zero-pad the data to the next fast FFT size.
       | Zero padding increases the apparent frequency resolution and can
       | reduce computation time depending on the FFT size. Padding to the
       | next power of two is not always optimal.
       | (default = False)
   * - ``window_name``
     - string, optional
     - hann
     - Name of the window applied to the time series before computing the FFT.
   * - ``rm_mean``
     - bool, optional
     - True
     - | Remove the mean of each window prior to the FFT process
       | (default = True)
   * - ``norm``
     - string, optional
     - integrate
     - | Normalization applied to the FFT output.
       | (default = integrate)
       | "integrate" :
       | Normalization preserving the total signal power (energy).
       | This correction compensates for the attenuation introduced by
       | the window using the window noise gain. Each frequency bin
       | represents spectral power (units²/bin, e.g. µV²/bin).
       | Summing bins over a frequency range yields the total band power:
       | µV²/bin → sum over bins → µV²
       | "rms" :
       | Normalization preserving the amplitude of sinusoidal components.
       | This uses the coherent gain of the window so that the RMS amplitude
       | of sinusoidal signals is correctly represented in the spectrum.
       | Each bin represents the discrete spectral power associated with
       | that frequency component (units²/bin, e.g. µV²/bin).
       | "noise" :
       | Power spectral density (PSD) normalization suitable for estimating
       | broadband noise levels. The spectrum is expressed as a density
       | per frequency unit:
       | units²/Hz (e.g. µV²/Hz)
       | "no" :
       | No normalization applied to the FFT output.
   * - ``filename``
     - string
     - —
     - | Python filename (including path) used to save the STFT cache
       | in order to navigate through epochs.

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
   * - ``psd``
     - list of dicts
     - | keys of the dict:
       | psd : spectral power values
       | freq_bins : frequency bins (Hz)
       | win_len : window length (s)
       | win_step : window step (s)
       | sample_rate : sampling rate of the original signal (Hz)
       | chan_label : channel label

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Stft** under the **Signal Processing** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.
