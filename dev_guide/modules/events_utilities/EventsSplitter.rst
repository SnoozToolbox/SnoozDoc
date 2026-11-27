.. _module_eventssplitter:

Events Splitter
===============

**Module name:** ``EventsSplitter``

**Package:** CEAMSModules 7.5.0

**Version:** 2.0.0

Overview
--------

Class to split too long events.

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
     - Pandas DataFrame
     - —
     - DataFrame events to split (columns=['group','name','start_sec','duration_sec','channels'])
   * - ``max_length_s``
     - str or float
     - —
     - | Event maximum length or longest duration before a split is performed.
       | I.e. max_length_s=30 sec means that events longer than 30s are split into multiple events with a maximum duration of 30s each.

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
   * - ``splitted_events``
     - Pandas DataFrame
     - DataFrame of splitted events (columns=['group','name','start_sec','duration_sec','channels'])

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Events Splitter** under the **Events Utilities** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.
