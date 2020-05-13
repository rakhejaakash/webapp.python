## A sample website

###### Repo: `webapp.python`

### Description

This is a sample website.

Below is the structure of the project:

```
.
├── README.md                                   <-- This instructions file
├── templates                                   <-- Directory of all templates
    └── index.html                              <-- A sample template
├── website.py                                  <-- Central application
├── requirements.txt                            <-- List of all requirements
└── .gitignore                                  <-- Contains names of all files and directories to be ignored for git
```

### Requirements

- Python3.7+

### Create a virtual environment and install dependencies

For all the steps in this document that pertains to building/running/testing this application, you will need to set up a virtual environment and install the necessary dependencies. Below are the steps to doing just that:

- Create a virtual env: `python -mvenv .venv/`
- Activate virtual env: `source .venv/bin/activate` (macOS) or `source .venv/Scripts/activate` (windowsOS)
- Install dependencies: `pip install -r requirements/dev.txt`

### Local development

- Run `python website.py`
