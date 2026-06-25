.. _module_trimsignal:

Trim Signal
===========

**Module name:** ``TrimSignal``

**Package:** CEAMSModules 7.5.0

**Version:** 2.0.0

Overview
--------

Trim a list of SignalModel objects and an events table to a target time window.

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
     - list[SignalModel]
     - —
     - | Input signal segments to crop. Each element is expected to provide
       | at least: `samples`, `sample_rate`, `start_time`, `end_time`, and `duration`.
   * - ``events``
     - pandas.DataFrame
     - —
     - Event annotations with at least `start_sec` and `duration_sec` columns.
   * - ``start_sec``
     - float \| str
     - —
     - Absolute start time (in seconds) of the trimming window.
   * - ``duration_sec``
     - float \| str
     - —
     - Duration (in seconds) of the trimming window.
   * - ``reset_time``
     - bool
     - True
     - | If True, output signal/event times are shifted so trimmed data starts at 0.
       | If False, absolute timeline is preserved.

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
   * - ``signals``
     - list[SignalModel]
     - Deep-copied and trimmed signals, with updated timing metadata.
   * - ``events``
     - pandas.DataFrame
     - | Events overlapping the trimming window, clipped to boundaries and optionally
       | time-shifted depending on `reset_time`.

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Trim Signal** under the **Signal Processing** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.
