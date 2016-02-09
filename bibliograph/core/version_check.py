import re

import subprocess
from pkg_resources import parse_version

from bibliograph.core.utils import bin_search
from bibliograph.core.utils import MissingBinary


version_regex = re.compile('bibutils suite version (.*) date', re.MULTILINE)
_marker = object()


def get_bibutils_version():
    """Return the installed version of the bibutils package, if present"""
    version = None
    try:
        bin_search('bib2xml')
    except MissingBinary:
        pass
    else:
        pipe = subprocess.Popen(
            'bib2xml --version', shell=True, stderr=subprocess.PIPE
        )
        output = pipe.stderr.read()
        matches = version_regex.search(output)
        if matches:
            version = matches.group(1)
    return version


def checkBibutilsVersion(min_version=4.6, bibutils_version=_marker):
    """ Ensure that a certain Bibutils version is installed"""
    # this is purely a hack to allow easier testing
    if bibutils_version is _marker:
        bibutils_version = get_bibutils_version()

    min_version = parse_version(str(min_version))

    try:
        version = parse_version(bibutils_version)
    except AttributeError:
        # bibutils_version is not a string, we can do nothing
        pass
    else:
        if version and version >= min_version:
            return bibutils_version
        else:
            msg = 'Minimum requirement is Bibtutils %s, found %s'
            raise RuntimeError(msg % (min_version, version))

    raise RuntimeError('Unable to determine Bibtutils version')

