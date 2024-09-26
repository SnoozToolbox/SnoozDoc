.. _module_howtos:

=================
How Tos - Module 
=================

To know what is the role of a module in Snooz, see :ref:`technical_overview`.

.. contents::
   :local:

Before creating your own module
==================================

- You need to have a properly configured development environment for Snooz. 
   - See :ref:`installation` for more details.
- Ensure that you have created your repository (e.g., my_snooz_repo) to manage your packages. 
   - See :ref:`run_snooz` for more details.
- You have already explored Snooz and have an understanding of its structure. 
   - See :ref:`explore_ex` for more details. 

How to create a module
==================================
We use a command line tool to help create new modules. To access the terminal in VS Code, make sure to close Snooz beforehand. 

- In VS Code navigate to **Terminal -> New Terminal**
- Select your repository you forked from snooz_package_template (e.g. my_snooz_repo)
- Make sure the virtual environment **snooz_310_env** is activated (see :ref:`installation`)
- In the terminal type : ``python main_utils.py``
- Select **2- Create a module**
- Fill the information to suit your design. If you make any mistakes, just repeat the steps and it will ask to overwrite the previous one.  If you need more information, see :ref:`info_modules`.

As the message in the console mentions, there's a final step before you can use the module in a process. 
You need to generate the python files associated with the two .ui files of the module. 

In VS Code:

1. Find the new subfolder of your module in your package.
2. Right-click on file **Ui_[MODULE]ResultsView.ui**
3. Select **Compile Qt UI file**.
4. Repeat the process for the file **Ui_[MODULE]SettingsView.ui**

How to update a module
==================================
To modify the behavior of a module, you can modify the compute function and adjust the module version according to these :ref:`Versioning Guidelines<versioning>`. 

To modify the inputs and outputs of a module, you need to update a few files. For a list of files included in the module structure, see  :ref:`info_modules`.

JSON file
-------------------------

The JSON file contains all the information related to a module—its name, label, category, inputs, outputs, etc. This is used by Snooz to know what to expect from the module.

Each input or output of the module is defined by a dictionnary as shown below : 

- **name** : The name of the input/output
- **value** : The default value of the input (ignored for outputs).
- **connections** : This is only ever filled when a module is part of a process, you can ignore it.
- **sub_plugs** : This is not use yet, you can ignore it.

To add or remove an input/output, simply add or remove a key-value pair from the ``inputs`` or ``outputs`` dictionary.

For an example of a JSON file, see :ref:`module_json_file`.

Module python file
-------------------------

The main module python file (referred :ref:`here<info_modules>` as [MODULE].py) contains the compute function and interacts with the inputs/outputs of the module.  
To update the inputs/outputs properly you need to update 3 sections:

   1. The init function
   2. The compute function parameters
   3. The code of the compute function

1. The init function

In the init function, you'll have to remove/add the calls to the InputPlug/OutputPlug functions. 
These function calls are used to register the inputs and outputs to the engine that runs the process.

For example, let's remove the ``signal_1`` input and add an output called ``statistics``.

.. code-block:: python

   def __init__(self, **kwargs):
         """ Initialize ModuleA """
         super().__init__(**kwargs)
         if DEBUG: print('ModuleA.__init__')

         # Input plugs
         InputPlug('signal_1',self) # REMOVE THIS LINE
         InputPlug('signal_2',self)
         
         # Output plugs
         OutputPlug('signal',self)
         OutputPlug('statistics',self) # ADD THIS LINE

2. The compute function parameters

To update the compute function, add or remove the necessary parameters. The compute function of the class is called when the module is executed within a process. 
The parameters should match exactly (and be in the same order) as the inputs defined in the JSON file and registered in the init function.

For example, let's remove the input called ``signal_1`` and add an output called ``statistics``.

Change this:

.. code-block:: python

   def compute(self, signal_1,signal_2):
      ...
      return {'signal': output_signal}

To this:

.. code-block:: python

   def compute(self, signal_2):
      ...
      return {
         'signal': output_signal,
         'statitics': some_stats # ADD THIS KEY/VALUE PAIR
         }

3. The code of the compute function

Ensure that you remove any code that references the removed parameter and add the necessary code to handle the new parameter within the compute function.

Settings View
-------------------------

The Settings View is a user interface displayed in the **Settings** tab when the user double-clicks on a module in the process view.
This same view may also be used in the step-by-step interface of a tool. Modifying this settings view will also impact those tools.

Three files are involved:

- Ui_[MODULE]SettingsView.ui : An XML description of the UI, edited using Qt Designer.
- Ui_[MODULE]SettingsView.py : The python file generated from Ui_SettingsView.ui.
- [MODULE]SettingsView.py : The python file that links the Settings View UI to the module inputs.

**Add or remove an input**

Follow these guidelines depending on whether the input parameter is displayed in the Settings View UI:

- **To add a new input** : Add the input parameter in the UI if it is user-editable.
- **To remove an input** : Remove the input parameter from the UI if it was previously present. 

The modifications to the UI are as follows:

- Edit Ui_SettingsView.ui using Qt Designer.
- Save the changes.
- Compile the Ui_SettingsView.py file.

Handling the input parameter from the SettingsView.py :

- Add or remove the subscription in the constructor.
- Add or remove the call to the publisher in the ``on_apply_settings`` function.
- Add or remove the ping in the ``load_settings`` function.
- Add or remove the response to the ping in the ``on_topic_response`` function.

Modifying an output does not affect the Settings View.

For more details about the Settings View, see :ref:`SettingsView Info<module_SettingsView_file>` and :ref:`howto_settingsView`.

Results View
-------------------------

The Results View is a user interface displayed in the **Results** tab when the user double-clicks on a module in the process view.

Three files are involved:

- Ui_[MODULE]ResultsView.ui : An XML description of the UI, edited using Qt Designer.
- Ui_[MODULE]ResultsView.py : The python file generated from Ui_ResultsView.ui.
- [MODULE]ResultsView.py : The python file that links the Results View UI to the module cache.

Modifying an ouput that was displayed in the Results View has to be handled. See :ref:`howto_resultsView` for more details.

.. _howto_settingsView:

How to design the settings tab
====================================================================
TODO

.. _howto_resultsView:

How to design the results tab
====================================================================
TODO

How to use the cache to show information inside the result tab
====================================================================
TODO

How to add an option to a module
====================================================================
TODO

How to change the state of a module
====================================================================
TODO

How to add a resource to a module
====================================================================
TODO

How to show information in the log tab
====================================================================
TODO

How to generate a runtime exception in a module
====================================================================
TODO

How to run a process over multiple files
====================================================================
TODO

More information about the modules
====================================================================
