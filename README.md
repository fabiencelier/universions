# universions

Python library to get the version of other tools

[![PyPI pyversions](https://img.shields.io/pypi/pyversions/universions.svg)](https://pypi.python.org/pypi/universions/)  
[![PyPI version](https://badge.fury.io/py/universions.svg)](https://badge.fury.io/py/universions)  
[![Anaconda-Server Badge](https://anaconda.org/conda-forge/universions/badges/version.svg)](https://anaconda.org/conda-forge/universions)  
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[Read the documentation](https://universions.readthedocs.io/en/latest/index.html)

## Install

### with pip

```bash
pip install universions
```

### with conda

```bash
conda install -c conda-forge universions
```

## Examples

In python code :

```python
>>> from universions.java import get_java_version
>>> get_java_version()
Version(major=10, minor=0, patch=2, prerelease=None, build=None)
>>> get_java_version() > (1, 8)
True
```

In the command line :

```bash
>>> universions java
11.0
>>> universions node -v
12.6.0
```

## Languages and other tools supported

- [Java](https://universions.readthedocs.io/en/latest/tools/java.html)
- [Node](https://universions.readthedocs.io/en/latest/tools/node.html)
- [Pip](https://universions.readthedocs.io/en/latest/tools/pip.html)
- [Python](https://universions.readthedocs.io/en/latest/tools/python.html)

Open an issue if you want more !
If you want to contribute read the [contributing guide](https://github.com/fabiencelier/universions/blob/master/CONTRIBUTING.md).
