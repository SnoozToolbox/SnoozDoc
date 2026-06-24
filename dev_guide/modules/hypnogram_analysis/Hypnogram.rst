.. _module_hypnogram:

Hypnogram
=========

**Module name:** ``Hypnogram``

**Package:** CEAMSModules 7.5.0

**Version:** 2.1.0

Overview
--------

Module to display in the results view an hypnogram and its sleep cycles.

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
     - pandas DataFrame
     - —
     - List of sleep stages. (columns=['group','name','start_sec','duration_sec','channels'])
   * - ``sleep_cycles``
     - List of tuples
     - —
     - | Each element of the list defines a sleep cycle. The first tuple is the
       | beginning and end of the NREM period. The second tuple is the beginning
       | and end of the REM period. Both beginning and end are inclusive indexes.
       | The last variable [is_complete] tells of this cycle is complete. An incomplete
       | cycle would be one without a REM period, it's often found at the end of the night.
       | ((NREM_BEGIN,NREM_END), (REM_BEGIN,REM_END), is_complete)
   * - ``epoch_len_sec``
     - —
     - —
     - See module settings for configuration details.
   * - ``fig_name``
     - String
     - —
     - Path to save the hypnogram picture (jpg).

Outputs
-------

This module has no outputs.

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Hypnogram** under the **Hypnogram Analysis** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.
