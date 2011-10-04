#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages, Extension
    have_setuptools = True
except ImportError:
    from distutils.core import setup
    def find_packages():
        return [
            'grandma',
        ]
    have_setuptools = False

requires = []

setup(
    author = 'Mark Fink',
    author_email = 'mark@mark-fink.de',
    description = 'grandma is used for combinatorial testing',
    url = 'http://github.com/markfink/grandma',
    download_url='http://pypi.python.org/pypi/grandma',
    name='grandma',
    version='0.1a2',
    packages = find_packages(),
    license='GNU LESSER GENERAL PUBLIC LICENSE, Version 3',
    long_description=open('README').read(),
    ext_modules = [Extension("jenny", ["./jenny/jenny.c"])],
    #scripts=['bin/grandma',],
    test_suite='nose.collector',
    test_requires=['nose', 'coverage'],
    platforms = 'any',
    zip_safe = False,
    include_package_data = True,
    classifiers = [
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Testing',
        'Natural Language :: English',
    ],
)

