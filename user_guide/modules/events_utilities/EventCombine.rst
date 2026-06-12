.. _module_eventcombine:

Event Combine
=============

**Module name:** ``EventCombine``

**Package:** CEAMSModules 7.4.0

**Version:** 2.0.0

Overview
--------

This class combines two lists of events, with or without selection.

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
     - Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels'])
     - —
     - The first list of events
   * - ``event1_name``
     - String
     - —
     - The name of the first event to combine
   * - ``events2``
     - Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels'])
     - —
     - The second list of events
   * - ``event2_name``
     - String
     - —
     - The name of the second event to combine.
   * - ``channel1_name``
     - String or list of string
     - —
     - The channel name to extract events1 or the channel name saved in a list.
   * - ``channel2_name``
     - String or list of string
     - —
     - The channel name to extract events1 or the channel name saved in a list.
   * - ``behavior``
     - String
     - union
     - | Select how to combine events : union (all events) or
       | intersection (concurrent events only).
   * - ``new_event_group``
     - String
     - —
     - The group of the created (combined) list of events.
   * - ``new_event_name``
     - String
     - —
     - The name of the created (combined) list of events.
   * - ``new_event_chan``
     - String
     - —
     - The name of the created (combined) list of events.

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
     - Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels'])
     - The new events list created.

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Event Combine** under the **Events Utilities** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.
