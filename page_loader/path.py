from urllib.parse import urlparse
import re


def replace_chars(s):
    """Replace all chars to hyphens."""

    s = re.sub(r"[^A-Za-z0-9]", '-', s)  # Replace all chars to hyphens
    s = re.sub(r"\-{2,}", '-', s)  # Replace multiple hyphens in string
    s = re.sub(r"(^\-)|(\-$)", '', s)  # Remove hyphens from start/end of str
    return s


def remove_url_ext(s: str) -> str:
    """Remove extension from the end of string."""

    if re.search(r"\.[^.\/]*$", s):  # Substring after last '.'
        return re.sub(r'\.[^.\/]*$', '', s)
    else:
        return s


def get_ext(s: str) -> str:
    """Get extension from URL."""

    path = parse_url(url=s)['path']
    if re.search(r"(\.[^.\/]*)$", path):  # Get subsring after last '.'
        ext = re.search(r"\.([^.\/]*)$", path)[1]
        if '?' in ext:  # Remove elements from extension ('js?2708' -> 'js')
            ext = ext.split('?')[0]
        return ext

    return 'html'  # Return 'html' if URL does not have extension


def parse_url(url: str) -> dict:
    """Parse URL and split it to parameters."""

    p = urlparse(url)
    return {
        'scheme': p.scheme,
        'netloc': p.netloc,
        'path': p.path,
        'params': p.params,
        'query': p.query,
        'fragment': p.fragment
    }


def url_to_string(url: str) -> str:
    """Convert URL into formatted string."""

    p = parse_url(url)
    output = ''.join([p['netloc'], remove_url_ext(p['path'])])
    return replace_chars(output)


def get_file_name(url: str, ext: str):
    if not ext:
        raise ValueError('Invalid asset value - may not be None or empty')
    return f'{url_to_string(url)}.{ext}'


def get_foldername(url: str):
    return str(url_to_string(url) + '_files')
