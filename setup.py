from setuptools import setup

setup(
    name='setuptools-golang-cli',
    version='0.0.3',
    url='https://github.com/aleksey925/setuptools-golang-cli',
    license='MIT',
    author='Aleksey Petrunnik',
    author_email='petrunnik.a@gmail.com',
    description='Setuptools extension for building golang cli.',
    py_modules=['setuptools_golang_cli'],
    python_requires='>=3',
    install_requires=[],
    entry_points={
        'distutils.setup_keywords': [
            'build_golang_cli = setuptools_golang_cli:set_build_ext',
        ],
    },
)
