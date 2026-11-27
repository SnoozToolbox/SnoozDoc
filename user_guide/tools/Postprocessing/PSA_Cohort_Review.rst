.. _PSA_Cohort_Review:

=================================================
Review EEG Spectral Power for the cohort
=================================================

A tool to explore, clean (such as removing bad channels or renaming channels), and transpose the EEG spectral power report in order to have 1 subject per row.

The EEG spectral power report is written by the :ref:`Power_Spectral_Analysis` tool in Snooz, with one row per recording, channel and frequency bin.

.. note::

   Run :ref:`Power_Spectral_Analysis` with the distributions you need checked in its step "Output Files" ("Total", "Distribution per hour", "Distribution per sleep cycle"). This tool exports only the distributions found in the report.

The clean report has the same variable names as the input report.
In the transposed report, the channel label and the frequency band are added to the variable name as a suffix, with ``abs`` for the absolute power or ``rel`` for the relative power.

.. note::

   * ``total_act`` becomes ``total_act_abs_EEG F3-RC_1_4`` for the channel ``EEG F3-RC`` and the absolute power in the frequency band 1-4 Hz.
   * ``total_act`` becomes ``total_act_rel_EEG F3-RC_1_4`` for the channel ``EEG F3-RC`` and the relative power in the frequency band 1-4 Hz.

Steps
-----------------

**1 - Input Files**

*EEG spectral power reports*

Add the EEG spectral power reports written by the :ref:`Power_Spectral_Analysis` tool. You can add more than one report.
Each recording of the reports is a subject of "Subjects".

*Channel labels*

Double-click a channel label to edit it. You can edit it at the subject level, in "Channels of the subject", or at the cohort level, in "Channels of the cohort". A label edited at the cohort level changes for all the subjects loaded.
Uncheck a channel to remove it.

*Regions of interest*

You can add a region of interest (ROI) at the cohort level to average several channels together. Click "Add ROI", then check the channels to include in the ROI (the list holds the channels of the cohort loaded).
Check "blank" to leave the ROI empty when data are missing for the mean. Otherwise the missing data are ignored.
The ROI is named ``ROI_`` followed by its channel labels, with ``_b`` at the end when "blank" is checked (for example, ``ROI_C3C4`` for the channels C3 and C4).

.. warning::

   Rename your channel labels first. Adding the ROIs must be the final step.

**2 - Frequency Band**

You can add a new band with the button "Add" or load an existing file with the button "Load". You can edit the bands loaded (double-click a cell). The values must be within the frequency bins available, so add the reports in step 1 first.
"Remove" removes the selected band. "Save" saves the bands you edited in a .tsv file, which "Load" can read later.

The spectral power can be absolute or relative.

- For absolute power, fill only the numerator of the band, "num-start(Hz)" and "num-end(Hz)". Leave "den-start(Hz)" and "den-end(Hz)" as nan (not a number).
- For relative power, fill the numerator and the denominator of the band. The relative power is the power of the numerator band divided by the power of the denominator band, in percent. For example, 1-4 Hz over 0.5-32 Hz gives the power from 1 to 4 Hz as a percentage of the power from 0.5 to 32 Hz.

A band includes its low frequency bin and excludes its high one, [low, high[, so the power of a frequency bin is never averaged twice in two adjacent bands.
For example, with bins of 0.5 Hz, the band 1-4 Hz holds the 6 bins that start at 1, 1.5, 2, 2.5, 3 and 3.5 Hz.
Use band limits that are limits of the frequency bins: a band whose bins are not all in a report is left empty for that channel.

**3 - Output File**

Check the reports you want to generate:

   * the clean report, with the selected channels only and their edited labels, in the same format as the input reports;
   * the transposed report, with one subject per row and the selected channels (ROIs included) and frequency bands as additional columns.

To export the transposed report, choose the activity variables, that is how to average the spectral power across the recording:

    * **Total** to output the average through the whole recording.
    * **Distribution per clock hour** to output the average per real clock hour, from hour 1 to 9 by default.
    * **Distribution per hour spent in each sleep stage** to output the average per stage when it reaches an hour, from hour 1 to 9 by default.
    * **Distribution per sleep cycle** to output the average per sleep cycle, from sleep cycle 1 to 6 by default.

Only the choices found in the report are listed. For a report of the analysis per annotation, the averages are given for each annotation, and **Distribution per hour spent in each sleep stage** is not available.

The maximum number of hours and sleep cycles, and the starting point (either the first sleep stage or the sleep onset) are defined when running the :ref:`Power_Spectral_Analysis` tool.

Define the filename to save the exported files. The suffix _clean or _transposed is added to the filename, and the files are .tsv (tab separated values) files: for example, ``cohort.tsv`` gives ``cohort_clean.tsv`` and ``cohort_transposed.tsv``.

.. Warning::

   The output files are replaced if they already exist.


Version History
-----------------

* v2.0.0 : Distributed with CEAMS package version 7.2.0 — Snooz beta 2.0.1
    - Initial release of the tool.

* v2.4.0 : Distributed with CEAMS package version 7.3.0 — Snooz beta 3.0.0
    - Update UI to support elapsed clock time and sleep-stage time.

* v2.5.0 : Distributed with CEAMS package version 7.4.0 — Snooz 1.0.0
   - Show subjects without selected channel or ROI and let users skip them during analysis.

* v2.6.1 : Distributed with CEAMS package version 7.5.0 — Snooz Toolbox 1.1.0
   - Adapted to the per-annotation reports of the Power Spectral Analysis tool, which now have the same distributions as the per-stage reports (total, per clock hour, per sleep cycle); the "Distribution per annotation" option was removed.
   - Updated the forms to the new look of Snooz Toolbox 1.1.0 (Inter font, light and dark themes).

* v2.6.2 : Distributed with CEAMS package version 7.6.0 — Snooz Toolbox 1.2.0
   - Redesigned the pages and the step descriptions of the tool.
   - Corrected the example of the variable names of the transposed report (``total_act``), the name of step 3 (Output File), and the output files, which are replaced (not appended).
