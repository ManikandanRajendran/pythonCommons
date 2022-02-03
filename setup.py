import sys
import setuptools

setuptools.setup(
  name="commons",
  version="1.0",
  packages=setuptools.find_packages(),
    platforms='any',

    install_requires=[
      'requests'
    ],
  
  extras_require={}, 
  package_data={},
  classifiers=[],)
