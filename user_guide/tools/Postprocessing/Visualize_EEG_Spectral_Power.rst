.. _Visualize_EEG_Spectral_Power:

=================================================
Visualize EEG Spectral Power
=================================================

Description
-----------------

This tool allows to generate images of spectral power of EEG signals, channels, and regions of interest (ROIs).
Besides, the user can generate images based on the preferred sleep stages, hour, cycle, and the total duration of the sleep.

Steps
-----------------

**1 - Input Files :**

	- Add your EEG spectral power report file (.tsv), which is generated from the :ref:`Power_Spectral_Analysis` tool.
	- Select the channels in "Channels of the subject" or "Channels of the cohort". The channel labels cannot be edited in this tool.

	- ROIs :
	    - Add ROIs and select them. 
	    - You can create ROIs to group channels with similar labels (e.g., C3-A2, C3-M2, C3) together.  
	    - You can choose to analyze either channels or ROIs, or both.
	    - Check "blank" to leave the ROI empty when data are missing for the mean, otherwise the missing data are ignored. The ROI is named ``ROI_`` followed by its channel labels, with ``_b`` at the end when "blank" is checked.

.. NOTE::

     To modify the channel names displayed on the plot, we recommend first using the ":ref:`PSA_Cohort_Review`" tool.
     Customize the names in the generated report, then use that report in this tool for visualization purposes.


**2 - Group Definition :**
	- Assign a group to each report file. Any group label is accepted.
	- The number of groups is unlimited.
	- At the cohort level, the report files with the same group label are put together.
	
	.. warning::

   	    If you need to analyze subjects from a single report in two distinct groups, please create two separate report files—one for each group.

**3 - Output Files :**
	- Define the parameters for generating the images. 
	- Images can be generated at either the **group level** or the **cohort level**.

		- Group Level: to generate images for each individual group.
			- One picture per group:
				All the selected channels or ROIs are illustrated on the same picture.
				
				Example of displaying all of the selected channels:
				
				.. image:: ./Visualize_EEG_Spectral_Power/Control_Group_avg_psa_Total_N2.png
				   :width: 500
				   :alt: Per group image
				
				Example of displaying mean and standard deviation of the selected channels:
				
				.. image:: ./Visualize_EEG_Spectral_Power/Control_Group_avg_psa_Total_N2_mean_std.png
				   :width: 500
				   :alt: Per group mean and SD image

			- One picture per channel or ROI per group:
				All the subjects in a group are illustrated on the same picture.

				Example of displaying all of the subjects for a specific channel:

				.. image:: ./Visualize_EEG_Spectral_Power/Control_Group_EEG_C3_psa_Total_N2.png
				   :width: 500
				   :alt: Per channel image

				Example of displaying mean and standard deviation of the subjects for a specific channel:

				.. image:: ./Visualize_EEG_Spectral_Power/Control_Group_EEG_C3_psa_Total_N2_mean_std.png
				   :width: 500
				   :alt: Per channel mean and SD image

		- Cohort Level: to generate pictures for the cohort.
			- One picture per cohort:
				PSA averaged across channels per group of subjects.
				Each PSA curve represents the signal averaged across all the selected channels or ROIs for a group of subjects.

				Example of displaying all of the subjects in a cohort:

				.. image:: ./Visualize_EEG_Spectral_Power/cohort_psa_all_Total.png
				   :width: 500
				   :alt: per cohort image

				Example of displaying mean and standard deviation of the subjects in a cohort:

				.. image:: ./Visualize_EEG_Spectral_Power/cohort_psa_mean_std_Total.png
				   :width: 500
				   :alt: per cohort mean and SD image

			- One picture per channel or ROI:
				PSA per channel per group of subjects.
				Each PSA curve represents the signal for a selected channel or ROI for a group of subjects.

				Example of displaying all of the subjects for a specific channel in a cohort:

				.. image:: ./Visualize_EEG_Spectral_Power/cohort_psa_all_Total_EEG_C3.png
				   :width: 500
				   :alt: per cohort per channel image

				Example of displaying mean and standard deviation of the subjects for a specific channel in a cohort:

				.. image:: ./Visualize_EEG_Spectral_Power/cohort_psa_mean_std_Total_EEG_C3.png
				   :width: 500
				   :alt: per cohort per channel mean and SD image

	- Select the preferred sleep stages, and the section to display ("Total", a sleep cycle, a clock hour or a stage hour). "All" plots the power of all the stages together. Some reports are computed on annotations instead of sleep stages (step "Section Selection" of the :ref:`Power_Spectral_Analysis` tool): for these reports, the annotations are plotted in place of the sleep stages, and the sleep stage selection is not used. A run cannot mix reports computed per sleep stage and reports computed on annotations. The section must be in the reports: check the distributions you need in the step "Output Files" of the :ref:`Power_Spectral_Analysis` tool.

	- Specify desired display options, such as plotting the mean and standard deviation EEG signal spectral power curve and setting axis limits.
	- In the optional settings "Colors", define the first four colors of the pictures (ten colors are available). With "Auto", the colors are blue, red, green, purple, orange, brown, pink, gray, olive and cyan. On every picture, the sleep stages are differentiated by the line style.

	- Select the output folder to save the images. The pictures are .pdf files, and existing pictures with the same names are replaced.
	- At the group level, a picture is named with the report file name, the channel or ROI label, the section and the stages, then ``_mean`` or ``_mean_std`` (for example ``learn-nsrr01_PSA_report_EEG_psa_Total_All_mean_std.pdf``); "One picture per group" adds ``avg``. At the cohort level, a picture is named ``cohort_psa``, then the display option and the section, and the channel or ROI label for one picture per channel (for example ``cohort_psa_mean_std_Total_EEG.pdf``).

Version History
-----------------

* v2.0.0 : Distributed with CEAMS package version 7.3.0 — Snooz beta 3.0.0
	- Initial release of the tool.

* v2.0.1 : Distributed with CEAMS package version 7.4.0 — Snooz 1.0.0
	- The title of the figures has been removed to allow more flexibility for the users.
	- Some parameter names have been changed internally to be clearer for developers, leading to an increase in the tool's version number.

* v2.1.1 : Distributed with CEAMS package version 7.5.0 — Snooz Toolbox 1.1.0
	- Added separate logarithmic scale options for the X axis (frequency) and the Y axis (power) in the Output Files step.
	- Added support for the per-annotation reports of the Power Spectral Analysis tool: the annotations are drawn in place of the sleep stages (sleep-stage and annotation reports cannot be mixed in one run).
	- Updated the forms to the new look of Snooz Toolbox 1.1.0 (Inter font, light and dark themes).

* v2.2.1 : Distributed with CEAMS package version 7.6.0 — Snooz Toolbox 1.2.0
	- Redesigned the pages and the step descriptions of the tool.
	- Corrected the Output Files page: the pictures are named with the report file name (not the PSG recording).
