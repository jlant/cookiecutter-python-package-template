cookiecutter-python-package-template
====================================

*A simple Cookiecutter Python package template.*


Features
--------

* Command line interface with Click_
* Code testing with pytest_
* Code documentation website with Sphinx_
* Helpful project maintenance with a Makefile_


Quick Start
-----------
To create a new Python_ package, run the Cookiecutter_ program in a directory
of your choice with the URL of this cookiecutter-python-package-template_:

.. code:: bash

   cookiecutter https://github.com/jlant/cookiecutter-python-package-template.git

You will then be prompted to answer a few questions about your package::

    author [Your name]: Jeremiah Lant
    email [Your email]: jeremiahlant@gmail.com
    package_name [Your package name]: hello world
    package_name_hyphenated [hello-world]: <Enter>
    package_name_underscored [hello_world]: <Enter>
    package_short_description [A short description of the project]: An example Hello World Python package.
    package_version [0.1.0]: <Enter>


After answering the questions, your package template will be created in your current working directory,
with the following package layout::

   hello-world                      Top level package directory
   |-- .gitignore                   Git ignore file
   |-- LICENSE                      MIT License for the package
   |-- Makefile                     Makefile for package maintenance
   |-- README.rst                   README file for package
   |-- docs                         Directory for code documentation
   |-- src                          Directory for source code
   |   |--hello_world               Directory for package source code
   |       |-- __init__.py          Python file to make the package source code directory a Python package
   |       |-- cli.py               Command line interface file using Click
   |       `-- hello_world.py       Python file representing the main package module
   |-- pyproject.toml               Configuration file for Python projects, defines build settings, metadata, dependencies, etc.
   `-- tests                        Directory for tests
       |-- __init__.py              Python file to make the tests directory a Python package
       `-- test_hello_world.py      Sample test file for main Python package


To start developing your newly created Python package, please do the following:

1. Create a virtual environment

.. code:: bash

   python3 -m venv venv

2. Activate the virtual environment

.. code:: bash

   source venv/bin/activate

3. Install the *development* dependenices listed in the `pyproject.toml` file in editable mode

.. code:: bash

   python -m pip install -e ".[dev]"

4. Confirm the package can be run from the Click_ command line interface

.. code:: bash

   hello-world --version

The output should be something like the following:

.. code:: bash

   hello-world, version 0.1.0

5. View the help menu from the Click_ command line interface:

.. code:: bash

   hello-world --help

You can also run the package as a module with:

.. code:: bash

   python -m hello_world --help

6. Run the initial unit tests using pytest_:

.. code:: bash

   pytest tests


7. Generate the package website using top-level Makefile:

.. code:: bash

   make docs

or, make the project website using Makefile from Sphinx::

   cd docs
   make html

The project documentation HTML pages are contained in the `_build\html` directory.
Open `index.html` in your browser to view the website.


Dependencies
------------
* Cookiecutter_

Install Cookiecutter_ using pip_:

.. code:: bash

   pip install cookiecutter


Author
------
Jeremiah Lant, jeremiahlant@gmail.com


References
----------
* Cookiecutter_
* pyOpenSci_
* `Best Practices in Scientific Computing`_
* `Simon Willison's Weblog - Things I've learned about building CLI tools in Python`_

.. _Cookiecutter: https://github.com/cookiecutter/cookiecutter
.. _Click: https://click.palletsprojects.com/en/stable/
.. _Python: https://www.python.org/
.. _pip: https://pip.pypa.io/en/stable/
.. _pytest: https://docs.pytest.org/en/latest/
.. _Sphinx: http://www.sphinx-doc.org/en/master/
.. _Makefile: https://en.wikipedia.org/wiki/Makefile
.. _pyOpenSci_: https://www.pyopensci.org/python-package-guide/index.html
.. _Best Practices in Scientific Computing: https://doi.org/10.1371/journal.pbio.1001745
.. _Simon Willison's Weblog - Things I've learned about building CLI tools in Python: https://simonwillison.net/2023/Sep/30/cli-tools-python/
.. _cookiecutter-python-package-template: https://github.com/jlant/cookiecutter-python-package-template
