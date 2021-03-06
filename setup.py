#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

from zerodivision import __version__

with open('README') as stream:
  long_desc = stream.read()

setup(
    name='zerodivision',
    version=__version__,
    author='Shane R. Spencer',
    author_email='shane@bogomip.com',
    packages=['zerodivision', 'zerodivision.proxy'],
    url='https://github.com/whardier/zerodivision',
    license='MIT',
    description='Python based zeromq proxy helpers',
    long_description=long_desc,
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Development Status :: 1 - Planning',
        'Environment :: No Input/Output (Daemon)',
        'Environment :: Console',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Topic :: System :: Networking',
        'Topic :: Database',
        'Topic :: Communications',
        'Topic :: System :: Distributed Computing',
    ],
)


