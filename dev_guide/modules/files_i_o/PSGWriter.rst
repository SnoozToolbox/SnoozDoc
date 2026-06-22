.. _module_psgwriter:

PSGWriter
=========

**Module name:** ``PSGWriter``

**Package:** CEAMSModules 7.4.0

**Version:** 2.2.0

Overview
--------

Write a PSG file. The PSG signals are always in a file separated from the annotations file containning the events. 

.. note:: The setting (bool flag) "overwrite_signals" allows to overwrite the signal and "overwrite_events" allows to overwrite the events.

.. note:: If input_filename and output_filename are the same, the PSG file will be overwritten when overwrite_signals is True and the annotations file will be overwritten when overwrite_events is True.

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
   * - ``input_filename``
     - String
     - —
     - The name of the input file
   * - ``output_filename``
     - String
     - —
     - The name of the output file to write.
   * - ``signals``
     - List of SignalModel
     - —
     - Signals to write to a file
   * - ``new_events``
     - pandas DataFrame columns=['group','name','start_sec','duration_sec','channels']
     - —
     - New events to write to a file.
   * - ``events_to_remove``
     - list of tuple of n events to remove.
     - —
     - | Events group and name to remove from the file.
       | ex. [('group1', 'name1'), ('group2', 'name2')]
   * - ``overwrite_events``
     - bool
     - True
     - True to overwrite old events with the same group and name as the new ones.
   * - ``overwrite_signals``
     - bool
     - False
     - True to overwrite signals that's been modified

Outputs
-------

This module has no outputs.

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **PSGWriter** under the **Files I/O** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.
