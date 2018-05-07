from setuptools import setup


setup(
    name='setuptools-golang-cli',
    description='',
    url='',
    version='0.0.1',
    author='Aleksey Petrunnik',
    author_email='',
    py_modules=['setuptools_golang_cli'],
    install_requires=[],
    entry_points={
        'distutils.setup_keywords': [
            'build_golang_cli = setuptools_golang_cli:set_build_ext',
        ],
    },
)