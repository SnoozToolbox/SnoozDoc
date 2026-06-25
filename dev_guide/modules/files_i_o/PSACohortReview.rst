.. _module_psacohortreview:

PSA Cohort Review
=================

**Module name:** ``PSACohortReview``

**Package:** CEAMSModules 7.4.0

**Version:** 2.5.0

Overview
--------

Class to read the PSA output file generated from Tool-> Sleep analysis -> PSA and generate the PSA file clean or transposed.

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
     - List of String
     - []
     - List of filename (including path) to the PSA output file.
   * - ``subject_chans_label``
     - dict
     - {}
     - | Keys are the subjects
       | Each item is a list of 3 elements [original chan label, modified chan label, bool selection flag]
   * - ``ROIs_cohort``
     - dict
     - {}
     - | Dict to manage the ROI created at the cohort level
       | keys are ROIs labels
       | Each item is a list of 2 elements [channel list to average, blank flag]
   * - ``ROIs_subjects``
     - dict
     - {}
     - | Dict to manage the ROI at the subject level
       | keys are the subjects
       | Each item is a list of n_ROIs with its selection label [ROI#1 label, bool selection flag]
       | [ROI#2 label, bool selection flag]
       | ...
   * - ``freq_band``
     - pandas DataFrame
     - —
     - frequency bands to average, columns=['num-start(Hz)','num-end(Hz)','den-start(Hz)','den-end(Hz)']))
   * - ``activity_label``
     - string
     - Total
     - The activity variable to export/save i.e. 'Total', 'distribution per clock hour', 'distribution per hour spent in each sleep stage' or 'distribution per sleep cycle'.
   * - ``PSA_clean_flag``
     - bool
     - 0
     - Flag to generate and save the PSA file with only selected channels.
   * - ``PSA_transposed_flag``
     - bool
     - 1
     - Flag to generate and save the transposed PSA file (1 subject per row)
   * - ``output_dir``
     - string
     - —
     - Output path to save the PSA file clean and/or transposed.

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
   * - ``out_df``
     - pandas DataFrame
     - PSA data converted into a dataframe with modifications applied.

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **PSA Cohort Review** under the **Files I/O** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.
