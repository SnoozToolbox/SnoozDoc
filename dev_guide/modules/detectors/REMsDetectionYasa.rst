.. _module_remsdetectionyasa:

REMs Detection Yasa
===================

**Module name:** ``REMsDetectionYasa``

**Package:** CEAMSModules 7.4.0

**Version:** 3.1.0

Overview
--------

REMsDetectionYasa detects Rapid Eye Movements (REMs) in EEG/EOG sleep recordings.

Raises
^^^^^^

NodeInputException If input parameters have invalid types or missing keys. NodeRuntimeException If an error occurs during execution.

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
     - list
     - —
     - List of raw signal objects containing EEG/EOG data.
   * - ``events``
     - DataFrame
     - —
     - DataFrame containing event-related information.
   * - ``sleepstages``
     - DataFrame
     - —
     - Sleep stage classification for each epoch.
   * - ``filename``
     - str
     - —
     - Name of the file being processed.
   * - ``amplitude``
     - float
     - —
     - Minimum amplitude threshold for REM detection.
   * - ``duration``
     - float
     - —
     - Minimum duration threshold for REM events.
   * - ``freq_rem``
     - tuple
     - —
     - Frequency range for REM detection (e.g., (0.5, 4 Hz)).
   * - ``relative_prominence``
     - float
     - —
     - Relative prominence threshold for REM detection.
   * - ``remove_outliers``
     - bool
     - —
     - Whether to remove statistical outliers in detection.
   * - ``rems_event_name``
     - str
     - —
     - Name assigned to detected REM events.
   * - ``rems_event_group``
     - str
     - —
     - Group name for REM events.
   * - ``include``
     - int or list
     - —
     - Sleep stage(s) to include in REM detection.

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
     - —
     - Output produced by this module.
   * - ``events_details``
     - DataFrame
     - A DataFrame containing detected REM events.

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **REMs Detection Yasa** under the **Detectors** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.
