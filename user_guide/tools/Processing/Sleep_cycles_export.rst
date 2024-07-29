.. _Sleep_cycles_export:

===============================
Sleep cycles
===============================

Description
-----------------

This tool computes and report the sleep cycles. 

Sleep cycles typically last around 90 minutes to 2 hours, during which time the brain cycles from slow-wave sleep to REM sleep.  Sleep cycles are succession of NREM-REMs periods.  

**Simple definition of NREM Period (NREMP)**

* First NREMP : begins at the first NREM stage of the recording.
* Central NREMPs : begin at the next NREM stage following a REMP end.
* The NREMP ends at the start of a REMP.

**REM Period (REMP)**

* The REMP ends when there are 15 min without an R stage (except at the last cycle).
* The end is defined as the last R stage of the REMP or the beginning of the next NREMP.
* The REMP begins at the first stage R.


Steps
-----------------

**1 - Input Files**

Start by opening your PSG files (.edf, .eeg or .sts).

* The .tsv file is also needed for the EDF format.

* The .sig file is also needed for Stellate format.

* The whole NATUS subject folder is also needed for the .eeg format.

**2 - Cycle Definition**

Select or edit your sleep cycle criteria.

**3 - Output Files**

Sleep Cycle Cohort file : 

* The start and duration (s) of each NREM and REM period are saved in a .tsv (tab separated values) file defined by the user.
* The file includes 5 columns : group, name, start_sec, duration_sec and channels.
* Each row corresponds to a period and the group identifies the PSG recording.  
* New PSG recording are added in the .tsv file if it exists otherwise it is created.

Sleep Cycle specific to each PSG opened: 

* The hypnogram of each PSG is saved in a .png picture file
* The sleep stages and sleep periods events are saved in a .tsv file 

