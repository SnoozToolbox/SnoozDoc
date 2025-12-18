================================================
Running Snooz on Compute Canada for Users
================================================

This guide explains how to run Snooz in headless mode on Compute Canada clusters using the command line (terminal).

.. contents:: Table of Contents
   :depth: 3
   :local:

Prerequisites
=============

Before starting, ensure you have:

* Access to a Compute Canada cluster (Narval, Beluga, Cedar, or Graham)
* Login credentials at: https://ccdb.alliancecan.ca/security/login
* Your Snooz Toolbox code in a Compute Canada cluster (snooz-toolbox folder)
* Your Snooz packages
* A valid Snooz pipeline JSON file

Connecting to Compute Canada
=============================

Step 1: Open Terminal
----------------------

**On Windows:**

* Press ``Windows Key + R``
* Type ``cmd`` or ``powershell`` and press Enter

**On Mac/Linux:**

* Press ``Cmd + Space`` (Mac) or ``Ctrl + Alt + T`` (Linux)
* Type ``terminal`` and press Enter

Step 2: Connect to the Cluster
-------------------------------

In the terminal, type the following command and press Enter::

    ssh your_username@narval.computecanada.ca

Replace ``your_username`` with your actual Compute Canada username.

When asked, enter your password (the text won't appear as you type, this is normal).

.. note::
   You need to activate your account with Duo two-factor authentication.
   After successful login, you will see a command prompt on the cluster.

Installation on Compute Canada
===============================

Step 1: Set Up Python Environment
----------------------------------

Create Virtual Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can check :ref:`virt_env` for more details.

Type these commands one by one, pressing Enter after each::

    python -m venv ~/snooz_env
    source ~/snooz_env/bin/activate

You should see ``(snooz_env)`` appear at the beginning of your command line.

.. note::
   The virtual environment keeps your dependencies isolated and prevents conflicts.

Step 2: Navigate to Snooz Toolbox
----------------------------------

1. **Go to your Snooz Toolbox folder**::

    cd /path/to/snooz-toolbox/

2. **Ensure proper file encoding** (if needed write this command in the terminal to have a proper format)::

    dos2unix requirements.txt

3. **Install the required libraries**::

    grep -avE '^(PySide6|PySide6_Addons|PySide6_Essentials|shiboken6)' requirements.txt | pip install -r /dev/stdin

Wait for the installation to complete. You will see many lines of text scrolling by.

.. tip::
   This command automatically excludes GUI-related packages that are not needed in headless mode.

Preparing Your Files
====================

Step 1: Check Package Installation
-----------------------------------

Navigate to the packages folder::

    cd src/main/resources/base/packages

List the files to verify your packages are there::

    ls -la

.. important::
   Package versions must match your CEAMSModules and CEAMSTools versions.

Step 2: Organize Your Files
----------------------------

Your files should be organized like this::

    snooz-toolbox/
    └── src/
        └── main/
            └── resources/
                └── ComputeCanada/
                    ├── YourWorkspace.json    # Your pipeline file
                    └── data/                 # Your dataset folder

Create the folder structure if needed::

    mkdir -p src/main/resources/ComputeCanada/data

Copy your files to the ComputeCanada folder::

    cp /path/to/your/workspace.json src/main/resources/ComputeCanada/
    cp -r /path/to/your/data/* src/main/resources/ComputeCanada/data/

.. tip::
   You can move your files from your local machine to Compute canada using mediator apps like FileZilla or WinSCP.

Running Snooz
=============

Step 1: Activate Virtual Environment
-------------------------------------

If you closed the terminal or it's a new session, activate the environment again::

    source ~/snooz_env/bin/activate

Step 2: Navigate to Python Folder
----------------------------------

Go to the main Python folder::

    cd ~/snooz-toolbox/src/main/python

Step 3: Run Snooz
-----------------

Run your pipeline with this command::

    python main.py --headless --f /absolute/path/to/YourWorkspace.json

Replace ``/absolute/path/to/YourWorkspace.json`` with the full path to your workspace file.

Example::

    python main.py --headless --f /home/username/snooz-toolbox/src/main/resources/ComputeCanada/YourWorkspace.json

.. note::
   The process will start and show progress in the terminal. Wait until it completes.

Running Long Jobs with SLURM
=============================

For analyses that take more than a few minutes, use SLURM to run in the background.

Step 1: Create Job Script
--------------------------

Create a new file::

    nano run_snooz.sh

Type or paste the following::

    #!/bin/bash
    SBATCH --account=def-your_account
    #SBATCH --time=02:00:00
    #SBATCH --mem=8G
    #SBATCH --cpus-per-task=4
    SBATCH --job-name=snooz_analysis
    SBATCH --output=snooz_%j.out
    SBATCH --error=snooz_%j.err

    source ~/snooz_env/bin/activate
    cd $HOME/snooz-toolbox/src/main/python
    python main.py --headless --f /absolute/path/to/YourWorkspace.json
    echo "Job completed at $(date)"

Replace:

* ``def-your_account`` with your Compute Canada account
* ``/absolute/path/to/YourWorkspace.json`` with your actual file path

Step 2: Submit the Job
-----------------------

Submit your job::

    sbatch run_snooz.sh

You will see a message like: ``Submitted batch job 12345678``

Step 3: Check Job Status
-------------------------

Check if your job is running::

    squeue -u $USER

View the output file while it's running::

    tail -f snooz_12345678.out

Replace ``12345678`` with your actual job number.

Press ``Ctrl+C`` to stop viewing the file.

Troubleshooting
===============

Common Problems
---------------

Problem: "Command not found"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Make sure you activated the virtual environment::

    source ~/snooz_env/bin/activate

Problem: "File not found"
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Solution:**

1. Check the file exists::

       ls /path/to/your/file.json

2. Use the full path starting with ``/home/username/``

3. Check you're in the right folder::

       pwd

Problem: "Permission denied"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Make the file readable::

    chmod +r /path/to/your/file

Problem: Job killed or out of memory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Edit your job script and increase memory::

    nano run_snooz.sh

Change the line::

    #SBATCH --mem=8G

To::

    #SBATCH --mem=16G

Save and resubmit::

    sbatch run_snooz.sh

Useful Commands
===============

Basic Terminal Commands
------------------------

View current folder::

    pwd

List files in current folder::

    ls

Change folder::

    cd /path/to/folder

Go back one folder::

    cd ..

View file content::

    cat filename.txt

Check if program is installed::

    which python

Compute Canada Commands
------------------------

Check storage usage::

    diskusage_report

View running jobs::

    squeue -u $USER

Cancel a job::

    scancel job_number

View completed job info::

    seff job_number

Getting Help
============

If you encounter problems:

1. Check the error messages in the terminal
2. Look at the output files: ``snooz_jobid.out`` and ``snooz_jobid.err``
3. Verify all file paths are correct and use full paths
4. Make sure your virtual environment is activated
5. Contact your Compute Canada support with your job ID

.. tip::
   Save all commands you use in a text file for future reference.
