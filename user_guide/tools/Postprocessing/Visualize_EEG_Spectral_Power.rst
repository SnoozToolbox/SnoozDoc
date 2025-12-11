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
	- Select the channels in the "Subject Channel List" or "Cohort Channel List".

	- ROIs :
	    - Add ROIs and select them. 
	    - You can create ROIs to group channels with similar labels (e.g., C3-A2, C3-M2, C3) together.  
	    - You can choose to analyze either channels or ROIs, or both.

.. NOTE::

     To modify the channel names displayed on the plot, we recommend first using the ":ref:`PSA_Cohort_Review`" tool.
     Customize the names in the generated report, then use that report in this tool for visualization purposes.


**2 - Group Definition :**
	- Assign a cohort group to each report file.  Any cohort group label is accepted.  
	- The number of cohort groups is unlimited.
	
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

	- Select the prefered sleep stages, and section to display the EEG spectral power images.

	- Specify desired display options, such as plotting the mean and standard deviation EEG signal spectral power curve and setting axis limits. (For more options look at the "Colors" settings page in the left panel).

	- Select the output folder to save the images.

Version History
-----------------

* v2.0.0 : Distributed with CEAMS package version 7.3.0 — Snooz beta 2.1.0
    - Initial release of the tool.