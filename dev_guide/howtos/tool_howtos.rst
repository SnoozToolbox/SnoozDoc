
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
When using the ``main_utils.py`` Python script with the option **3- Create a tool**, make sure to answer **N** to the prompt "Is this a custom step?"

The script will then ask for a **module_id** — this corresponds to the identifier field automatically generated when the module is instantiated in the tool's process view.
If the instance has not yet been created, you can leave this field empty and edit the JSON file later.

**Example:**

The tool **SleepCycleExport** from the CEAMS package includes a module's settings view at the steps ``2 - Cycle Definition``.
The step is described in the JSON file ``SleepCycleExport.json`` as follows:

.. code-block:: JSON

      {
         "name": "Cycle Definition",
         "description": "Define your sleep cycle.",
         "module_id": "4ae3d940-e282-414a-a1a7-c71f0a7acc98",
         "show_index": true
      },

The **module_id** can be found in the same ``SleepCycleExport.json`` file under the module definition, as shown below:

.. code-block:: JSON

      },
         "module": "CEAMSModules.SleepCyclesDelimiter",
         "identifier": "4ae3d940-e282-414a-a1a7-c71f0a7acc98",
         "pos_x": -204.20408163265301,
         "pos_y": -156.0453514739229,
         "activation_state": "activated",
         "package": {
            "package_name": "CEAMSModules"
      }

.. warning::

   If you change the module instance in the process view (e.g., delete and recreate it), make sure to update the **module_id** in the JSON file accordingly.
   
.. note::

   If multiple instances of the same module exist in the process view, you can distinguish them by their position or their connections.

   A useful tip is to temporarily modify the value of an input field by adding a unique keyword to identify the instance more easily.


How to add picture to a step
======================================
Sometimes you may want to display a static image (e.g., a diagram, logo, or illustration) directly in your tool's interface.
To do this in Snooz, you can convert your image into Base64 format and then load it dynamically into a QLabel in your PyQt UI.

**Step 1 — Convert your image to Base64**

Use the following Python script to convert your image file(s) into a Base64-encoded .py file that can be safely included in your package.

.. code-block:: python

   import base64
   import os

   # List of images to convert
   image_files = ['image_to_convert.png']

   # Variable names for each image
   variable_names = ['IMAGE_BASE64']

   # Get script directory
   script_dir = os.path.dirname(os.path.abspath(__file__))

   # Create the output data file
   output_file = os.path.join(script_dir, 'image_data_base64.py')

   with open(output_file, 'w') as f:
      f.write('"""\n')
      f.write('Base64 encoded images\n')
      f.write('"""\n\n')

      for image_file, var_name in zip(image_files, variable_names):
         try:
               with open(os.path.join(script_dir, image_file), 'rb') as img_f:
                  image_data = base64.b64encode(img_f.read()).decode()
                  f.write(f'{var_name} = """\n')
                  f.write(image_data)
                  f.write('\n""".strip()\n\n')
         except FileNotFoundError:
               print(f"Warning: {image_file} not found in {script_dir}")
               f.write(f'{var_name} = ""\n\n')

   print(f"Created {output_file}")

After running this script, a new file named ``image_data_base64.py`` will be created in the same folder.
It will contain one variable (e.g., ``IMAGE_BASE64``) storing your image data.

**Step 2 — Add a QLabel to your UI**

In Qt Designer, place a QLabel in your form where you want the image to appear.
Rename it clearly (for example: ``label_illustration``).

.. note::
   Make sure the label has an appropriate size policy (e.g., Fixed or Preferred) and optionally set scaledContents to True if you want the image to resize with the label.

**Step 3 — Display the image in your code**

In your Python class that manages the UI, import the Base64 variable and set the image on the QLabel as follows:

.. code-block:: python

   import base64
   from qtpy.QtGui import QPixmap
   from .image_data_base64 import IMAGE_BASE64

   image_bytes = base64.b64decode(IMAGE_BASE64)
   pixmap = QPixmap()
   pixmap.loadFromData(image_bytes)
   self.label_illustration.setPixmap(pixmap)

**Example:**

The **SleepBouts** tool from the CEAMS package includes an image on its introduction page.
The file ``sleep_bouts.png`` is converted to Base64 and stored in ``art_image_data.py``.
The file ``IntroStep.py`` then loads the image and sets it on the QLabel as follows:

.. code-block:: python

    def _load_embedded_image(self):
        """Load the embedded base64 image data into label_5."""
        from .art_image_data import SLEEP_BOUTS_IMAGE_BASE64
        image_bytes = base64.b64decode(SLEEP_BOUTS_IMAGE_BASE64)
        pixmap = QPixmap()
        pixmap.loadFromData(image_bytes)
        self.label_5.setPixmap(pixmap)


How to add a resource to a step
======================================
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




   
 

