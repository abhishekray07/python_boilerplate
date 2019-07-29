#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
doclink = """
Documentation
-------------

The full documentation is at http://python_boilerplate.rtfd.org."""
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='python_boilerplate',
    version='1.0.0',
    description='Deploy static HTML sites to S3 with the simple 'alotofeffort' command.',
    long_description=readme + '\n\n' + doclink + '\n\n' + history,
    author='Abhishek Ray',
    author_email='abhishekray07@gmail.com',
    url='https://github.com/abhishekray07/python_boilerplate',
    packages=[
        'python_boilerplate',
    ],
    package_dir={'python_boilerplate': 'python_boilerplate'},
    include_package_data=True,
    install_requires=[
    ],
    license='MIT',
    zip_safe=False,
    keywords='python_boilerplate',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
