The `pbio` package provides miscellaneous bioinformatics and other supporting utilities for Python 3, including 
programs used for Ribo-seq periodicity estimation. It is required for the installation of [Rp-Bp](https://github.com/dieterich-lab/rp-bp). 
It combines utilities and programs from the defunct pymisc-utils (see [pyllars](https://github.com/bmmalone/pyllars))
and [riboseq-utils](https://github.com/dieterich-lab/riboseq-utils).


## Installation

The `pbio` package can be installed in editable mode by adding the `-e` option to 
the `requirements.txt` file. 

## Installation (virtual environment)

To install `pbio` and dependencies, first create a virtual environment:
 
```
python3 -m venv /path/to/virtual/environment
```

For information about Python virtual environments, see the [venv](https://docs.python.org/3/library/venv.html) documentation.
To activate the new virtual environment and install `pbio`:

```
# Activate the new virtual environment.
source /path/to/virtual/environment/bin/activate

# If necessary, upgrade pip and wheel or additional packages (such as setuptools if installing in editable mode).
pip install --upgrade pip setuptools wheel

# Clone the git repository
git clone https://github.com/dieterich-lab/pybio-utils.git
cd pybio-utils

pip --verbose install -r requirements.txt

```

## Anaconda installation

The package can also be installed within an [anaconda](https://www.continuum.io/) environment. 

```
# Create the anaconda environment.
conda create -n my_new_environment python=3.6 anaconda

# Activate the new environment.
source activate my_new_environment

# Clone the git repository
git clone https://github.com/dieterich-lab/pybio-utils.git
cd pybio-utils

pip --verbose install -r requirements.txt
```

## Usage

There is currently limited documentation, see [docs](docs/bio.md).

## Uninstallation

To remove the `pbio` package:

```
pip uninstall pbio
```

If the package was installed in a dedicated virtual environment, this environment can also be cleared or removed.