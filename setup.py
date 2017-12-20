#!/usr/bin/env python
# coding: utf-8
from setuptools import setup, find_packages
from wildcat import __author__, __version__, __license__
 
setup(
        name             = 'wildcat',
        version          = __version__,
        description      = 'Sample for installing python library from github using pip',
        license          = __license__,
        author           = __author__,
        author_email     = 'minato@mdrft.com',
        url              = 'https://github.com/mdrft/wildcat',
        keywords         = 'sample pip github python',
        packages         = find_packages(),
        install_requires = [],
        )
