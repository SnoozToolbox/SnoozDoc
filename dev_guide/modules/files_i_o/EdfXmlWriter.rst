.. _module_edfxmlwriter:

Edf Xml Writer
==============

**Module name:** ``EdfXmlWriter``

**Package:** CEAMSModules 7.4.0

**Version:** 2.0.0

Overview
--------

Create an XML file based on compumedic format.

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
   * - ``filename``
     - string
     - —
     - Path and filename of the XML file to write.
   * - ``events``
     - Pandas DataFrame
     - —
     - DataFrame events (columns=['group','name','start_sec','duration_sec','channels'])
   * - ``epoch_len``
     - double
     - —
     - The epoch length in second.
   * - ``stages_df``
     - Pandas DataFrame
     - —
     - | Sleep stages (columns=['group','name','start_sec','duration_sec','channels'])
       | group='stage', name='0'(ex.'1','2',...), duration_sec=30, channel=[]

Outputs
-------

This module has no outputs.

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Edf Xml Writer** under the **Files I/O** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.
