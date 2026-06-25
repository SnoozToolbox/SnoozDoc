.. _module_filtersignal:

Filter Signal
=============

**Module name:** ``FilterSignal``

**Package:** CEAMSModules 7.5.0

**Version:** 2.1.0

Overview
--------

This plugin applies a FIR/IIR filter to EEG signals.

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
     - list of SignalModel
     - None
     - list of SignalModel to filter
   * - ``type``
     - 'bandpass', 'lowpass', 'highpass', 'bandstop'
     - bandpass
     - Configuration value for type.
   * - ``IR_family``
     - 'IIR', 'FIR'
     - IIR
     - Configuration value for IR family.
   * - ``use_std_order``
     - bool or str
     - False
     - | If True, the order is calculated based on the
       | formula: order=5*(sample_rate/lower frequency)
       | If False, the order is taken from the [order]
       | parameter.
   * - ``order``
     - int or str
     - 6
     - Filter order
   * - ``cutoff``
     - float or str
     - 0.3, 64
     - | Cutoff frequency, must be an increasing value
       | between 0 and sample_rate/2
   * - ``window``
     - str
     - hamming
     - | Desired window ex: 'hamming'
       | -- see: https://docs.scipy.org/doc/scipy/reference/generated/ for all options.

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
   * - ``signals``
     - list of SignalModel
     - Filtered signals

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Filter Signal** under the **Signal Processing** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.
