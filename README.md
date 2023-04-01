setuptools-golang-cli
=====================

Setuptools extension for building golang cli.

**How to use**

Add `setuptools-golang-cli` to `setup_requires` in `setup.py`, as in an example below.

```python
from setuptools import setup, Extension

setup(
    ...
    build_golang_cli={'root': 'github.com/user/project'},
    ext_modules=[Extension('example', ['example.go'])],
    setup_requires=['setuptools-golang-cli'],
    ...
)
```