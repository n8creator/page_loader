from urllib.parse import urlparse
import re


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


def replace_chars(s):
    """Replace all chars in string to hyphens."""
    s = re.sub(r"[^A-Za-z0-9]", '-', s)  # Replace all chars to hyphens
    s = re.sub(r"\-{2,}", '-', s)  # Replace multiple hyphens
    s = re.sub(r"(^\-)|(\-$)", '', s)  # Remove hyphens from start/end
    return s


def split_path_and_ext(path: str) -> dict:
    """Split URL path into 'path without extension' and 'extension'."""
    pattern = r'\.[^.\/]*$'  # pattern to find substing after last '.'

    # Get path without extension
    if re.search(pattern, path):
        path_without_ext = re.sub(pattern, '', path)
    else:
        path_without_ext = path

    # Get extension or return 'html' by default
    if re.search(pattern, path):
        extension = re.search(r'\.([^.\/]*)$', path)[1]
        if '?' in extension:  # Remove elements from ext ('js?2708' -> 'js')
            extension = extension.split('?')[0]
    else:
        extension = 'html'

    return {
        'path': path_without_ext,
        'ext': extension
    }


def url_to_string(url: str) -> str:
    """Convert URL into formatted string."""
    p = parse_url(url)
    path_without_ext = split_path_and_ext(p['path'])['path']
    output = ''.join([p['netloc'], path_without_ext])
    return replace_chars(output)


def get_local_name(url: str, mode, ext: str = 'html'):
    """Return local name for file or for a folder with extension."""
    if mode == 'file':
        return f'{url_to_string(url)}.{ext}'
    if mode == 'folder':
        return f'{url_to_string(url)}_files'
