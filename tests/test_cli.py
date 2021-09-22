import pytest
from page_loader.cli import get_args
import os


@pytest.mark.parametrize('url, option, output', [
    ('https://site.io/blog', '-o', os.getcwd()),
    ('http://localhost/', '--output', '/var/tmp'),
])
def test_cli(url, option, output):
    args = get_args([option, output, url])
    assert (url, output) == (args.URL, args.output)
