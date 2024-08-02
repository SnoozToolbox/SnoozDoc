.. _Compare_PSG_events:

===============================
Compare events from a PSG file
===============================

Description
-----------------

A tool to compare two sets of events, such as detections versus expert annotations, to evaluate the performance of a detector. 
This tool can also be used to evaluate the concordance between the scoring of two experts.

**Definition of the evaluation metrics**

Let's first define the variables :

   * The **event** from the expert : ``e``  
   * The **detection** : ``d``
   * True Positive (**TP**) : Correct detection (``e`` and ``d`` are the same).
   * False Positive (**FP**) : Incorrect detection (``d`` does not match any ``e``).
   * False negatives (**FN**) : Event missed (``e`` not detected)

Evalutation metrics :

   * **Precision** : ``TP/(TP+FP)`` : Fraction of detections that are correct
   * **Recall** : ``TP/(TP+FN)`` : Fraction of events found
   * **F1 score** = ``2 x (precision x recall)/(precision + recall)``
   * **kappa** = ``(2 * (tp*tn - fn*fp))/((tp + fp)*(fp + tn) + (tp + fn)*(fn + tn))``

      .. warning::

         kappa is considered a conservative agreement because the expected agreement is removed from the score.

Metrics are computed in the samples domain, therefore the list of events ``e`` and ``d`` are sampled at 100 Hz and the units of TP, TN, FP, FN are samples. 

i.e. TP-samples=500 means 500 samples from the expert events are correctly detected. 

* Pro : the performance evaluation is conservative (strict)
* Con : many shorter ``d`` can match a longer ``e`` without significant penalty, therefore not suited for event density.

Metrics are also computed in the events domain with the use of the Jaccord index. 

**Jaccord index** : ``(intersection between e and d) / (union of e and d)``

To considere a ``d`` as a TP, the jaccord index must exceed a certain threshold.
Only one ``d`` can match a ``e``, the one with the highest Jaccord index.

* Pro : Suited for event density.
* Con : Need to define a Jaccord index threshold.

Steps
-----------------

**1 - Input Files**

Start by opening your PSG files (.edf, .eeg or .sts).

* The .tsv file is also needed for the EDF format.

* The .sig file is also needed for Stellate format.

* The whole NATUS subject folder is also needed for the .eeg format.

**2 - Expert Annotation**
	
Select for each PSG file the expert events as gold standard.

**3 - Detection Event**
	
Select for each PSG file the detections to be compared against the expert events. 

**4 - Output Files**

Select the sleep stages to perform the comparison in. (I.e. N2 for sleep spindles.)

Define the jaccord index threhold to compute the performance evaluation. 

Jaccord index : ``(intersection between e and d) / (union of e and d)``

The output performance file is written in the same directory as the PSG file.
The output file is named as the PSG file with an additional suffix "_perf" and the extension .tsv.
One evaluation file per PSG file is generated.
