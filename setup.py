#!/usr/bin/env python

import glob
from setuptools import setup, find_packages

# Get metadata from setup.cfg (optional) or directly include here
PACKAGENAME = 'scimes'
DESCRIPTION = 'Spectral Clustering for Molecular Interstellar Emission Segmentation'
AUTHOR = 'Dario Colombo, Erik Rosolowsky, Adam Ginsburg, Ana Duarte-Cabral, and Annie Hughes'
AUTHOR_EMAIL = 'dario.colombo222@gmail.com'
LICENSE = 'BSD'
URL = 'http://scimes.readthedocs.org'
VERSION = '0.3.2'

# Modernized setup
setup(
    name=PACKAGENAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',  # Ensure correct content type
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license=LICENSE,
    url=URL,
    packages=find_packages(),  # Automatically find all packages
    scripts=glob.glob('scripts/*'),  # Any scripts you want to include
    install_requires=[
        'astropy',
        'numpy',
        'astrodendro',
        'scikit-learn'
    ],  # Specify dependencies
    classifiers=[  # Add more classifiers to categorize your package
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Astronomy",
    ],
    python_requires='>=3.7',  # Minimum Python version
    zip_safe=False,
)
