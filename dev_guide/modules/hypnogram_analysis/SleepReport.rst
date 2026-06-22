.. _module_sleepreport:

Sleep Report
============

**Module name:** ``SleepReport``

**Package:** CEAMSModules 7.4.0

**Version:** 2.1.0

Overview
--------

Generate a sleep report in CSV file. The sleep report is made of about 300 statistics. These stats are based on the sleep stages and the sleep cycles produced by the module SleepCycleDelimiter.

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
     - The name of the file being analysed, it will be written in the report in the first column.
   * - ``sleep_stages``
     - pandas DataFrame
     - None
     - A dataframe with all sleep stages of the file to analyze.
   * - ``sleep_cycles``
     - array
     - None
     - Array of sleep cycles. This is the one selected by the user.
   * - ``sleep_cycles_params``
     - dict
     - None
     - Parameters that were selected by the user to create the sleep cycles.
   * - ``record_info``
     - dict
     - None
     - Information about the user from the PSG file.
   * - ``rem_periods``
     - array
     - None
     - List of REM periods
   * - ``report_constants``
     - dict
     - None
     - Constants used in the report (N_HOURS, N_CYCLES)
   * - ``html_report``
     - bool
     - True
     - Generate the HTML report if True.
   * - ``html_report_config``
     - None
     - None
     - This input is not used in the module.
   * - ``csv_report``
     - bool
     - True
     - Generate the CSV report if True.
   * - ``output_prefix``
     - string
     - None
     - The prefix of the report filename
   * - ``output_directory``
     - string
     - None
     - The path to the output directory

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
   * - ``report``
     - pandas DataFrame
     - Dataframe with all statistics of the report. This is then used as an input to another module to produce the HTML report.

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Sleep Report** under the **Hypnogram Analysis** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.
