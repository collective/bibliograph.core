# -*- coding: utf-8 -*-
###############################################################################
# $Copy$
###############################################################################
""" Vocabularies used by the bibliograph.* packages

$Id$
"""
__docformat__ = 'reStructuredText'
__author__  = 'Tom Gross <itconsense@gmail.com>'

import sys

# Zope imports
from zope.interface import implementer
from zope.schema.vocabulary import SimpleVocabulary

from zope.schema.interfaces import IVocabularyFactory

# XXX as long as we don't have a propper translation messagefactory
if sys.version_info[0] == 2:
    _ = unicode
else:
    _ = str

###############################################################################

@implementer(IVocabularyFactory)
class BibFormatVocabulary(object):
    """ A vocabulary for bibliographic formats
    """

    def __call__(self, context):
        """ A simple constant vocabulary """
        return SimpleVocabulary.fromItems([
            (_("Bibtex"), 'bibtex'),
            (_("Endnote"), 'endnote'),
            (_("RIS"), 'ris'),
            (_("XML (MODS)"), 'xml'),
            (_("PDF"), 'pdf'),
        ])

BibFormatVocabularyFactory = BibFormatVocabulary()
