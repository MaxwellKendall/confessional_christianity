# confessional-christianity-api
The goal of this project is to create a REST API that returns valuable data on the historic confessions of the Christian faith. This will be an iterative project; first, we will attempt to return the contents of the confessions themselves in a client friendly manner; in the future, we may seek to possibly provide insights on the data itself.

## Technology
Currently we are using Python and the Django module for scaffolding the API and Postgres for the data layer.

## Dependency Management in Python
Dependency management for python projects are done using virtual environments. Like `npm`, we use a global install of the [virtual_env](https://docs.python-guide.org/dev/virtualenvs/) module.

1. Global install: `pip install virtualenv`
2. Create a virtual env: `virtualenv venv`

The result of this command is a new copy of python with all the relevant executables and a copy of `pip` to install new packages. The name of the virtual environment is `venv`. This is by convention. 

To begin using the virual environment, we need to activate it with the following third step:

3. Activate the virtual env: `source venv/bin/activate`

The benefit of this is that any package installed using pip will be placed in the `venv` folder, isolated from the global Python installation.

To create a `requirements.txt` file, simply freeze the current dependency map with the followifng command: `pip freeze > requirements.txt`. We can see the listed dependencies by executing `pip list`.

For another developer to duplicate this environment, all they will need to do is run `pip install -r requirements.txt`.

To exit the virtual environment and go back to using the local install of Python with its local modules, execute `deactivate`.

## Using the English Standard Version for API Calls
Old Testament DAM_ID: `ENGESVO1ET`
New Testament DAM_ID: `ENGESVN1ET`

## Natural Language Processing Resources
Spacy + NLTK.

## Conda
Similar to both pip & venv as it can (a) manage virutal environments and (b) install non-python modules.

## Data Science
Jupyter module (Julia, python, R)
- for interactive notebooks
Go to directory of Jupyter notebook:
- Establish conda virtual env
- With jupyter installed, run `jupyter lab`
- Opens browser window
