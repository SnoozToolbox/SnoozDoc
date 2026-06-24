.. _module_edfxmlreader:

Edf Xml Reader
==============

**Module name:** ``EdfXmlReader``

**Package:** CEAMSModules 7.5.0

**Version:** 2.0.0

Overview
--------

Read events from a EDF.XML file

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
     - Path and filename of the XML file to read.
   * - ``event_name``
     - (optional) string or a list of string
     - —
     - Event label to extract from the XML.

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
     - Path and filename of the XML file read.
   * - ``events``
     - Pandas DataFrame
     - DataFrame events (columns=['group','name','start_sec','duration_sec','channels'])
   * - ``epoch_len``
     - double
     - The epoch length in second.
   * - ``stages_epoch``
     - array
     - | A sleep stage per epoch (an array of stages from 0-9)
       | 0 : awake
       | 1 : n1
       | 2 : n2
       | 3 : n3
       | 4 : n4
       | 5 : REM
       | 6 : movement
       | 7 : technician intervention
       | 9 : uncored
   * - ``stages_df``
     - Pandas DataFrame
     - | Sleep stages (columns=['group','name','start_sec','duration_sec','channels'])
       | group='stage', name='0'(ex.'1','2',...), duration_sec=30, channel=[]

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Edf Xml Reader** under the **Files I/O** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.
