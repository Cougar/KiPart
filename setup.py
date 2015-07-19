#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import KiPart


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='kipart',
    version=KiPart.__version__,
    description="Part creator for KiCad.",
    long_description=readme + '\n\n' + history,
    author=KiPart.__author__,
    author_email=KiPart.__email__,
    url='https://github.com/xesscorp/kipart',
#    packages=['kipart',],
    packages=setuptools.find_packages(),
    entry_points={'console_scripts':['kipart = kipart.__main__']},
    package_dir={'kipart':
                 'kipart'},
    include_package_data=True,
    package_data={'KiPart': ['*.gif', '*.png']},
    scripts=[],
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='kipart',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
