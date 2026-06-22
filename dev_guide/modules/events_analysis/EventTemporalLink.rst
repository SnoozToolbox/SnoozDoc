.. _module_eventtemporallink:

Event Temporal Link
===================

**Module name:** ``EventTemporalLink``

**Package:** CEAMSModules 7.4.0

**Version:** 2.0.0

Overview
--------

Generate temporal links.

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
   * - ``record_info``
     - dict
     - —
     - Information about the current record
   * - ``report_events``
     - dict(str, Pandas DataFrame)
     - —
     - | DataFrame of events associated with the label of the report. The events
       | are the one filtered/selected by the report criteria.
   * - ``sleep_report``
     - pandas DataFrame
     - —
     - DataFrame of the sleep report for the current subject.
   * - ``window_size``
     - float
     - 0.5
     - Window analysis size.
   * - ``temporal_links``
     - list[[bool, str, str]]
     - —
     - | List of temporal links report to generate. bool value can be ignored.
       | The str values are associated to the list of events received in the
       | 'report_events'. A temporal link report must be generate for each
       | pair of events.
   * - ``html_report``
     - bool
     - False
     - Generate the html report or not
   * - ``html_report_config``
     - TODO TYPE
     - —
     - TODO DESCRIPTION
   * - ``csv_report``
     - bool
     - True
     - Generate the CSV report or not
   * - ``output_prefix``
     - str
     - —
     - The prefix of the report filename
   * - ``output_directory``
     - str
     - —
     - The path to the output directory

Outputs
-------

This module has no outputs.

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Event Temporal Link** under the **Events Analysis** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.
