#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ast
import os
import re
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

script_file = 's3pypi-root-index'

with open(script_file, 'rb') as f:
    init_contents = f.read().decode('utf-8')

    def get_var(var_name):
        pattern = re.compile(r'%s\s+=\s+(.*)' % var_name)
        match = pattern.search(init_contents).group(1)
        return str(ast.literal_eval(match))

    name = get_var("__prog__")
    version = get_var("__version__")
    description = get_var("__description__")

readme = open('README.md').read()
requirements = open("requirements.txt").read().split("\n")
author = 'November Five BVBA, Nate Coraor'
author_email = 'nate@bx.psu.edu'
url = 'https://github.com/natefoo/s3pypi-root-index'


setup(
    name=name,
    version=version,
    description=description,
    long_description=readme,
    long_description_content_type='text/markdown',
    author=author,
    author_email=author_email,
    url=url,
    scripts=[script_file],
    install_requires=requirements,
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Topic :: System :: Archiving :: Packaging',
        'Topic :: System :: Installation/Setup',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
