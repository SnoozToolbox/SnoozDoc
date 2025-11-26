.. _PSAImages:

=================================================
Visualize EEG Spectral Power
=================================================

This tool allows you to visualize the EEG spectral power for specific signals, channels and region of interestes (ROIs).
Besides, the user can generate images based on the prefered sleep stages, hour, cycle, or the total duration of the sleep.

Steps
-----------------

**1 - Input Files :**

	- Add your EEG spectral power report (.tsv), which is generated from the :ref:`Power_Spectral_Analysis`.
	- Select the channels in the **Subject Channel List** or **Cohort Channel List**.

	- ROIs :
	    - Add ROIs and select them. 
	    - You can create ROIs to group channels with similar labels (e.g., C3-A2, C3-M2, C3) together.  
	    - You can choose to analyze either channels or ROIs, or both.

.. NOTE::

     To modify the channel names displayed on the plot, we recommend first using the :ref:`PSA_Cohort_Review` tool. Once the channel names are customized, use the generated clean report as input to this tool for visualization.


**2 - Group Definition :**
	- Assign a condition group to each report file.  Any condition group label is accepted.  
	- The number of condition groups is unlimited.

**3 - Output Files :**
	- Define the parameters for generating the images. 
	- Images can be generated at either the subject level or the cohort level, or both.

	- You have the option to generate individual pictures 
	- for each channel/ROI or combine them into a single picture.
	
	- Select the prefered sleep stages, and section to display the PSA images.

	- Specify desired display options, such as plotting the mean PSA signal curve and setting axis limits. (For more options look at the "Colors" settings page in the left panel).

	- Select the output folder to save the images.


Example of the Generated Images
---------------------------------

.. image:: ./PSA_Images/Picture_Cohort.png
   :width: 500
   :alt: Cohort level image

.. image:: ./PSA_Images/Picture_per_channel.png
   :width: 500
   :alt: Per channel image

.. image:: ./PSA_Images/Picture_per_report.png
   :width: 500
   :alt: Per report image

