#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
  name = 'cartago',
  packages = find_packages(),
  install_requires=['pbxproj==2.1.2'],
  entry_points={
    'console_scripts': [
        'cartago = cartago.cartago:main'
    ]
  },
  version = '0.1',
  description = 'An automated framework installer using carthage',
  author = 'HELM S.C.P.',
  author_email = 'pypi@helm.cat',
  url = 'https://github.com/HelmMobile/Cartago',
  download_url = 'https://github.com/HelmMobile/Cartago/archive/0.2.tar.gz',
  keywords = ['carthage', 'swift', 'xcode', 'ios', "framework", "script", "xcode project"],
  classifiers = [],
)
