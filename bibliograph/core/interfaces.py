from zope.interface import Interface
from zope.interface.common.mapping import IIterableMapping
from zope import schema
from zope.schema.interfaces import ITextLine
from zope.schema.vocabulary import SimpleVocabulary

from bibliograph.core.encodings import _python_encodings

# XXX as long as we don't have a propper translation messagefactory
_ = unicode


###############################################################################

class IBibliographyExport(Interface):
    """ Marker interface for a container with
        exportable bibliography elements.
    """

    format = schema.Choice(
        title=_('Export format'),
        required=True,
        default='bibtex',
        vocabulary="bibliography.formats",
        )

    output_encoding = schema.Choice(
        title=_('Encoding of output'),
        required=False,
        vocabulary=SimpleVocabulary.fromValues(_python_encodings)
        )

###############################################################################

_ = unicode

class IBibliography(IIterableMapping):
    """An interface for objects containing IBibliographicReference objects.
    """


class IBibliographyFolder(IBibliography):
    """
    """

    id = schema.TextLine(
        title=_('Id'),
        description=_('The id of the bibliography.'),
        required=True,
        )

    title = schema.TextLine(title=_(u"Title"),
                            description=_(u"Title of the bibliography"),
                            required=True)


class IAuthor(Interface):
    """Represents the author of an IBibliographicReference.
    """

    title = schema.TextLine(
        title=_('Title'),
        description=_('Title of the author.'),
        required=False,
        )

    firstname = schema.TextLine(
        title=_('First name'),
        description=_('The first name(s) of the author.'),
        required=False,
        )

    middlename = schema.TextLine(
        title=_('Middle name'),
        description=_('The middle name(s) of the author.'),
        required=False,
        )

    lastname = schema.TextLine(
        title=_('Last name'),
        description=_('The last name(s) of the author.'),
        required=False,
        )

    prefix = schema.TextLine(
        title=_('Prefix'),
        description=_("Any prefix for the author's name."),
        required=False,
        )

    suffix = schema.TextLine(
        title=_('Suffix'),
        description=_("Any suffix for the author's name."),
        required=False,
        )

    isEditor = schema.Bool(
        title=_('Is editor?'),
        description=_('Indicates whether the author is an editor.'),
        required=False,
        )


class IIdentifier(Interface):
    """
    """

    id = schema.TextLine(
        title=_('Id'),
        description=_('The id of the identifier.'),
        required=True,
        )

    value = schema.TextLine(
        title=_('Value'),
        description=_('The value of the identifier.'),
        required=False,
        )

    def getURL():
        """Return a URL corresponding to the identifier, or None if not
        possible.
        XXX[Perhaps this should be move to a view.]
        """


class IAddress(Interface):
    """
    """

    address = schema.TextLine(
        title=_('Address'),
        description=_('The address of the publisher.'),
        required=False,
        )

class INonStandardPublisherDetails(IAddress):
    """
    """

    institution = schema.TextLine(
        title=_('Institution'),
        description=_("The institution that published the work."),
        required=False,
        )

    howpublished = schema.TextLine(
        title=_('How published'),
        description=_("For publications without a publisher. e.g., an "+
                      "'Institute Report'."),
        required=False,
        )


class IPublisherDetails(IAddress):
    """
    """

    publisher = schema.TextLine(
        title=_('Publisher'),
        description=_('The publisher of this reference.'),
        required=False,
        )


class IPages(Interface):
    """
    """

    pages = schema.TextLine(
        title=_('Pages'),
        description=_("A page number or range of numbers such as '42-111'; "+
                      "you may also have several of these, separating them "+
                      "with commas: '7,41,73-97'."),
        required=False,
        )


class IVolume(Interface):
    """
    """

    def isEditedVolume():
        """Return True if the book is an edited volume.
        """


class IWithinVolume(IPages, IPublisherDetails):
    """
    """

    chapter = schema.TextLine(
        title=_('Chapter'),
        description=_("A chapter number."),
        required=False,
        )

    volumetitle = schema.TextLine(
        title=_('Volume title'),
        description=_("Title of the book, collection or proceedings, that the "+
                      "cited resource is part of."),
        required=False,
        )

    editors = schema.List(
        title=_('Editor(s)'),
        description=_('The editor(s) of the reference.'),
        required=True,
        value_type=schema.Object(IAuthor),
        )


class IBibliographicReference(Interface):
    """An object is renderable as a bibliography.
    """

    id = schema.TextLine(
        title=_('Id'),
        description=_('The id of the reference.'),
        required=True,
        )

    title = schema.TextLine(
        title=_('Title'),
        description=_('The title of the document.'),
        required = True,
        )

    authors = schema.List(
        title=_('Author(s)'),
        description=_('The authors of the reference.'),
        required=False,
        value_type=schema.Object(IAuthor),
        )

    #publication_type = schema.TextLine(
    #    title=_('Publication type'),
    #    description=_('A publication type as found in the bibtex definition'),
    #    required=True,
    #    vocabulary=publication_type_vocab
    #    )

    publication_year = schema.TextLine(
        title=_('Year of publication'),
        required=True,
        )

    publication_month = schema.TextLine(
        title=_('Year of publication'),
        required=False,
        )

    abstract = schema.Text(
        title=_('Abstract'),
        description=_('A short summary of the document'),
        required=False,
        )

    identifiers = schema.List(
        title=_('Identifiers'),
        description=_('A list of identifiers for this reference.'),
        required=False,
        value_type=schema.Object(IIdentifier),
        )
    #identifiers = schema.Dict(
    #    title=_('Identifiers'),
    #    description=_('A dictionary of identifiers for this reference.'),
    #    required=False,
    #    key_type=schema.TextLine(),
    #    value_type=schema.TextLine(),
    #    )

    def getIdentifierById(id, default=None):
        """Return the value for the identifier corresponding to `id', or
        `default' if no such identifier exists.
        """

    url = schema.TextLine(
        title=_('URL of the publication'),
        required=False,
        )

    subject = schema.List(
        title=_('Subject'),
        description=_('A list of tags(subjects) of the document'),
        required=True,
        value_type=schema.Object(ITextLine),
        )

    note = schema.Text(
        title=_('Note'),
        description=_('Some additional notes'),
        required = False,
        )

    annote = schema.Text(
        title=_('Annotation'),
        description=_('Some annotations'),
        required = False,
        )


class IArticleReference(IBibliographicReference, IPages):
    """
    """

    journal = schema.TextLine(
        title=_('Journal'),
        description=_('The journal.'),
        required=False,
        )

    volume = schema.TextLine(
        title=_('Volume'),
        description=_('The journal volume.'),
        required=False,
        )

    issue = schema.TextLine(
        title=_('Issue'),
        description=_('The journal issue.'),
        required=False,
        )


class IBookReference(IBibliographicReference, IPublisherDetails, IVolume):
    """
    """

    edition = schema.TextLine(
        title=_('Edition'),
        description=_('The edition of the book.'),
        required=False,
        )

    series = schema.TextLine(
        title=_('Series'),
        description=_("The name of a series or set of books. When citing an "+
                      "entire book, the 'title' field gives its title and "+
                      "this optional 'series' field gives the name of a "+
                      "series in which the book is published."),
        required=False,
        )


class IBookletReference(IBibliographicReference, IVolume,
                        INonStandardPublisherDetails):
    """
    """


class IConferenceReference(IBibliographicReference):
    """
    """

    organization = schema.TextLine(
        title=_('Organization'),
        description=_("The organization sponsoring a conference, issuing a "+
                      "technical report etc."),
        required=False,
        )

class IInbookReference(IBibliographicReference, IWithinVolume):
    """
    """

class IIncollectionReference(IBibliographicReference, IWithinVolume):
    """
    """

class IInproceedingsReference(IBibliographicReference, IWithinVolume):
    """
    """

class IManualReference(IBibliographicReference):
    """
    """

class IMiscReference(IBibliographicReference):
    """
    """

class IBaseUniversityReference(IAddress):
    """
    """

    school = schema.TextLine(
        title=_('School'),
        description=_("The name of the school (college, university etc.) "+
                      "where a thesis was written."),
        required=False,
        )


class IMasterthesisReference(IBibliographicReference, IBaseUniversityReference):
    """
    """

class IPhdthesisReference(IBibliographicReference, IBaseUniversityReference):
    """
    """

class IProceedingsReference(IBibliographicReference, IVolume):
    """
    """

class ITechreportReference(IBibliographicReference):
    """
    """

class IUnpublishedReference(IBibliographicReference):
    """
    """

class IWebpublishedReference(IBibliographicReference):
    """
    """



# EOF
