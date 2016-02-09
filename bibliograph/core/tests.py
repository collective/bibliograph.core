import unittest, doctest

from zope.testing import doctestunit
from zope.component import testing
from zope.component import provideUtility
from zope.component import getUtility

from zope.schema.interfaces import IVocabularyFactory

from bibliograph.core.vocabulary import BibFormatVocabularyFactory

class DummyEntry(object):

    def __init__(self, id=None):
        self.id = id

    def getId(self):
        return self.id

class VocabularyTestCase(unittest.TestCase):

    def setUp(self):
        provideUtility(BibFormatVocabularyFactory,
                       IVocabularyFactory,
                       u'bibliography.formats')

    def test_formatsvoc(self):
        voc = getUtility(IVocabularyFactory, u'bibliography.formats')(object())
        assert 'bibtex' in voc


class VersionCheckTestCase(unittest.TestCase):

    def _call_FUT(self, bibutils_version):
        from bibliograph.core.version_check import checkBibutilsVersion
        return checkBibutilsVersion(bibutils_version=bibutils_version)

    def test_lower_numeric_versions(self):
        """assert that numeric versions less than the minimum are rejected"""
        versions = ['3.0', '3.12', '4.1']
        for version in versions:
            self.assertRaises(RuntimeError, self._call_FUT, version)

    def test_higher_numeric_versions(self):
        versions = ['4.12', '5.1', '5.12']
        for version in versions:
            self.assertEqual(self._call_FUT(version), version)

    def test_no_bibutils_version(self):
        self.assertRaises(RuntimeError, self._call_FUT, None)

    def test_invalid_version(self):
        self.assertRaises(RuntimeError, self._call_FUT, 'iamnotaversion')


def test_suite():
    return unittest.TestSuite([

        # Gather doctests from package files
        doctestunit.DocTestSuite(
            'bibliograph.core.utils',
            optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE,
            globs=dict(DummyEntry=DummyEntry)),
        doctestunit.DocTestSuite(
            'bibliograph.core.bibutils',
            optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE),
        unittest.makeSuite(VocabularyTestCase),
        unittest.makeSuite(VersionCheckTestCase),
        ])


if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
