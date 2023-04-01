from setuptools import setup

setup(
    py_modules=['setuptools_golang_cli'],
    entry_points={
        'distutils.setup_keywords': [
            'build_golang_cli = setuptools_golang_cli:set_build_ext',
        ],
    },
)
