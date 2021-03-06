#!/usr/bin/env python

import platform

from setuptools import setup, find_packages

DESCRIPTION = """
Pydump allows post-mortem debugging for Python programs.

It writes the traceback of an exception into a file and can later load
it in a Python debugger.

Works with the built-in pdb and with other popular debuggers
(pudb, ipdb and pdbpp).
"""

# get version without importing
__version__ = 'unknown'
import os
for line in open(os.path.join('pydump', 'pydump.py')):
    if line.startswith('__version__ = '):
        exec(line)
        break

setup(
    name='pydump',
    version=__version__,
    description='Post-mortem debugging for Python programs',
    long_description=DESCRIPTION,
    author='Eli Finer',
    license='MIT',
    author_email='eli.finer@gmail.com',
    url='https://github.com/gooli/pydump',
    packages=find_packages(),
        entry_points={
        'console_scripts': [
            'pydump=pydump.pydump_main:main'
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Debuggers'
    ]
)
