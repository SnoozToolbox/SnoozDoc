.. _module_eventsleepreport:

Event Sleep Report
==================

**Module name:** ``EventSleepReport``

**Package:** CEAMSModules 7.5.0

**Version:** 2.0.0

Overview
--------

Generate event sleep report.

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
   * - ``events``
     - Pandas Dataframe
     - —
     - List of events.
   * - ``record_info``
     - dict
     - —
     - Dictionary of information about the current recording.
   * - ``sleep_stages``
     - Pandas Dataframe
     - —
     - List of sleep stages and sleep cycles.
   * - ``events_report_criteria``
     - list[dict]
     - —
     - | List of event report to generate. Each element is a dictionary with
       | all event's selection criteria used in the report.
       | (one report per item that can be identified with its name)
   * - ``nominal_values``
     - TODO TYPE
     - —
     - | TODO DESCRIPTION
       | (ne pas faire pour l'instant)
   * - ``report_constants``
     - dict
     - {}
     - Constants used in the report (N_HOURS, N_CYCLES)
   * - ``html_report``
     - bool
     - True
     - Generate the HTML report if True.
   * - ``html_report_config``
     - TODO TYPE
     - —
     - | TODO DESCRIPTION
       | (ne pas faire pour l'instant)
   * - ``csv_report``
     - bool
     - True
     - Generate the CSV report if True.
   * - ``save_events_report``
     - bool
     - False
     - Save events report if true.
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

.. list-table::
   :widths: 25 20 65
   :header-rows: 1
   :align: left
   :class: left-align-caption wrap-table

   * - Output
     - Format
     - Description
   * - ``report_events``
     - dict(str, Pandas DataFrame)
     - | DataFrame of events associated with the label of the report. The events
       | are the one filtered by the report criteria.
       | (events_report_criteria is no more usefull, report_events includes only event)

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Event Sleep Report** under the **Events Analysis** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.
