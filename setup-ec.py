#!/usr/bin/env python

# here is some internal information
# $Id: setup-ec.py,v 1.1 2006-07-26 10:04:04 marc Exp $
#


__version__ = "$Revision: 1.1 $"
# $Source: /atix/ATIX/CVSROOT/nashead2004/management/comoonics-clustersuite/python/Attic/setup-ec.py,v $

from distutils.core import setup

setup(name='comoonics-ec-py',
      version='0.1',
      description='Comoonics Enterprisecopy utilities and libraries written in Python',
      long_description=
"""
Comoonics Enterprisecopy utilities and libraries written in Python
""",
      author='Marc Grimme',
      author_email='grimme@atix.de',
      url='http://www.atix.de/comoonics/',
      package_dir =  { 'comoonics.enterprisecopy' : 'lib/comoonics/enterprisecopy'},
      packages=      [ 'comoonics.enterprisecopy' ],
      scripts=['bin/com-ec']
     )

#########################
# $Log: setup-ec.py,v $
# Revision 1.1  2006-07-26 10:04:04  marc
# initial revision
#
# Revision 1.1  2006/07/19 14:30:34  marc
# initial revision
#