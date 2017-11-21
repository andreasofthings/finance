#!/usr/bin/env python

import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

setup(
    name='finance',
    version='0.17.11',
    description='Collection of financial Python functions',
    long_description=README,
    license='MIT License',
    author='Andreas Neumeier',
    author_email='andreas@neumeier.org',
    url='https://github.com/aneumeier/finance/',
    packages=['finance'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
        'pandas',
    ]
)
