The `pbio` package provides miscellaneous bioinformatics and other supporting utilities for Python 3, including 
programs used for Ribo-seq periodicity estimation. It is required for the installation of [Rp-Bp](https://github.com/dieterich-lab/rp-bp). 
It combines utilities and programs from the defunct pymisc-utils (see [pyllars](https://github.com/bmmalone/pyllars))
and [riboseq-utils](https://github.com/dieterich-lab/riboseq-utils).


## Installation

To install from the command line:

```
# Clone the git repository.
git clone https://github.com/dieterich-lab/pybio-utils.git
cd pybio-utils
   
# To install in editable mode, replace "install" with "develop"...
python setup.py install --verbose --user
# ... or use pip (add option -e to install in editable mode).
pip3 --verbose --user install [-e] .
```

The `--user` option instructs `setup.py` to install the package in the user site-packages directory for the running Python.
Python automatically searches this directory, so it is not necessary to add this path to the PYTHONPATH variable.

## Virtual environment installation

It is a good practice to install a package and its dependencies in a virtual environment. 
The `venv` module provides support for creating environments with their own site directories. 
See [venv](https://docs.python.org/3/library/venv.html) for more information about Python 
virtual environments. To create a virtual environment:

```
python -m venv /path/to/virtual/environment
```

To activate the new virtual environment and install the package:

```
# Activate the new virtual environment.
source /path/to/virtual/environment/bin/activate

# If necessary, upgrade pip and additional packages.
pip install --upgrade pip

# Clone the git repository.
git clone https://github.com/dieterich-lab/pybio-utils.git
cd pybio-utils

pip --verbose install [-e] .

```

## Anaconda installation

The package can also be installed within an [anaconda](https://www.continuum.io/) environment. 

```
# Create the anaconda environment.
conda create -n my_new_environment python=3.5 anaconda

# Activate the new environment.
source activate my_new_environment

# Clone the git repository
git clone https://github.com/dieterich-lab/pybio-utils.git
cd pybio-utils

pip --verbose install [-e] .
```

## Usage

There is currently limited documentation, see [docs](docs/bio.md).

## Uninstallation

To remove the `pbio` package:

```
pip uninstall pbio
```
