Signal Processing
=================

.. toctree::
   :maxdepth: 1

   EpochSignal
   FilterSignal
   IcaComponents
   IcaRestore
   InvertSignals
   IRASAYASA
   MovingRMS
   PSACompilationFOOOF
   RemoveChannelArtefact
   Resample
   RescaleSignal
   ResetSignalArtefact
   YasaSleepStaging
   Stft
   SubtractSignals
   TrimSignal

Quick reference
---------------

.. list-table::
   :widths: 25 15 60
   :header-rows: 1
   :align: left
   :class: left-align-caption wrap-table

   * - Module
     - Version
     - Description
   * - :ref:`Epoch Signal <module_epochsignal>`
     - 2.0.0
     - Segments EEG signals into overlapping or non-overlapping epochs of fixed duration.
   * - :ref:`Filter Signal <module_filtersignal>`
     - 2.1.0
     - Applies a FIR/IIR filter to EEG signals.
   * - :ref:`Ica Components <module_icacomponents>`
     - 2.0.0
     - Find components of a signal with idependant component analysis.
   * - :ref:`Ica Restore <module_icarestore>`
     - 2.0.0
     - Reconstructs signal from ICA components.
   * - :ref:`Invert Signals <module_invertsignals>`
     - 2.0.0
     - Inverts signals.
   * - :ref:`IRASA YASA <module_irasayasa>`
     - 0.0.0
     - Spectral power decomposition using IRASA algorithm.
   * - :ref:`Moving RMS <module_movingrms>`
     - 2.0.0
     - Computes RMS value on a moving window.
   * - :ref:`PSA Compilation FOOOF <module_psacompilationfooof>`
     - 0.0.0
     - Analyses and reports the PSD output designed specifically for FOOOF analysis.
   * - :ref:`Remove Channel Artefact <module_removechannelartefact>`
     - 2.0.0
     - Removes full-channel artefacts from signals and events.
   * - :ref:`Resample <module_resample>`
     - 2.0.0
     - Resamples a signal.
   * - :ref:`Rescale Signal <module_rescalesignal>`
     - 2.1.0
     - Creates a list of dictionaries with the channels from specific epochs during a recording.
   * - :ref:`Reset Signal Artefact <module_resetsignalartefact>`
     - 2.1.0
     - Resets the signal that occurs during an artefact.
   * - :ref:`Score Sleep Stages YASA <module_yasasleepstaging>`
     - 2.0.0
     - Automatic sleep stage classification using YASA's machine learning model.
   * - :ref:`Stft <module_stft>`
     - 2.1.0
     - Computes the STFT on the signal split into sliding windows.
   * - :ref:`Subtract Signals <module_subtractsignals>`
     - 2.0.0
     - Subtracts signals from a specific channel from the signals of a list of channels.
   * - :ref:`Trim Signal <module_trimsignal>`
     - 2.0.0
     - Trims continuous/discontinuous signal segments and their associated events to a time window defined by.
