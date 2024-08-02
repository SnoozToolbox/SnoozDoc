.. _Sleep_Bouts:

===============================
Sleep Bouts
===============================

Description
-----------------

This tool detects and reports continuous periods of sleep stages. 

This tool detects three **types** of sleep bouts:

   1. Continuous period of N2 and N3 stages
   2. Continuous period of N2, N3 and REM stages
   3. Continuous period of REM stage

Steps
-----------------

**1 - Input Files**

Start by opening your PSG files (.edf, .eeg or .sts).

* The .tsv file is also needed for the EDF format.

* The .sig file is also needed for Stellate format.

* The whole NATUS subject folder is also needed for the .eeg format.

**2 - Output Files**
    
The output is a CSV (Comma separated Values) file. 
A new row is added for every file analyzed. 

The columns of the file are as follows:

* The name of the PSG file
  
* The ten longest sleep bouts of type 1
  
* The mean value of all sleep bouts of type 1
  
* The standard deviation value of all sleep bouts of type 1

Repeat for type 2 and 3.

