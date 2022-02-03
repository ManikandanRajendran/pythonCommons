import sys
import setuptools

setuptools.setup(
  name="pythonCommons",
  version="1.0",
  url="https://github.com/ManikandanRajendran/pythonCommons",
  packages=setuptools.find_packages(),
    platforms='any',
    install_requires=[
      'requests'
    ],  
  extras_require={}, 
  package_data={},
  classifiers=[],)
