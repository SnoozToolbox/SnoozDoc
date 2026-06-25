.. _module_edfannotationsreader:

EDF Annotations Reader
======================

**Module name:** ``EDFAnnotationsReader``

**Package:** CEAMSModules 7.5.0

**Version:** 2.0.0

Overview
--------

Class to read the EDF Annotations signal and create a pandas dataframe with the events.

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
   * - ``annot_files``
     - list of string
     - —
     - List of edf file to read.
   * - ``psg_files``
     - list of string
     - —
     - List of edf file to read.

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
   * - ``filename``
     - string
     - The current file read.
   * - ``events``
     - Pandas DataFrame with columns ['group','name','start_sec','duration_sec','channels']
     - The list of events read.

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **EDF Annotations Reader** under the **Files I/O** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.
