.. _installation:

==========================
Developer Installation
==========================
This section will guide you through the steps of installing and configuring your development environment.

.. contents::
   :local:

Git client
=============
Install a Git client to download the code.

* On Windows you can use Git for windows: https://git-scm.com/download/win
* On Linux and macOS, run this command: ``sudo apt install git``

Snooz Workspace
==========================
First, manually create a folder called "snooz_workspace". 
This will be the root directory of the project and will contain at first only the snooz-toolbox repository.

Snooz Toolbox repository
-----------------------------------

The "snooz-toolbox" repository contains the main application code (the architecture of Snooz), which is essential for running the application in debug mode. 
However, you generally won't need to make modifications to this code unless you are working on a core feature of Snooz rather than on a specific tool.

Clone this repository into your new "snooz_workspace" folder. Type this command line in a terminal (or "Git Bash" on Windows): ``git clone https://github.com/SnoozToolbox/snooz-toolbox.git``

.. note::
   It is advised to tell Git to ignore the file **snooz.code-workspace** once downloaded because it will end up containing values that are specific to your installation. 
   
   Run this command to do it: ``git update-index --skip-worktree ./snooz.code-workspace``

The repository "snooz-toolbox" also contains the tools, modules and apps released with the Snooz Toolbox, located in the resources folder. 
This allows you to run many tools using a single repository. 
However, any modifications to tools, modules and apps must be made in a different repository, which you will learn about in another step.

Python 
=============
It's important to install Python version 3.10.X. The latest available version with an installer is version 3.10.11. 
You can download Python from the following link: https://www.python.org/downloads/release/python-31011/.

.. note::
   On Windows, it's advised to add the path to the Python executable to your environment variables.
   Follow this guide: https://realpython.com/add-python-to-path/

   Default Python installation path:

   * Windows : C:/Users/UserName/AppData/Local/Programs/python
   * Linux and macOS : /usr/bin/python3.10 or /usr/local/bin/python3.10

.. warning::
   On Linux, you need to manually install the Qt dev tools to access the designer tool.  Type in the terminal ``sudo apt-get install qttools5-dev``.

Python virtual environment
=======================================
Software using Python often relies on various external libraries. 
Some software may require specific versions of these libraries, so it's strongly advised to create a Python virtual environment dedicated to your Snooz installation.

You can follow this guide to set up a Python virtual environment: `Python venv <https://docs.python.org/3/library/venv.html>`_

Name the virtual environment ``snooz_310_env``.

If you have multiple versions of Python installed, make sure you use Python 3.10 to create the virtual environment.
Here an example of the command to type in the Command Prompt for Windows ``C:\Users\UserName\AppData\Local\Programs\Python\Python310\python -m venv .\snooz_310_env``

.. note::
   On Linux, you might need to run this command first: ``sudo apt install python3.10-venv``.

A folder called ``snooz_310_env`` should be created.

Activate the virtual environment in the terminal or Command Prompt:

   * For Windows : ``call /path_to_virtual_environment/snooz_310_env/Scripts/activate.bat``
   * For Linux and macOS : ``source /path_to_virtual_environment/snooz_310_env/bin/activate``

Once activated, you should see the name of the virtual environment in parenthesis in the terminal.

To complete the setup of your virtual environment, install the external libraries required to run Snooz.
The ``requirements.txt`` file is saved in the root folder of the "snooz-toolbox" repository you cloned previously.

To install the requirements, type in the terminal or Command Prompt:
 | ``pip install -r requirements.txt``

Visual Studio Code as IDE
=======================================
An Integrated Development Environment (IDE) is a software application that combines a source code editor, compiler/interpreter, debugger, and version control integration to streamline the development process within a single interface.

We use Visual Studio Code (VS Code) as our IDE. 
It's a free tool developed by Microsoft and is compatible with multiple platforms, including Windows, Linux, and macOS. 
For installation instructions, please refer to the following link: https://code.visualstudio.com/download.

Install the Python extension
------------------------------

VS Code is used for all kinds of programming tasks. To work with Python, you need to install a few extensions.

* Open VS Code
* From the navigation bar on the left, navigate to the extension panel(Ctrl-Shift-X).
* Install "Python" extension from Microsoft.
* Install "Qt for Python"

Configure your workspace
----------------------------

**Python Interpreter**

Define the Python intepreter from the virtual environment ``snooz_310_env``.

* Open VS Code
* Navigate to File-> Open workspace from file
* Choose the file snooz.code-workspace from the "snooz-toolbox" repository you cloned.
* Navigate to View -> Command Palette (Ctrl-Shift-p)  
  
   - Select "Python:Select Interpreter"
   - Select "Select at workspace level"
   - Find and select the Python executable within the folder of the Python virtual environment ``snooz_310_env`` you created in the previous step.  
     
     .. note::
      The path to the Python interpreter
   
      * Windows : "/snooz_310_env/Scripts/python";   
      * Linux and macOS : "snooz_310_env/bin/python"

.. warning::
   On macOS

   You may need to add the path to Python in the settings (when you virtual env does not appear in the selection.)

   * Open Visual Studio Code
   * Open .vscode/settings.json
   * Add the following setting::

      {
         "python.defaultInterpreterPath": "/path_to_virtual_environment/snooz_310_env/bin/python"
      }

Run Snooz
=======================================
To run Snooz from the source code see : :ref:`run_snooz`

.. toctree::

