.. _module_remsdetails:

REMs Details
============

**Module name:** ``REMsDetails``

**Package:** CEAMSModules 7.5.0

**Version:** 2.2.0

Overview
--------

To average REMs events characteristics such as duration, amplitude and density per stage and sleep cycle.

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
   * - ``recording_path``
     - string
     - —
     - The recording path.
   * - ``subject_info``
     - dict
     - —
     - | filename : Recording filename without path and extension.
       | id1 : Identification 1
       | id2 : Identification 2
       | first_name : first name of the subject recorded
       | last_name : last name of the subject recorded
       | sex :
       | ...
   * - ``signals``
     - a list of SignalModel
     - —
     - | Each item of the list is a SignalModel object as described below:
       | signal.samples : The actual signal data as numpy list
       | signal.sample_rate : the sampling rate of the signal
       | signal.channel : current channel label
       | signal.start_time : The start time of the signal in sec
       | signal.end_time : The end time of the signal in sec
       | (for more info : look into common/SignalModel)
   * - ``rems_events_details``
     - Pandas DataFrame
     - —
     - REMs events defined as (columns=['group', 'name', 'start_sec','duration_sec','channels'])
   * - ``artifact_events``
     - Pandas DataFrame
     - —
     - | Artifact events defined as (columns=['group', 'name','start_sec','duration_sec','channels'])
       | Artifacts are forced to zeros for the detection (with a tukey window)
   * - ``sleep_cycle_param``
     - Dict
     - —
     - Options used to define the cycles
   * - ``stages_cycles``
     - Pandas DataFrame
     - —
     - | Events defined as (columns=['group', 'name','start_sec','duration_sec','channels'])
       | The sleep stage group has to be commons.sleep_stage_group "stage" and
       | the sleep cycle group has to be commons.sleep_cycle_group "cycle".
   * - ``rems_det_param``
     - Dict
     - —
     - | rems_event_name : String label of the event name
       | stage_sel : Sleep stages selection to detect REMs in.
   * - ``report_constants``
     - dict
     - {}
     - Constants used in the report (N_HOURS, N_CYCLES)
   * - ``cohort_filename``
     - string
     - —
     - Path and filename to save the REMs characteristics for the cohort.
   * - ``export_rems``
     - bool or string
     - False
     - True : generate a file per subject of the characteristics of each REM event.

Outputs
-------

This module has no outputs.

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **REMs Details** under the **Events Utilities** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.
