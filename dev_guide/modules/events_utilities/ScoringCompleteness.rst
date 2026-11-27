.. _module_scoringcompleteness:

Scoring Completeness
====================

**Module name:** ``ScoringCompleteness``

**Package:** CEAMSModules 7.5.0

**Version:** 2.0.0

Overview
--------

Evaluate if the scoring (events) is unique, complete and specifique to the sleep staging. The output file log any problems. The log includes which event (if any) is not unique or outside the sleep staging. The log also includes which part of the sleep stage does not have any scoring (events).

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
   * - ``sleep_stages``
     - Pandas Dataframe (columns=['group','name','start_sec','duration_sec','channels'])
     - —
     - List of sleep stages and sleep cycles.
   * - ``events``
     - Pandas Dataframe (columns=['group','name','start_sec','duration_sec','channels'])
     - —
     - The scoring, a list of events.
   * - ``output_file``
     - string
     - —
     - path and name of the output file to log the scoring problems.

Outputs
-------

This module has no outputs.

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Scoring Completeness** under the **Events Utilities** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.
