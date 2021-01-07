"""Module converting URL into readable string or filename."""
from urllib.parse import urlparse
import re


def replace_chars(s):
    """Replace chars to hyphens.

    Args:
        s ([str]): string containing some chars, like:
                   "https://python.org/3/library/exceptions.html"

    Returns:
        [str]: string with chars replaced to hyphens, like:
               "https-python-org-3-library-exceptions-html"
    """
    # Replace all chars to hyphens
    s = re.sub(r"[^A-Za-z0-9]", '-', s)

    # Replace multiple hyphens in string
    s = re.sub(r"\-{2,}", '-', s)

    # Remove unneccessary hyphen from the start & end of the string
    s = re.sub(r"(^\-)|(\-$)", '', s)

    return s


def remove_html(s):
    """Remove unnecessary `html` from the end of line.

    Args:
        s ([str]): some string that may contain `html` in the end of line,
                   like: "https-python-org-3-library-exceptions-html"

    Returns:
        [str]: string without `html` in the end of line, like:
               "https-python-org-3-library-exceptions"
    """
    if re.search(r"\-?html$", s) is not None:
        return re.sub(r'\-?html$', '', s)
    else:
        return s


def convert_url(url):
    """Convert URL into readable string without unnescessary chars & elements.

    Args:
        url ([str]): url, like "https://python.org/3/library/exceptions.html"

    Returns:
        [type]: string containing URL netloc and path without any chars &
                unnecessary elements, like: "python-org-3-library-exceptions"
    """
    output = ''

    # Parse url into elements (scheme, netloc, path, params, query, fragment)
    # and generare string containing netlock & path only
    p = urlparse(url)
    if p.netloc:
        output += p.netloc
    if p.path:
        output += p.path

    return remove_html(replace_chars(output))


def url_to_filename(url):
    """Convert URL into filename which may be saved on disk.

    Args:
        url ([str]): url, like "https://python.org/3/library/exceptions.html"

    Returns:
        [str]: filename, like: "python-org-3-library-exceptions.html"
    """
    return str(convert_url(url) + '.html')
