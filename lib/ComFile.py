""" Comoonics file module


here should be some more information about the module, that finds its way inot the onlinedoc

"""


# here is some internal information
# $Id: ComFile.py,v 1.1 2006-06-30 08:01:25 mark Exp $
#


__version__ = "$Revision: 1.1 $"
# $Source: /atix/ATIX/CVSROOT/nashead2004/management/comoonics-clustersuite/python/lib/Attic/ComFile.py,v $

from ComDataObject import DataObject


class File(DataObject):
    """ Base Class for all source and destination objects"""
    def __init__(self, element, doc):
        DataObject.__init__(self, element, doc)
        
# $Log: ComFile.py,v $
# Revision 1.1  2006-06-30 08:01:25  mark
# initial checkin
#
