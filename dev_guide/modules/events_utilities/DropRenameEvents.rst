.. _module_droprenameevents:

Drop/Rename Events
==================

**Module name:** ``DropRenameEvents``

**Package:** CEAMSModules 7.5.0

**Version:** 2.0.0

Overview
--------

To drop events and/or rename events group and/or name.

We suppose that the output file has already all the events. We want to rename some events (events_to_rename), so new_events is only the new set of events renamed (all untouched events are not included in new_events). We also want to drop some events (events_to_drop_in).

.. warning:: the renamed events are added as new_events, so we need to drop the original (not renamed) events. The output "events_to_drop_out" also include the original events that has been renamed.

.. warning:: if the renamed events also exists in the original events, they will be deleted by the PSgWriter, they must be added on the new_events. I.E. renaming the stage 4 to stage 3 will remove the original (valid) stage 3.

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
     - pandas DataFrame columns=['group','name','start_sec','duration_sec','channels']
     - —
     - Original list of events.
   * - ``events_to_drop_in``
     - list of tuple
     - —
     - | Events group and name to remove from the file.
       | ex. [('group1', 'name1')
       | ('group2', 'name2')]
   * - ``events_to_rename``
     - list of tuple
     - —
     - | Events group and name to remove from the file.
       | ex. [('group1_ori', 'name1_ori', 'group1_new', 'name1_new')
       | ('group2_ori', 'name2_ori', 'group2_new', 'name2_new')]

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
   * - ``new_events``
     - pandas DataFrame columns=['group','name','start_sec','duration_sec','channels']
     - Modified list of events (renamed and dropped if apply).
   * - ``events_to_drop_out``
     - list of tuple
     - | Events group and name to remove from the file.
       | ex. [('group1', 'name1')
       | ('group2', 'name2')]

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Drop/Rename Events** under the **Events Utilities** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.
