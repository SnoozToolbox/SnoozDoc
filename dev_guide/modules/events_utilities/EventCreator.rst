.. _module_eventcreator:

Event Creator
=============

**Module name:** ``EventCreator``

**Package:** CEAMSModules 7.4.0

**Version:** 2.0.0

Overview
--------

EventCreator creates a pandas Dataframe of events.

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
   * - ``event_name``
     - str
     - —
     - The name of the event.
   * - ``group_name``
     - str
     - —
     - The group of the event.
   * - ``start_time``
     - double
     - —
     - The start time of the event from the beginning of the recording.
   * - ``duration``
     - double
     - —
     - The duration of the event.
   * - ``channels``
     - str
     - —
     - A space separated list of channels
   * - ``interval``
     - double
     - —
     - Interval in seconds between the start of two event
   * - ``count``
     - int
     - —
     - How many events to generate

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

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Event Creator** under the **Events Utilities** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.
