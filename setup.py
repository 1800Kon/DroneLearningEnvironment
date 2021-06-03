# flake8: noqa
from distutils.core import setup
from glob import glob
from os.path import basename, splitext

from setuptools import find_packages

setup(name='Drone learning environment',
      version='1.0',
      description='Python Learning environment',
      author='Pepe Loperena and Georgi Dimitrov',
      packages=find_packages('Challenges'),
      package_dir={'': 'Challenges'},
      py_modules=[splitext(basename(path))[0] for path in glob('Challenges/*.py')],
      )
