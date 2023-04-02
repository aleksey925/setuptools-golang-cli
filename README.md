setuptools-golang-cli
=====================

Setuptools extension for building cli written in golang.

## How to use

`pyproject.toml`

> Replace `tag-name` with the required tag.

```toml
[build-system]
requires = [
    "setuptools>=61.0.0",
    "setuptools-golang-cli @ git+https://github.com/aleksey925/setuptools-golang-cli.git@tag-name",
    "wheel",
]
build-backend = "setuptools.build_meta"
```

`setup.py`

```python
from setuptools import setup, Extension

setup(
    ext_modules=[Extension('example', ['example.go'])],
    build_golang_cli={'root': 'github.com/user/project'},
)
```

An example of usage can be found [here](https://github.com/aleksey925/py-gopac/)