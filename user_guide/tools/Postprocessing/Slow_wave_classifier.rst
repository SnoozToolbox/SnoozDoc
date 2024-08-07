.. _Slow_wave_classifier:

=================================================
Slow Wave Classifier
=================================================

Description
-----------------

This tool classifies slow waves into categories based on their transition frequency.

The classifier uses the files generated by the tool :ref:`Slow_wave_detection` : 

* **Slow Wave characteristics report** : Files with the signal characteristic of each slow wave event. One file per recording, one row per event.
* **Slow Wave cohort report**: A file with the slow wave characteristics averaged per subject.  One file for the cohort, one row per channel. (see :ref:`slow_wave_cohort_info_csv`)
* **Sleep stages files** : Files with the sleep stages selected for detection (listed as events).

.. warning::

   The option to generate the needed input files has to be checked by the user on step "4 - Output Files" in the :ref:`Slow_wave_detection` tool.

The slow wave characteristics files are copied and saved in the defined output directory, with the corresponding slow wave category appended.


Steps
-----------------

**1 - Input Files**

Add the slow wave characteristics report, the slow wave cohort report and the sleep stages files for your cohort. 

.. note::
   
   The slow wave characteristics files are saved in a directory at the cohort report level named "slow_waves_characteristics".
   
   The sleep stages files are saved in a directory at the cohort report level named "slow_wave_sleep_stages".

**2- Classification criteria**
	
Two options are avaible:

1. **An automatic classification**
   
Automatic classification using a gaussian mixture to fit the distribution of sleep slow waves transition frequency and checking the Akaire Information Criterion (AIC) of each model to select the gaussian distribution that fit's the best. 
In other words, the gaussian mixture distribution that has the lowest AIC value is the one that determines the number of sleep slow wave categories that are present in the dataset.

2. **A manual classification**
   
Specify the number of sleep slow waves categories to use.

.. note::
   
   Useful if the automatic classification doesn't analyse correctly the dataset or if you already know how many sleep slow wave categories there are in the set. 
   For example, you can select an automatic classification for a group data anlysis to find out the number of sleep slow wave categories you will apply to each individual if an individual analysis is needed.

**3 - Output Files**

Choose the destination folder for the output files.

The slow wave characteristics files are copied and saved in the output directory, with the corresponding slow wave category appended.

A cohort report containing the averaged slow wave characteristics per category is generated.

The slow wave characteristics are also provided per sleep cycle and segment of night.
Choose the granularity of the segment you are interested in. 

The histogram of transition frequency values along with the resulting model is saved in the output directory as a .pdf picture. 