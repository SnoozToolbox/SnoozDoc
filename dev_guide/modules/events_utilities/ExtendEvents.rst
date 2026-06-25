.. _module_extendevents:

Extend Events
=============

**Module name:** ``ExtendEvents``

**Package:** CEAMSModules 7.5.0

**Version:** 2.0.0

Overview
--------

Extend or shrink events by a percentage of their duration, applied to **each side**.

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
     - pandas.DataFrame
     - —
     - | A dataframe with required columns:
       | ['group', 'name', 'start_sec', 'duration_sec', 'channels']
   * - ``per_side_exten_percent``
     - float
     - —
     - | Percentage to extend (+) or shrink (−) **on each side**.
       | For example:
       | 50.0 → start moves 50% earlier, end moves 50% later
       | -20.0 → start moves 20% later, end moves 20% earlier

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
   * - ``extended_events``
     - pandas.DataFrame
     - Copy of `events` with updated 'start_sec' and 'duration_sec'.

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Extend Events** under the **Events Utilities** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.
