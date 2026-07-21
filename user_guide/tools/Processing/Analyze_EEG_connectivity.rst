.. _Analyze_EEG_connectivity:

======================================
Analyze EEG Functional Connectivity
======================================

Description
-----------------------

The **Analyze EEG Functional Connectivity** module computes both functional and directional brain connectivity using three established EEG measures:

- **wPLI (Weighted Phase Lag Index)**: estimates non-zero-lag phase synchronization, minimizing volume conduction artifacts.
- **dPLI (Directed Phase Lag Index)**: estimates the direction of phase-lead/lag between pairs of EEG channels.
- **AEC (Amplitude Envelope Correlation)**: estimates coupling between amplitude envelopes of band-limited EEG signals. Signals are orthogonalized before envelope extraction to reduce spurious connectivity from volume conduction (leakage).

For wPLI and dPLI, the tool automatically applies statistical correction using surrogate data testing and Wilcoxon signed-rank tests to retain only significant connections. AEC does not use surrogate testing; leakage correction is used instead. The tool requires at least two clean brain channels and two valid epochs to run.

.. note::
   For optimal results, it is strongly recommended to preprocess your data using the **EEGInspector** app in Snooz. This allows you to mark and exclude:
   - Non-brain channels (e.g., EOG, EMG, ECG)
   - Noisy/bad channels
   - Noisy epochs

----

Steps
-----------------

**1 - Input Files**

   Start by opening your PSG files (.edf, .eeg or .sts).

   * The .tsv file is also needed for the EDF format.
   * The .sig file is also needed for Stellate format.
   * The whole NATUS subject folder is also needed for the .eeg format.

**2 - Events Exclusion**

   Use previously saved artifact annotations (e.g., from EEGInspector, Snooz artifact detection tool) to exclude noisy data from connectivity calculations.

.. important::

   Connectivity cannot be performed on:
   - Fewer than 2 channels
   - Fewer than 2 valid epochs

**3 - Filtering**

- **Frequency Band Selection**:  
  Choose a predefined band (Delta, Theta, Alpha, Beta, Full) or define a custom band to match your research question.

- **Recording Scope Selection**:  
  Select Sleep Stages to analyze specific stages, Unscored to analyze the full recording or a chosen time segment, or Specific Annotations to base the analysis on event markers.


**4 - Annotation Selection**
  Select specific annotations/events to perform connectivity analysis on. You can choose multiple annotations if needed.

**5 - Connectivity Configuration**

- **Connectivity Type**:  
  Choose between wPLI, dPLI, or AEC.

- **Epoch Parameters** (all methods):
  - Epoch length (seconds)
  - Epoch overlap (seconds)

- **Statistical testing** (wPLI and dPLI only; these controls are disabled for AEC):
  - Number of surrogates (for statistical testing)
  - P-value threshold (to retain only significant connections)

  Statistical testing ensures connections are not due to chance and provides more reliable connectivity estimates.

- **Network Properties Settings** (wPLI only; this section is disabled for dPLI and AEC):

  When wPLI is selected and at least 32 channels are used, the tool computes graph metrics from the wPLI connectivity matrices to characterize network efficiency, integration, segregation, and small-world organization.

  - **Minimally spanning tree** (recommended): finds the smallest threshold that keeps the network fully connected.
  - **Custom threshold**: retains the top X fraction of strongest edges (value between 0 and 1).

**6 - Output Files**

All files are saved in the selected Output folder, or next to the input file if "Save in the same folder" is checked.

Output files include:

- **Connectivity Matrix** (TSV)
  - File: ``<Filename>_{wpli|dpli|aec}_convalue.tsv``

- **Connectivity Heatmap** (PNG)
  - File: ``<Filename>_{wpli|dpli|aec}_conheatmap.png``
  - Visual matrix of the TSV data.

- **Head Connectivity Plot** (PNG, optional)
  - File: ``<Filename>_{wpli|dpli|aec}_contopomap.png``
  - Saved only if a montage with ≥ 4 EEG channels is found.

- **Network Properties** (TSV, wPLI only, ≥ 32 channels)
  - File: ``<Filename>_wpli_net_properties_results.tsv``
  - Per-window values of characteristic path length, clustering coefficient, global efficiency, small-worldness, modularity, and mean participation coefficient. If minimally spanning tree mode is used, the selected threshold per window is also included.

- **Participation Coefficients** (TSV, wPLI only, ≥ 32 channels)
  - File: ``<Filename>_wpli_participation_coefficient_results.tsv``
  - Per-window participation coefficient for each individual channel.

.. note::

   Network Properties and Participation Coefficient files are generated only when **wPLI** is selected and at least **32** channels are used. With fewer channels, connectivity outputs are still produced, but network-property TSVs are skipped.

Connectivity value ranges

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Measure
     - Range and interpretation
   * - wPLI
     - 0 to 1 (0 = no phase coupling; 1 = strong coupling)
   * - dPLI
     - 0 to 1 (0.5 = neutral; > 0.5 = leads; < 0.5 = lags)
   * - AEC
     - 0 to 1 (0 = no amplitude envelope correlation; 1 = strong coupling)

Head connectivity plot elements

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Element
     - Description
   * - Nodes
     - EEG channels (connected = filled black; unconnected = white)
   * - Edges
     - wPLI & AEC: single color (darker means stronger); dPLI: gradient red -> purple -> blue (red = leader, blue = lagger)
   * - Styling
     - Edge thickness and opacity scale with connection strength


**Montage Handling**

- Montage is automatically selected from MNE built-ins.
- For HydroCel 128/129, face/neck sensors are removed to clean up the layout.

----

Display Thresholds
----------------------

Default thresholds for plotting:

**wPLI:**

- neutral_min = 0.05 (ignore below)
- moderate_min = 0.10 (thin & faint)
- strong_min = 0.20 (thick & dark)
- max_val = 0.40 (for opacity scaling)

**dPLI (bias = dPLI − 0.5):**

- neutral_abs = 0.01 (ignore below)
- moderate_abs = 0.02 (thin & faint)
- strong_abs = 0.08 (thick & dark)
- max_abs = 0.25 (for opacity scaling)

**AEC:**

- neutral_min = 0.10 (ignore below)
- moderate_min = 0.20 (thin & faint)
- strong_min = 0.35 (thick & dark)
- max_val = 0.60 (for opacity scaling)

----

References
-----------------

[1] Stam, C. J., & van Straaten, E. C. W. (2012). Go with the flow: Use of a directed phase lag index (dPLI) to characterize patterns of phase relations in a large-scale model of brain dynamics. NeuroImage, 62(3), 1415–1428. https://doi.org/10.1016/j.neuroimage.2012.05.050

[2] Vinck, M., Oostenveld, R., van Wingerden, M., Battaglia, F., & Pennartz, C. M. (2011). An improved index of phase-synchronization for electrophysiological data in the presence of volume-conduction, noise and sample-size bias. NeuroImage, 55(4), 1548–1565. https://doi.org/10.1016/j.neuroimage.2011.01.055

[3] Hipp, J. F., Hawellek, D. J., Corbetta, M., Siegel, M., & Engel, A. K. (2012). Large-scale cortical correlation structure of spontaneous oscillatory activity. Nature Neuroscience, 15(6), 884–890. https://doi.org/10.1038/nn.3101

[4] Duclos, C., Maschke, C., Mahdid, Y., Nadin, D., Rokos, A., Arbour, C., Badawy, M., Létourneau, J., Owen, A. M., Plourde, G., & Blain-Moraes, S. (2023). Brain responses to propofol in advance of recovery from coma and disorders of consciousness: A preliminary study. American Journal of Respiratory and Critical Care Medicine, 207(5), 602–613. https://doi.org/10.1164/rccm.202105-1223OC

[5] Rubinov, M., & Sporns, O. (2010). Complex network measures of brain connectivity: Uses and interpretations. NeuroImage, 52(3), 1059–1072. https://doi.org/10.1016/j.neuroimage.2009.10.003


Version History
-----------------

* v2.3.0 : Distributed with CEAMS package version 7.3.0 — Snooz beta 3.0.0
    - Initial release of the tool.
* v2.5.0 : Distributed with CEAMS package version 7.4.0 — Snooz 1.0.0
    - Renamed to "Analyze EEG Functional Connectivity" for clarity.
    - Add error handling workflow for PSG loading from workspaces and display failed files in the UI.
    - Add error handling workflow for duplicated sleep stages.
* v2.6.0 : Distributed with CEAMS package version 7.5.0 — Snooz 1.1.0
    - Add Amplitude Envelope Correlation (AEC) connectivity method with leakage correction.
    - Add Network Properties analysis for wPLI (requires ≥ 32 channels), with minimally spanning tree or custom threshold.
    - Add network properties and participation coefficient TSV outputs.
