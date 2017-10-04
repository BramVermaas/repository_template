Repository Template
===================

Template for a minimal python repository file structure.


Getting Started
---------------
This package is used mainly as a starting point for creating new packages

repository_template
~~~~~~~~~~~~~~~~~~~
Main project code folder. Change name to your own project name.

repository_template/__init__.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Allows for importing the package
Imports everything from core.py, doesn't need to be edited.

repository_template/core.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Core python module of this package.
Edit the content, but not the file name.

tests
~~~~~
Project unittests folder. Doesn't need to be edited

tests/__init__.py
~~~~~~~~~~~~~~~~~
Allows for importing and running tests. Doesn't need to be edited.

tests/test_core.py
~~~~~~~~~~~~~~~~~~
Unit test for specific module.
Edit name and content to fit project.

.gitignore
~~~~~~~~~~~
Description of files that shouldn't be published to git.
Contains allmost all files you don't want in git, probably doesn't need to be edited.

MANIFEST.in
~~~~~~~~~~~
Discription of non python files that should be published to git.
Edit if you have any required non python files in your project.

README.rst
~~~~~~~~~~~
Info displayed in PyPI on how to install and use the package. Required for PIP installation.
Edit to reflect installation and usage of your own project.

README.md
~~~~~~~~~~~
Info displayed on git on how to install and use the package. Required for GOGS, because it lacks a .rst parser.
Edit to reflect installation and usage of your own project.

requirements.py
~~~~~~~~~~~~~~~
Description of packages that need to be installed to use this package.
Edit information to fit requirements for your own project.

setup.py
~~~~~~~~
Contains project name, description, author, packages and information on testing the package.
Edit information to fit your own project.



Prerequisites
-------------

The following software is required to install this package

    * Python: http://www.python.org/downloads/
    * pip: https://bootstrap.pypa.io/get-pip.py
    * git: https://git-scm.com/download/

The following environment variables need to be set:

    * Path should contain the python installation directory (for example C:/Python27)
    * PYTHONPATH should contain the package installation directory (for example if the installation directory is Y:/pipeline, the pythonpath should be set to Y:/pipeline/Lib/site-packages). Use forward slashes, not the backward slashes windows uses by default.


Installation
------------

Run the following code in your terminal.
Replace the prefix <Drive:/folder> with the desired installation location.

    * ``python -m pip install --upgrade --prefix=<Drive:/folder> git+http://github.com/BramVermaas/repository_template#egg=repository_template``
    * ``python -m pip install --upgrade --prefix=<Drive:/folder> -r https://raw.githubusercontent.com/BramVermaas/repository_template/master/requirements.txt``



Running the tests
-----------------

Run the following in a terminal with the working directory in the package directory:

    python setup.py test

Or let nose2 find the tests:

    python -m nose2 -v



