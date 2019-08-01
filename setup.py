from setuptools import setup

setup(
    name='setuptools-golang-cli',
    version='0.0.2',
    url='https://bitbucket.org/alex925/setuptools-golang-cli/src/master/',
    author='Aleksey Petrunnik',
    author_email='zzz_vvv.94@mail.ru',
    description='',
    py_modules=['setuptools_golang_cli'],
    install_requires=[],
    entry_points={
        'distutils.setup_keywords': [
            'build_golang_cli = setuptools_golang_cli:set_build_ext',
        ],
    },
)