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
To modify the behavior of a module, you can modify the ``compute()`` function and adjust the module version according to these :ref:`Versioning Guidelines<versioning>`. 

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

The main module python file (referred :ref:`here<info_modules>` as [MODULE].py) contains the ``compute()`` function and interacts with the inputs/outputs of the module.  
To update the inputs/outputs properly you need to update 3 sections:

   1. The init function
   2. The ``compute()`` function parameters
   3. The code of the ``compute()`` function

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

To update the ``compute()`` function, add or remove the necessary parameters. The ``compute()`` function of the class is called when the module is executed within a process. 
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

3. The code of the ``compute()`` function

Ensure that you remove any code that references the removed parameter and add the necessary code to handle the new parameter within the ``compute()`` function.

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

How to handle exceptions
====================================================================
In Snooz, when a module is executing we define two types of possible problems: 

- input problems
- runtime problems
 
The module is responsible for detecting these problems and raise the appropriate exception when they happens. 

NodeInputException
---------------------
An input problem occurs when an input module is not of the expected type. When this happens, the module must raise a ``NodeInputException``. 
A ``NodeInputException`` is considered a critical error and will stop the execution of Snooz.

This error typically occurs during the development phase, when the process has not yet been fully validated. 
It may result from an input parameter being poorly defined or modules in the process not being properly connected.

Once the process is integrated into a tool, any user-editable parameters should be validated before execution begins.

The best practice is to verify the type of the input parameters at the start of the ``compute()`` function in your module.

.. code-block:: python
   
   def compute(self, signal_1):
      # Make appropriate checks to input values
      if not isinstance(signal_1, dict):
         raise NodeInputException(self.identifier, "signal_1", "signal_1 must be a dictionary")

.. note::

   self.identifier informs which instance of a module is responsible for generating the exception, this is useful when you have multiple instances of the same module inside a process.

NodeRuntimeException
---------------------
A runtime exception occurs when there is a problem during the execution of the ``compute()`` function, 
after the initial checks for input validity have passed. When this happens, the module must raise a ``NodeRuntimeException``.

A runtime exception is not considered as critical as ``NodeInputException``, since the error can be caused by the content being analyzed rather than the developer's code. 
If the process is set up to run on multiple files (using a master node), only the current iteration will fail, and the process will continue with the next iteration. 
At the end of all iterations, the user will be informed that an error occurred during one or more iterations.

Here are a few examples where your module should raise a ``NodeRuntimeException``:

- A file you are trying to open is locked by another software and cannot be accessed.
- The file you are trying to read is empty or improperly formatted.
- There isn't enough disk space to save a file.
- You lack the necessary credentials to perform an action on the file system.

It is important that the developer catches these errors to help the user understand why Snooz failed to analyze their data.

Here's an example of how to handle a runtime error in a ``compute()`` function:

.. code-block:: python

   try : 
         dataframe.to_csv(path_or_buf=filename, sep='\t', \
            index=False, index_label='False', mode='a', header=write_header, encoding="utf_8")
   except :
         error_message = f"Snooz can not write in the file {filename}."+\
            f" Check if the drive is accessible and ensure the file is not already open."
         raise NodeRuntimeException(self.identifier, "SpindlesDetails", error_message)     


How to run a process over multiple files
====================================================================
TODO

More information about the modules
====================================================================
See :ref:`info_modules`.

More information about the tools
====================================================================
See :ref:`info_tools`.

More information about the packages
====================================================================
See :ref:`info_packages`.