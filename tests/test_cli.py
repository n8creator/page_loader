import pytest
from page_loader.cli import get_args
import os


@pytest.mark.parametrize('url, option, output', [
    ('https://ru.hexlet.io/professions', '-o', os.getcwd()),
    ('https://vc.ru/', '--output', '/var/tmp'),
    ])
def test_cli(url, option, output):
    args = get_args([option, output, url])
    assert (url, output) == (args.URL, args.output)
