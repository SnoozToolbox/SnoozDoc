# SnoozDoc
Documentation about the Snooz application

# Create a virtual python environment
python3.10 -m venv snooz_doc_env

# Activate the virtual python environment
source snooz_doc_env/bin/activate

# To install the documentation
pip install sphinx
pip install sphinx_rtd_theme

# To create the documentation from the root folder
sphinx-build -b html . html

# To create the requirements.txt used by readthedocs from the root folder
pip3 freeze > requirements.txt
