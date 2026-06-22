.. _module_slowwavepicsgenerator:

Slow Wave Pics Generator
========================

**Module name:** ``SlowWavePicsGenerator``

**Package:** CEAMSModules 7.4.0

**Version:** 3.0.0

Overview
--------

Class to generate pictures of slow wave events.

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
   * - ``files``
     - dict
     - —
     - Keys are filenames. Each file contains a montage and a list of channel to process.
   * - ``file_group``
     - dict
     - —
     - Keys are filenames. Values are the group label.
   * - ``sw_char_folder``
     - str
     - —
     - Path to the folder containing the slow wave characteristics files.
   * - ``sw_events_def``
     - dict
     - —
     - Keys are filenames and values are group and name labels for sw events.
   * - ``ROIs_def``
     - dict
     - —
     - Keys are ROI names and values are the channels list and the blank flag.
   * - ``chans_ROIs_sel``
     - dict
     - —
     - Keys are channel labels or ROI names and values are the selection flag.
   * - ``pics_param``
     - dict
     - —
     - | Each key is a parameter to generate pictures.
       | The default values are :
       | 'cohort_avg': True,
       | 'cohort_sel': False,
       | 'subject_avg': False,
       | 'subject_sel': False,
       | 'show_sw_categories': False,
       | 'display': "mean_std", # all, mean, mean_std
       | 'neg_up': False,
       | 'force_axis': False, # False or [xmin, xmax, ymin, ymax]
       | 'output_folder': ''
   * - ``colors_param``
     - dict
     - —
     - | Each key is a parameter to generate pictures.
       | The default values are :
       | 'subjectavg': ['tab:blue', 'tab:red', 'tab:green', 'tab:purple', 'tab:orange', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan'],
       | 'subjectsel': ['tab:blue', 'tab:red', 'tab:green', 'tab:purple', 'tab:orange', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan'],
       | 'cohortavg': ['tab:blue', 'tab:red', 'tab:green', 'tab:purple', 'tab:orange', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan'],
   * - ``alignment_param``
     - string
     - —
     - | How to align the slow wave signals to display them on each other.
       | The default value is 'ZC'for Zero crossing.
       | Other values are 'PP ' for Positive Peak and 'NP' for Negative Peak.

Outputs
-------

This module has no outputs.

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Slow Wave Pics Generator** under the **Events Utilities** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.
