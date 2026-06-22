.. _module_psapicsgenerator:

PSA Pics Generator
==================

**Module name:** ``PSAPicsGenerator``

**Package:** CEAMSModules 7.4.0

**Version:** 2.0.1

Overview
--------

* group-level plots (individual groups, single or all channels)
* Cohort-level plots (group averages with standard deviation bands)
* Support for multiple sleep stages, frequency ranges, and log/linear scales
* Automatic color expansion for scenarios with many recordings

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
   * - ``filenames``
     - dict
     - —
     - Keys are filenames. Each file contains a TSV file with PSA data.
   * - ``file_group``
     - dict
     - —
     - Keys are filenames. Values are the group label for cohort analysis.
   * - ``ROIs_def``
     - dict
     - —
     - | Keys are ROI names and values are [channels_list, blank_flag].
       | blank_flag=True requires all channels to be present.
   * - ``chans_ROIs_sel``
     - dict
     - —
     - Keys are channel labels or ROI names. Values are boolean selection flags.
   * - ``pics_param``
     - dict
     - True
     - | Plotting parameters with keys:
       | - 'cohort_avg', 'cohort_sel', 'group_avg', 'group_sel': bool flags for plot types
       | - 'display': str, display mode ('all', 'mean', 'mean_std')
       | - 'force_axis': bool or [xmin, xmax, ymin, ymax]
       | - 'output_folder': str, path to save figures
       | - 'freq_range': [float, float], frequency range to display
       | - 'log_scale': bool, use log scale for y-axis
       | - 'show_legend': bool, show legend on plots
       | - 'font': str, font family for all text
       | - 'fontsize': int, font size for axis labels and legend
       | - 'figure_width': float, figure width in inches
       | - 'figure_height': float, figure height in inches
       | - 'sleep_stage_selection': list of str, sleep stages to include
       | - 'activity_var': str, variable for activity ('total', 'clock_h', 'stage_h', 'cyc')
       | - 'hour': int, hour for 'clock_h' and 'stage_h' variables
       | - 'cycle': int, cycle for 'cyc' variable
   * - ``colors_param``
     - dict
     - —
     - | Color palettes for different plot types with keys:
       | - 'group_avg', 'group_sel', 'cohort': list of color strings

Outputs
-------

This module has no outputs.

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **PSA Pics Generator** under the **Events Utilities** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.
