from zope.interface import implements
from zope.schema.fieldproperty import FieldProperty
#from zope.component.factory import Factory

from interfaces import IAuthor
from interfaces import IIdentifier
from interfaces import IAddress
from interfaces import IVolume
from interfaces import IWithinVolume
from interfaces import IPublisherDetails
from interfaces import INonStandardPublisherDetails
from interfaces import IPages
from interfaces import IBibliographicReference
from interfaces import IArticleReference
from interfaces import IBookReference
from interfaces import IBookletReference
from interfaces import IConferenceReference
from interfaces import IInbookReference
from interfaces import IIncollectionReference
from interfaces import IInproceedingsReference
from interfaces import IManualReference
from interfaces import IMiscReference
from interfaces import IBaseUniversityReference
from interfaces import IMasterthesisReference
from interfaces import IPhdthesisReference
from interfaces import IProceedingsReference
from interfaces import ITechreportReference
from interfaces import IUnpublishedReference
from interfaces import IWebpublishedReference

from utils import FieldPropertyWithDefault

# XXX as long as we don't have a propper translation messagefactory
_ = unicode


class Author(object):
    """
    """
    implements(IAuthor)
    
    firstname = FieldProperty(IAuthor['firstname'])
    middlename = FieldProperty(IAuthor['middlename'])
    lastname = FieldProperty(IAuthor['lastname'])
    prefix = FieldProperty(IAuthor['prefix'])
    suffix = FieldProperty(IAuthor['suffix'])
    isEditor = FieldProperty(IAuthor['isEditor'])


class Identifier(object):
    """
    """
    implements(IIdentifier)

    id = FieldProperty(IIdentifier['id'])
    value = FieldProperty(IIdentifier['value'])

    def getURL(self):
        """
        """
        return 'http://www.example.com/'


class Pages(object):
    """
    """
    implements(IPages)

    pages = FieldProperty(IPages['pages'])


class Volume(object):
    """
    """

    def isEditedVolume(self):
        """Return True if the book is an edited volume.
        """
        for author in self.authors:
            if author.isEditor:
                return True
        return False


class WithinVolume(Pages):
    """
    """
    implements(IWithinVolume)

    chapter = FieldProperty(IWithinVolume['chapter'])
    volumetitle = FieldProperty(IWithinVolume['volumetitle'])
    editors = FieldPropertyWithDefault(IWithinVolume['editors'], default=list)


class Address(object):
    """
    """
    implements(IAddress)

    address = FieldProperty(IAddress['address'])


class NonStandardPublisherDetails(Address):
    """
    """
    implements(INonStandardPublisherDetails)

    institution = FieldProperty(INonStandardPublisherDetails['institution'])
    howpublished = FieldProperty(INonStandardPublisherDetails['howpublished'])


class PublisherDetails(Address):
    """
    """
    implements(IPublisherDetails)

    publisher = FieldProperty(IPublisherDetails['publisher'])


class BibliographicReference(object):
    """An object is renderable as a bibliography.
    """
    implements(IBibliographicReference)
    
    id = FieldProperty(IBibliographicReference['id'])
    title = FieldProperty(IBibliographicReference['title'])
    authors = FieldPropertyWithDefault(IBibliographicReference['authors'],
                                       default=list)
    publication_year = FieldProperty(IBibliographicReference['publication_year'])
    publication_month = FieldProperty(IBibliographicReference['publication_month'])
    abstract = FieldProperty(IBibliographicReference['abstract'])
    identifiers = FieldPropertyWithDefault(IBibliographicReference['identifiers'],
                                           default=list)
    url = FieldProperty(IBibliographicReference['url'])
    subject = FieldPropertyWithDefault(IBibliographicReference['subject'],
                                       default=list)
    note = FieldProperty(IBibliographicReference['note'])
    annote = FieldProperty(IBibliographicReference['annote'])

    def getIdentifierById(self, id, default=None):
        """
        """
        for each in self.identifiers:
            if each.id == id:
                return each.value
        return default


class ArticleReference(BibliographicReference, Pages):
    """
    """

    implements(IArticleReference)
    portal_type = 'ArticleReference'
    publication_type = 'article'

    journal = FieldProperty(IArticleReference['journal'])
    volume = FieldProperty(IArticleReference['volume'])
    issue = FieldProperty(IArticleReference['issue'])


class BookReference(BibliographicReference, PublisherDetails, Volume):
    """
    """

    implements(IBookReference)
    portal_type = 'BookReference'
    publication_type = 'book'

    edition = FieldProperty(IBookReference['edition'])
    series = FieldProperty(IBookReference['series'])


class BookletReference(BibliographicReference,
                       NonStandardPublisherDetails,
                       Volume):
    """
    """

    implements(IBookletReference)
    portal_type = 'BookletReference'
    publication_type = 'booklet'


class ConferenceReference(BibliographicReference):
    """
    """

    implements(IConferenceReference)
    portal_type = 'ConferenceReference'
    publication_type = 'conference'

    organization = FieldProperty(IConferenceReference['organization'])


class InbookReference(BibliographicReference, WithinVolume):
    """
    """

    implements(IInbookReference)
    portal_type = 'InbookReference'
    publication_type = 'inbook'


class IncollectionReference(BibliographicReference, WithinVolume):
    """
    """

    implements(IIncollectionReference)
    portal_type = 'IncollectionReference'
    publication_type = 'incollection'


class InproceedingsReference(BibliographicReference, WithinVolume):
    """
    """

    implements(IInproceedingsReference)
    portal_type = 'InproceedingsReference'
    publication_type = 'inproceenings'


class ManualReference(BibliographicReference):
    """
    """

    implements(IManualReference)
    portal_type = 'ManualReference'
    publication_type = 'manual'


class MiscReference(BibliographicReference):
    """
    """

    implements(IMiscReference)
    portal_type = 'MiscReference'
    publication_type = 'misc'


class BaseUniversityReference(object):
    """
    """

    school = FieldProperty(IBaseUniversityReference['school'])


class MasterthesisReference(BibliographicReference, BaseUniversityReference):
    """
    """

    implements(IMasterthesisReference)
    portal_type = 'MasterthesisReference'
    publication_type = 'masterthesis'


class PhdthesisReference(BibliographicReference, BaseUniversityReference):
    """
    """

    implements(IPhdthesisReference)
    portal_type = 'PhdthesisReference'
    publication_type = 'phdthesis'


class ProceedingsReference(BibliographicReference, Volume):
    """
    """

    implements(IProceedingsReference)
    portal_type = 'ProceedingsReference'
    publication_type = 'proceedings'


class TechreportReference(BibliographicReference):
    """
    """

    implements(ITechreportReference)
    portal_type = 'TechreportReference'
    publication_type = 'techreport'


class UnpublishedReference(BibliographicReference):
    """
    """

    implements(IUnpublishedReference)
    portal_type = 'UnpublishedReference'
    publication_type = 'unpublished'


class WebpublishedReference(BibliographicReference):
    """
    """

    implements(IWebpublishedReference)
    portal_type = 'WebpublishedReference'
    publication_type = 'webpublished'

