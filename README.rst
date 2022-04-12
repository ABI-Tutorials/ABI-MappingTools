
ABI Mapping Tools Documentation
===============================

The Auckland Bioengineering Institute (ABI) mapping tools documentation is a reStructured text based project.
This project uses Sphinx to create beautiful documentation from the reStructured text source files.
This documentation is available in its rendered form from `readthedocs.org <https://abi-mapping-tools.readthedocs.io/>`_.

Getting started
---------------

First we will create a Python virtual environment to install the Python packages that are required to generate an HTML form of the documentation.
We assume here that Python is at least version 3.7.

::
  
  python -m venv venv-sphinx

Next, we activate this virtual environment and install Sphinx::

  source venv-sphinx/bin/activate
  pip install sphinx

..note::

  The command for activating a virtual environment is slightly different for differnet OSes.
  Here we are showing commands suitable for a `bash <https://www.gnu.org/software/bash/>`_ environment.

To finish, we clone this documentation repository and retrieve all linked remote repositories.

::

  git clone --recurse-submodules -j4 https://github.com/ABI-Tutorials/ABI-MappingTools

Building documentation
----------------------

With the virtual environment created in the *Getting Started* we can build the documentation.
For a *bash* environment with GNU *make* available we can build the documentation with the following commands::

  cd ABI-MappingTools
  make html

..note::

  For Windows we can execute **make.bat** to build the documentation.

Viewing documentation
---------------------

To view the documententation pass the absolute path to the main documentation index file to your favourite web browser::

  <repository root directory>/docs/build/html/index.html 

You can if you want use Python to serve the HTML web pages with a simple server with the following commands::

  cd <repository root directory>/docs/build/html/index.html
  python -m http.server 8000

For both of these commands replace *<repository root directory>* with the absolute path to the repository.

