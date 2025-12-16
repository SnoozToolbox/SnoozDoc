===========================================
Running Snooz on Compute Canada
===========================================

This guide explains how to run Snooz in headless mode on Compute Canada clusters using the command line interface.

.. contents:: Table of Contents
   :depth: 3
   :local:

Prerequisites
=============

Before starting, ensure you have:

* Access to a Compute Canada cluster (Narval, Beluga, Cedar, or Graham)
* Login credentials at: https://ccdb.alliancecan.ca/security/login
* Clone of the :ref:`Snooz Toolbox repository <installation>` (snooz-toolbox)
* Your Snooz packages in: ``src/main/resources/base/packages``
* A valid Snooz pipeline JSON file

Installation on Compute Canada
===============================

Step 1: Connect to Your Cluster
--------------------------------

Using VSCode Remote-SSH Extension
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Install the Remote-SSH extension** in VSCode

2. **Configure SSH connection:**

   * Press ``F1`` or ``Ctrl+Shift+P``
   * Select: ``Remote-SSH: Open SSH Configuration File...``
   * Add a new host::

       Host narval
           YourUsername@narval.computecanada.ca

3. **Open your project folder** in VSCode through the remote connection

Step 2: Set Up Python Environment
----------------------------------

Create Virtual Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can check :ref:`Python virtual environment <installation>` for more details.

Open a terminal in VSCode and run::

    python -m venv ~/snooz_env
    source ~/snooz_env/bin/activate

.. note::
   The virtual environment keeps your dependencies isolated and prevents conflicts.

Configure Python Interpreter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Press ``Ctrl+Shift+P``
2. Type: ``Python: Select Interpreter``
3. Select the interpreter from ``~/snooz_env/bin/python``

Step 3: Install Dependencies
-----------------------------

1. **Navigate to the Snooz Toolbox directory:**

   ::

       cd /path/to/snooz-toolbox/

2. **Ensure proper file encoding** (if needed)::

       dos2unix requirements.txt

3. **Install required packages** (excluding GUI dependencies)::

       grep -avE '^(PySide6|PySide6_Addons|PySide6_Essentials|shiboken6)' requirements.txt | pip install -r /dev/stdin

.. tip::
   This command automatically excludes GUI-related packages that are not needed in headless mode.

Preparing Your Workspace
=========================

Verify Package Installation
----------------------------

1. Navigate to the packages directory::

       cd src/main/resources/base/packages

2. Verify that your Snooz package versions match your workspace modules::

       ls -la

.. important::
   Package versions must match your CEAMSModules and CEAMSTools versions.

Organize Your Files
-------------------

Project Structure
~~~~~~~~~~~~~~~~~

Organize your files as follows::

    snooz-toolbox/
    └── src/
        └── main/
            └── python/
                ├── main.py
                ├── YourWorkspace.json    # Your pipeline file
                └── data/                 # Optional: your dataset folder

File Placement Options
~~~~~~~~~~~~~~~~~~~~~~

**Option 1: Co-locate with main.py** (Recommended for testing)

Place both your JSON workspace and data in: ``snooz-toolbox/src/main/python/``

**Option 2: Use custom locations**

* Store your JSON file anywhere on the cluster
* Update paths in your JSON file to point to data locations
* Use absolute paths when running the command

Running Snooz in Headless Mode
===============================

Basic Usage
-----------

Navigate to the Python directory::

    cd snooz-toolbox/src/main/python

Run Snooz with your workspace::

    python main.py --headless --f YourWorkspace.json

Using Custom Paths
------------------

If your files are in different locations::

    python main.py --headless --f /absolute/path/to/YourWorkspace.json

.. note::
   When using custom paths:
   
   * Use **absolute paths** for reliability
   * Ensure all data paths in your JSON file are also absolute
   * Verify file permissions (``chmod +r``) if needed

Advanced Usage: SLURM Job Submission
=====================================

For long-running processes, submit as a SLURM job.

Create Job Script
-----------------

Create a file named ``run_snooz.sh``::

    #!/bin/bash
    #SBATCH --account=def-your_account
    #SBATCH --time=02:00:00
    #SBATCH --mem=8G
    #SBATCH --cpus-per-task=4
    #SBATCH --job-name=snooz_analysis
    #SBATCH --output=snooz_%j.out
    #SBATCH --error=snooz_%j.err

    # Activate virtual environment
    source ~/snooz_env/bin/activate

    # Navigate to working directory
    cd $HOME/snooz-toolbox/src/main/python

    # Run Snooz
    python main.py --headless --f YourWorkspace.json

    echo "Job completed at $(date)"

Submit the Job
--------------

:

    sbatch run_snooz.sh

Monitor Progress
----------------

Check job status::

    squeue -u $USER

View output in real-time::

    tail -f snooz_<job_id>.out

Troubleshooting
===============

Common Issues and Solutions
---------------------------

Import Errors
~~~~~~~~~~~~~

**Problem:** ``ModuleNotFoundError: No module named 'package_name'``

**Solution:**

1. Verify virtual environment is activated::

       which python

   Should point to ``~/snooz_env/bin/python``

2. Reinstall dependencies::

       pip install -r requirements.txt

File Not Found
~~~~~~~~~~~~~~

**Problem:** ``FileNotFoundError: [Errno 2] No such file or directory``

**Solution:**

* Use absolute paths in command and JSON files
* Verify file exists::

      ls -la /path/to/file

* Check file permissions::

      chmod +r /path/to/file

Memory Errors
~~~~~~~~~~~~~

**Problem:** Job killed due to memory limit

**Solution:**

Increase memory in SLURM script::

    #SBATCH --mem=16G
