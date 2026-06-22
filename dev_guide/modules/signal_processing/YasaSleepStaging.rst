.. _module_yasasleepstaging:

Score Sleep Stages YASA
=======================

**Module name:** ``YasaSleepStaging``

**Package:** CEAMSModules 7.4.0

**Version:** 2.0.0

Overview
--------

Automatic sleep stage classification using YASA's machine learning model. Handles both validation (against expert scores) and prediction modes.

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
   * - ``filename``
     - str
     - —
     - Path to the input data file
   * - ``signals_EEG``
     - list
     - —
     - List of EEG signal objects (required)
   * - ``signals_EOG``
     - list
     - —
     - List of EOG signal objects (optional)
   * - ``signals_EMG``
     - list
     - —
     - List of EMG signal objects (optional)
   * - ``sleep_stages``
     - pd.DataFrame
     - —
     - Expert-scored sleep stages (required in validation mode)
   * - ``stage_group``
     - str
     - —
     - group to add the predicted stages
   * - ``validation_on``
     - bool
     - —
     - Flag indicating validation mode (True) or prediction mode (False)

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
   * - ``results``
     - pd.DataFrame
     - Classification metrics (accuracy, kappa, confidence, F1 scores)
   * - ``info``
     - list
     - Contains [ground_truth_hypnogram, predicted_hypnogram, filename]
   * - ``new_events``
     - pd.DataFrame
     - Updated events with predicted sleep stages
   * - ``events_to_remove``
     - list of tuple of n events to remove.
     - [('group1', 'name1'), ('group2', 'name2')]

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Score Sleep Stages YASA** under the **Signal Processing** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.
