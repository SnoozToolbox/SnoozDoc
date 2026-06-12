.. _module_movingrms:

Moving RMS
==========

**Module name:** ``MovingRMS``

**Package:** CEAMSModules 7.4.0

**Version:** 2.0.0

Overview
--------

Compute RMS (Root Mean Squared) value on a moving window.

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
   * - ``signals``
     - a list of SignalModel
     - —
     - | signal.samples : The actual signal data as numpy list
       | signal.sample_rate : the original sampling rate of the signal
       | signal.channel : current channel label
   * - ``win_len_sec``
     - float
     - 1
     - window length in sec (how much data is taken for each RMS computation)
   * - ``win_step_sec``
     - float
     - 1
     - window step in sec (each time the RMS computation is applied)

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
   * - ``moving_RMS_values``
     - dict of SignalModel object, the key is the label of the channel.
     - moving_RMS_values[channel_label].samples: One RMS value per moving window as numpy array.

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Moving RMS** under the **Signal Processing** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.
