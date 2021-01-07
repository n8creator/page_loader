"""Module makes request to some URL and returns HTML code."""
import requests
import sys


def get_html(url):
    """Make request and return HTML or exit depending on the response code.

    Args:
        url ([str]): URL as a string

    Returns:
        [str]: string containing HTML code
    """
    r = requests.get(url)

    if r.ok:  # 200
        return r.text
    else:  # 40x, 30x, 50x
        sys.exit(f'Request returned {r.status_code}. Process was stopped.')
