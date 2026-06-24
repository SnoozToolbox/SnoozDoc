.. _module_icacomponents:

Ica Components
==============

**Module name:** ``IcaComponents``

**Package:** CEAMSModules 7.5.0

**Version:** 2.0.0

Overview
--------

Finds components of a signal with independent component analysis.

Taken from `_fastica.py <https://github.com/scikit-learn/scikit-learn/blob/main/sklearn/decomposition/_fastica.py>`_.
Read more in the `FastICA documentation <https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html>`_.


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
     - List
     - —
     - | List of signal with dictionary of channels with SignalModel with
       | properties :
       | name: The name of the channel
       | samples: The samples of the signal
       | alias: The alias of the channel
       | sample_rate: The sample rate of the signal
       | start_time: The start time of the recording
       | montage_index: The index of the montage used for this signal
       | is_modified: Value caracterizing if the signal as been modify
       | from the original
       | parameters : dict
       | parameters to decompose the signal.
       | ICA_algo : string ('infomax' or 'fastICA')
       | n_components : int, default=None
   * - ``parameters``
     - dict
     - Came in the description column    
     - | Parameters to decompose the signal.
       | {'ICA_algo': 'infomax' or 'fastICA',
       | 'n_components': None,
       | 'algorithm': 'parallel',
       | 'whiten': 'arbitrary-variance',
       | 'fun': 'logcosh',
       | 'max_iter': 1000,
       | 'tol': 0.0001,
       | 'random_state': None}


Parameters
----------

.. list-table::
   :widths: 25 20 15 50
   :header-rows: 1
   :align: left
   :class: left-align-caption wrap-table

   * - Parameter
     - Format
     - Default
     - Description
   * - ``ICA_algo``
     - string
     - 'infomax' or 'fastICA'
     - The algorithm to use for the ICA.
   * - ``n_components``
     - int
     - None
     - The number of components to extract. If None, all components are extracted.
   * - ``algorithm``
     - string
     - 'parallel'
     - The algorithm to use for the ICA.
   * - ``whiten``
     - string or bool
     - 'arbitrary-variance'
     - The whitening strategy to use.
   * - ``fun``
     - string
     - 'logcosh'
     - The functional form of the G function used in the approximation to neg-entropy.
   * - ``fun_args``
     - dict
     - None
     - Arguments to send to the functional form. If None, the default arguments are used.
   * - ``max_iter``
     - int
     - 200
     - The maximum number of iterations during fit.
   * - ``tol``
     - float
     - 0.0001
     - The tolerance on update at each iteration.
   * - ``w_init``
     - ndarray of shape (n_components, n_components)
     - None
     - The mixing matrix to be used to initialize the algorithm. If None, a random matrix is used.
   * - ``random_state``
     - int
     - None
     - Used to initialize ``w_init`` when not specified, with a normal distribution.

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
   * - ``components``
     - List
     - List of signal_models obtain after the decomposition

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Ica Components** under the **Signal Processing** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.
