.. _module_sleepbouts:

Sleep Bouts
===========

**Module name:** ``SleepBouts``

**Package:** CEAMSModules 7.4.0

**Version:** 2.0.0

Overview
--------

SleepBouts

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
     - string
     - None
     - Filename of the input file.
   * - ``sleep_stages``
     - pandas DataFrame
     - None
     - A DataFrame containing the sleep stages.
   * - ``output_filename``
     - string
     - None
     - Filename of the output file.
   * - ``export_in_seconds``
     - string of bool
     - 1
     - Flag to export the duration in seconds.

Outputs
-------

This module has no outputs.

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Sleep Bouts** under the **Hypnogram Analysis** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.
