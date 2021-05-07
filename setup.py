from distutils.core import setup
from glob import glob
from os.path import basename, splitext

from setuptools import find_packages

setup(name='Drone learning environment',
      version='1.0',
      description='Python Learning environment',
      author='Pepe Loperena and Georgi Dimitrov',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
      )