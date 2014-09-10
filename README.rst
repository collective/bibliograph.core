bibliograph.core
================

Overview
--------

This package defines common elements used by the packages sharing the
`bibliograph` namespace:

* `bibliograph.parsing <https://github.com/collective/bibliograph.parsing/>`_
* `bibliograph.rendering <https://github.com/collective/bibliograph.rendering/>`_

A few interfaces are defined:

IBibliographicReference
  an interface for a single content object with a given schema which can be
  rendered as a bibliographic entry (bibtex, endnote, ris, etc.)

IBibliographyExport
  is a marker for a container directly containing single exportable
  IBibliographicReference objects

IAuthor
  an interface for a single content object with a given schema which represents
  the author (or possibly the editor) of a bibliographic work

IBibliography
  An interface for containers which contain IBibliographicReference objects


This package also provides utility methods and a collection of encodings used
within python and latex.  A mapping of utf8 characters to equivalent latex
entities is also included.

A utility method `bin_search` is included. It acts like the `which`-command on
posix systems. It returns the full path of an executeable command, if it is
found in the PATH environment variable.

You may overload the PATH environment variable with another environment
variable: BIBUTILS_PATH. Executeables in this location will be found as well.

Resources
---------

- Homepage: http://pypi.python.org/pypi/bibliograph.core
- Code repository: https://github.com/collective/bibliograph.core

Contributors
------------

- Tom Gross, itconsense@gmail.com, Author
- Raphael Ritz, r.ritz@biologie.hu-berlin.de, Renderers
- Andreas Jung, info@zopyx.com, bugfixes
