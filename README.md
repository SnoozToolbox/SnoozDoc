# SnoozDoc  
Documentation about the Snooz Toolbox

---

## 🔧 1. Initial Configuration (One-Time Setup for Remote Builds)

This section is for configuring the remote ReadTheDocs server and GitHub integration. It only needs to be done once.

### ✅ Create a virtual environment for compatibility (Linux recommended for remote builds)
Use a supported OS: `ubuntu-20.04`, `ubuntu-22.04`, `ubuntu-24.04`, or `ubuntu-lts-latest`.

```bash
$ python3.10 -m venv snooz_doc_env
$ source snooz_doc_env/bin/activate
```

### ✅ Install the documentation dependencies
```bash
$ pip install sphinx  
$ pip install sphinx_rtd_theme  
```

### ✅ Generate the `requirements.txt`
This file is referenced in `.readthedocs.yaml` and required to build the docs remotely on ReadTheDocs.

> ⚠️ This step must be run on a supported Linux OS (e.g., `ubuntu-22.04`):

```bash
$ pip freeze > requirements.txt
```

### ✅ Configure `.readthedocs.yaml`
Ensure the `.readthedocs.yaml` is present and correctly configured for remote builds.

### ✅ Set up GitHub Webhook to trigger builds

1. Go to GitHub → **Settings** → **Webhooks**
2. Add:
   - **Payload URL**:  
     `https://readthedocs.org/api/v2/webhook/snooz-toolbox-documentation/243027/`
   - **Secret**:  
     Generated from ReadTheDocs:  
     [Webhook Settings](https://readthedocs.org/dashboard/snooz-toolbox-documentation/integrations/243027/)

> Use the **Resync webhook** button on ReadTheDocs to regenerate the secret if needed.

### ✅ Add a versioned release to the documentation

1. Tag the commit in the `main` branch.
2. Visit: [ReadTheDocs Project](https://app.readthedocs.org/projects/snooz-toolbox-documentation/)
3. Click **+ Add version** and select your tag.
4. Then go to:  
   [Version Settings](https://app.readthedocs.org/dashboard/snooz-toolbox-documentation/edit/)  
   Set **Default version** to the one you want displayed to visitors.

---

## 👩‍💻 2. Developer Instructions (For Snooz Tool Developers)

This section is for developers who want to write or update the documentation for their tools in Snooz.

### Clone the SnoozDoc repository
```bash
git clone https://github.com/SnoozToolbox/SnoozDoc.git
```

The branch to update must match the corresponding Snooz release
Browse the available branches to find the one that matches the Snooz release:
https://github.com/SnoozToolbox/SnoozDoc/branches

Create a new branch if the upcoming release branch is not yet available.

### ▶️ Create and activate the virtual environment

#### On Linux/macOS:
```bash
$ python3.10 -m venv snooz_doc_env
$ source snooz_doc_env/bin/activate
```

#### On Windows:
```cmd
> call snooz_doc_env\Scripts\activate.bat
```
```Powershell
> snooz_doc_env\Scripts\activate.ps1
```

### ▶️ Install documentation dependencies
```bash
$ pip install sphinx  
$ pip install sphinx_rtd_theme  
```

### ▶️ Build the HTML documentation locally
From the root folder:

```bash
$ sphinx-build -b html . html
```

> This will generate an `html/` folder (locally only — it's ignored by git).
