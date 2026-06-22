.. _module_defineeventgroup:

Define Event Group
==================

**Module name:** ``DefineEventGroup``

**Package:** CEAMSModules 7.4.0

**Version:** 2.0.0

Overview
--------

Define groups to events.

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
     - Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels'])
     - —
     - Lits of events (could miss the group column)
   * - ``groups``
     - dict
     - —
     - Group dictionary. Each item is an event name and the value is the group to add or modify.

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
     - Lits of events with the added or modified group.

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Define Event Group** under the **Events Utilities** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.
