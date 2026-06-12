.. _modules_statistics:

Statistics
==========

This section documents the **Statistics** modules from the CEAMSModules package.
Use these modules to build custom Snooz processes.

Modules
-------

.. toctree::
   :maxdepth: 1

   MutualInfo
   PSACompilation
   PSAOnEvents
   SignalStats
   SleepStagingExportResults
   SlowWaveClassifier
   ThresholdComputation

Quick reference
---------------

.. list-table::
   :widths: 30 15 55
   :header-rows: 1
   :align: left
   :class: left-align-caption wrap-table

   * - Module
     - Version
     - Description
   * - :ref:`Mutual Info <module_mutualinfo>`
     - 2.0.0
     - Finds the mutual information between two lists of signals.
   * - :ref:`PSA Compilation <module_psacompilation>`
     - 2.2.0
     - Analyses and reports the PSD output.
   * - :ref:`PSA on Events <module_psaonevents>`
     - 2.1.0
     - Compiles the PSA run on selected events.
   * - :ref:`Signal Stats <module_signalstats>`
     - 2.0.0
     - Computes the mean and standard deviation of the input signals per epoch, per channel.
   * - :ref:`Sleep Staging Export Results <module_sleepstagingexportresults>`
     - 2.0.0
     - Processes and visualizes sleep staging results.
   * - :ref:`Slow Wave Classifier <module_slowwaveclassifier>`
     - 2.0.0
     - Classifies slow wave events based on a gaussian mixture.
   * - :ref:`Threshold Computation <module_thresholdcomputation>`
     - 2.1.0
     - Computes the value to threshold (i.e. µV) from a signals (i.e. EEG time series)
