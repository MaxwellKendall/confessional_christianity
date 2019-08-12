# confessional-christianity-api

## Dependency Management
Dependency management for python projects are done using virtual environments. Like `npm`, we use a global install of the `[virtual_env](https://docs.python-guide.org/dev/virtualenvs/)` module.

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