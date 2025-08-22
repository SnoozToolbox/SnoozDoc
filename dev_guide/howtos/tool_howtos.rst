
.. _tool_howtos:

=================
How Tos - Tool 
=================

To know what is the role of a tool in Snooz, see :ref:`technical_overview`.

.. contents::
   :local:

Before creating your own tool
==================================

- You need to have a properly configured development environment for Snooz. 
   - See :ref:`installation` for more details.
- Ensure that you have created your repository (e.g., my_snooz_repo) to manage your packages. 
   - See :ref:`run_snooz` for more details.
- You have already explored Snooz and have an understanding of its structure. 
   - See :ref:`explore_ex` for more details.

.. _How_to_create_a_tool:

How to create a tool
==================================
We use a command line to help create new tool. To access the terminal in VS Code, make sure to close Snooz beforehand. 

- In VS Code navigate to **Terminal -> New Terminal**
- Select your repository you forked from snooz-package-template (e.g. my_snooz_repo)
- Make sure the virtual environment **snooz_310_env** is activated (see :ref:`installation`)
- In the terminal type : ``python main_utils.py``
- Select **3- Create a tool**
- Fill the information to suit your design. If you make any mistakes, just repeat the steps and it will ask to overwrite the previous one.  If you need more information, see :ref:`info_tools`.


How to create a custom step
---------------------------
When using the ``main_utils.py`` Python script with the option **3- Create a tool**, make sure to answer **Y** to the prompt "Is this a custom step?"

How to create a configuration step
----------------------------------
TODO

How to use a module's settings page inside a step
-------------------------------------------------
TODO

How to add a resource to a step
-------------------------------
TODO

How to Share Information Between Steps
======================================

The Snooz architecture allows information to be shared between custom steps in the step-by-step tool *before* the tool is run.  
This makes it possible to adapt default settings or perform validation checks based on the user's choices in previous steps.

The sharing process uses a **context dictionary** named ``_context_manager``.  
A custom step can modify values in this dictionary through its UI, and any other step that listens to the same context key will be notified of changes.  
The ``_context_manager`` is a dictionary that publishes updates via the ``PubSubManager`` whenever a value is modified.  
For more details, see :ref:`information`.

To modify the context dictionary
------------------------------------
Edit the Python file of the step that modifies the context dictionary (e.g., ``Step1.py``):

- Define the context key as a class attribute (e.g., ``context_choice = "choice"``).
- In the constructor, set the default value for that key in the ``_context_manager`` dictionary (inherited from ``BaseStepView``):  
     e.g., ``self._context_manager[self.context_choice] = "1"``
- Ensure the value of the key is kept in sync with the UI by updating it every time the user interacts with the interface.

To listen to the context dictionary
------------------------------------
Edit the Python file of the step that listens to the context dictionary (e.g., ``Step2.py``):

- Import the class of the step that modifies the context dictionary:  
     e.g., ``from CEAMSTools.Tool1.Step1Folder.Step1File import Step1Class``
- Update the ``on_topic_update`` function to respond to modifications of the context dictionary:
   .. code-block:: python

      def on_topic_update(self, topic, message, sender):
         if topic == self._context_manager.topic:
               if message == Step1Class.context_choice:  # key of the context dict
                  # Read the value of the key
                  context_value = self._context_manager[Step1Class.context_choice]
                  # Adapt the settings based on the value read

.. warning::
   If the communication between two steps is bidirectional, or if multiple steps need to listen to the same context key, the recommended strategy is to define the context key in a separate file (e.g., ``commons.py``).  
   This allows all relevant steps to write to the same dictionary.


Examples to look at
--------------------
The tool **PowerSpectralAnalysis** from the CEAMS package shares information between the steps ``SelectionStep`` and ``AnnotationsSelStep``.

For an example that uses a context key defined in a separate file, see the tool **ConvertEDFBrowser** from the CEAMS package.  
The steps ``InputFilesStep`` and ``GroupDefinition`` both write to the data model shared through the context manager.




   
 

