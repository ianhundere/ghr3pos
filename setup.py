#!/usr/bin/env python3
import ast
import os
from setuptools import setup

here = os.path.dirname(__file__)
metadata = {}
with open(os.path.join(here, 'ghr3pos.py')) as f:
    for line in f:
        if line.startswith(('__version__ =')):
            k, v = line.split('=', 1)
            metadata[k.strip()] = ast.literal_eval(v.strip())

setup(
    name='ghr3pos',
    version=metadata['__version__'],
    author='ian hundere',
    author_email='ianhundere@gmail.com',
    py_modules=['ghr3pos'],
    python_requires='>=3.6',
    install_requires=['requests >=2.0,<3.0'],
    entry_points={
        'console_scripts': ['ghr3pos = ghr3pos.application:main'],
    },

)
