.. _module_performancebyevent:

Performance By Event
====================

**Module name:** ``PerformanceByEvent``

**Package:** CEAMSModules 7.4.0

**Version:** 2.0.0

Overview
--------

Compare two sets of events (1:gold standard events, 2:estimated events). The class computes the performance by sample and the performance by event.

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
   * - ``events1``
     - Pandas DataFrame
     - —
     - The first set of events considered Gold Standard
   * - ``event1_name``
     - String
     - —
     - Label of the first set of events
   * - ``events2``
     - Pandas DataFrame
     - —
     - The second set of events considered estimation
   * - ``event2_name``
     - String
     - —
     - Label of the second set of events
   * - ``channel1_name``
     - String
     - —
     - Channel label to filter events1 (select events only from that channel)
   * - ``channel2_name``
     - String
     - —
     - Channel label to filter events2 (select events only from that channel)
   * - ``filename``
     - String (optional)
     - —
     - Filename to save performance evaluation
   * - ``jaccord_thresh``
     - int
     - 0.2
     - Jaccord index threshold (similarity between events to be valid).

Outputs
-------

This module has no outputs.

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Performance By Event** under the **Events Utilities** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.
