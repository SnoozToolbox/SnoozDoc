.. _module_spectraldetector:

Spectral Detector
=================

**Module name:** ``SpectralDetector``

**Package:** CEAMSModules 7.4.0

**Version:** 2.2.0

Overview
--------

This plugin detects events based on the spectrum. The plugin is flexible, an event can be detected when power goes above or below the threshold. The threshold can be fixed (as a uV^2 value) , adaptive based on a baseline window around the event (x BSL median) or adaptif based on the epochs of the recording (x epochs STD). The adaptive threshold can be x times the baseline median value or x times the standard deviation of the baseline. When a z-score is used as threshold (x BSL STD log10), the power values are log10 transformed to make them more normally distributed.

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
   * - ``psds``
     - dict
     - —
     - | The power spectral density of all windows.
       | psd : power (µV^2) narray [n_fft_windows x n_frequency_bins]
       | freq_bins : frequency bins (Hz); The frequencies of the bins within the psds
       | win_len : windows length (s); The length of the detection windows on which the psds was done (in seconds)
       | win_step : windows step (s); The step between the detection windows on which the psds was done (in seconds)
       | sample_rate : sampling rate of the original signal (Hz)
       | chan_label : channel label
       | start_time : start (s) of the signal (item of signals) on which the ffts are performed
       | end_time : end (s) of the signal (item of signals) on which the ffts are performed
       | duration : duraiton (s) of the signal (item of signals) on which the ffts are performed
   * - ``event_group``
     - string
     - —
     - Event group.
   * - ``event_name``
     - string
     - —
     - Event label.
   * - ``low_freq``
     - string
     - 0.5
     - The lower frequency of the bandwidth targeted by the detection
   * - ``high_freq``
     - string
     - 30
     - The higher frequency of the bandwidth targeted by the detection
   * - ``rel_freq``
     - string
     - 0
     - | '0' the frequency band is absolute (low_freq to high_freq)
       | '1' the frequency band is relative (absolute band / background band)
   * - ``bsl_low_freq``
     - string
     - 0.5
     - The lower frequency of the baseline used to compute the relative power.
   * - ``bsl_high_freq``
     - string
     - 30
     - The higher frequency of the baseline used to compute the relative power.
   * - ``threshold_val``
     - string or a list of float
     - —
     - | String : the value to threshold to detect events.
       | list : the value to threshold for each signal included in signals.
   * - ``threshold_unit``
     - string
     - fixed
     - | The threshold unit
       | -fxed
       | -x BSL median, x BSL STD or x BSL STD(log10)
       | -x epochs STD, x epochs STD(log10)
   * - ``threshold_behavior``
     - string
     - Above
     - | Above : Event is detected when activity goes above the threshold.
       | Below : Event is detected when activity goes below the threshold.
   * - ``sleep_stages``
     - pandas dataframe (columns=['group','name','start_sec','duration_sec','channels'])
     - —
     - (optional) Sleep stages list.
   * - ``baseline_win_len``
     - string
     - —
     - (optional) The baseline window length in seconds
   * - ``art_events``
     - Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels'])
     - —
     - (optional) Artefact events previously detected
   * - ``channel_dbg``
     - String
     - —
     - Channel label to save and exit detection info.

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
   * - ``events``
     - Pandas DataFrame
     - DataFrame events (columns=['group','name','start_sec','duration_sec','channels'])
   * - ``win_activity``
     - ndarray of n_windows
     - Spectral power in the frequency bins from low_freq to high_freq.
   * - ``win_bsl``
     - ndarray of n_windows
     - (Optional) Median\STD spectral power of the baseline window (low_freq to high_freq).

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Spectral Detector** under the **Detectors** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.
