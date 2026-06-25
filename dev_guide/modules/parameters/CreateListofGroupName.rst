.. _module_createlistofgroupname:

Create List of Group Name
=========================

**Module name:** ``CreateListofGroupName``

**Package:** CEAMSModules 7.5.0

**Version:** 2.0.0

Overview
--------

Creates a list of tuples that has two value of group and name: [(group0, name0), (group1, name1)]

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
     - pandas DataFrame
     - —
     - Pandas DataFrame columns=['group','name','start_sec','duration_sec','channels']
   * - ``group``
     - str
     - —
     - The group type to filter by (e.g., 'stage' for sleep stage events)

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
   * - ``group_name_list``
     - List[Tuple(str, str)]
     - List of (group, name) tuples for events matching the specified group

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Create List of Group Name** under the **Parameters** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.
