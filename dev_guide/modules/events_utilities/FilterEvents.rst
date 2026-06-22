.. _module_filterevents:

Filter Events
=============

**Module name:** ``FilterEvents``

**Package:** CEAMSModules 7.4.0

**Version:** 2.0.0

Overview
--------

Select (filter) events from specific sleep stages.

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
     - Events to select based on the sleep stages.
   * - ``sleep_stages``
     - pandas DataFrame
     - —
     - Sleep stages used to select events.
   * - ``stages_selection``
     - String
     - —
     - | A string of each sleep stage separeted by a comma with the same
       | valid values as sleep_stages. Example : '1,4,5,7'
   * - ``group_selection``
     - String
     - —
     - The group event to select. Can have many group separated by a comma.
   * - ``name_selection``
     - String
     - —
     - The name event to select. Can have many name separated by a comma.

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
   * - ``events_selected``
     - pandas DataFrame
     - Events selected from specific sleep stages (stages_selection).
   * - ``sleep_stages_selected``
     - andas DataFrame
     - Sleep stages selected from specific sleep stages (stages_selection).

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Filter Events** under the **Events Utilities** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.
