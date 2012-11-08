#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

from zerodivision.proxy.skel import __version__

with open('README') as stream:
  long_desc = stream.read()

requires = ['zerodivision']

setup(
    name='zerodivision.proxy.skel',
    version=__version__,
    author='Shane R. Spencer',
    author_email='shane@bogomip.com',
    namespace_packages=['zerodivision', 'zerodivision.proxy'],
    packages=['zerodivision.proxy.skel'],
    url='https://github.com/whardier/zerodivision/proxies/skel/',
    license='MIT',
    description='Zerodivision Skel Proxy',
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
        'Topic :: System :: Distributed Computing',
    ],
)


