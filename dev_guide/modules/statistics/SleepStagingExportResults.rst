.. _module_sleepstagingexportresults:

Sleep Staging Export Results
============================

**Module name:** ``SleepStagingExportResults``

**Package:** CEAMSModules 7.5.0

**Version:** 2.0.0

Overview
--------

* Saving performance metrics (accuracy, kappa, confidence) to TSV files
* Generating PDF reports with comparative hypnograms and confusion matrices

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
   * - ``ResultsDataframe``
     - pd.DataFrame
     - —
     - DataFrame containing sleep staging metrics (accuracy, kappa, confidence)
   * - ``info``
     - list
     - —
     - List containing [ground_truth_hypnogram, predicted_hypnogram, file_path]
   * - ``SavedDestination``
     - str
     - —
     - Directory path where results should be saved
   * - ``Checkbox``
     - bool
     - —
     - Flag indicating whether to save results (True) or skip (False)

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
   * - ``ExportResults``
     - str or None
     - Path to the generated TSV file if saved, None otherwise

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Sleep Staging Export Results** under the **Statistics** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.
