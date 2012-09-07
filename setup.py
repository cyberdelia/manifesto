#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='manifesto',
    version='0.4',
    description='Pluggable cache manifest for Django.',
    author='Timothee Peignier',
    author_email='timothee.peignier@tryphon.org',
    url='https://github.com/cyberdelia/manifesto',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'bencode',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
)