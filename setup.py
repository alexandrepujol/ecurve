#
# Elliptic Curves in python
# Version 1.0
# Year 2014
# Author Alexandre PUJOL <alexandre.pujol.1@etu.univ-amu.fr>
# Author Maxime CHEMIN <maxime.chemin@etu.univ-amu.fr>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License.
#

from setuptools import setup
from distutils.core import Extension
import sys

(major, minor, micro, level, serial) = sys.version_info

if major > 2:
    source = 'fasttools3.c'
else:
    source = 'fasttools2.c'

tools_ext = Extension('fasttools',
            libraries=['gmp'],
            sources=[source])

setup(name='ecurve',
	version='1.0',
	description='Cryptographic primitives on elliptic curves',
	author='Alexandre PUJOL & Maxime CHEMIN',
	url='https://github.com/alexandrepujol/ecurve',
	license='GPL',
	packages=['ecurve'],
    ext_modules= [tools_ext],
	install_requires=['pycrypto',],
	zip_safe=False)
