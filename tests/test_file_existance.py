import pytest
import tempfile
from page_loader import download
from page_loader.url import url_to_filename
import os


@pytest.mark.parametrize('url', [
    ('https://requests-mock.readthedocs.io/_/downloads/en/latest/pdf/'),
    ('https://ru.hexlet.io/professions'),
    ('https://ru.hexlet.io/courses'),
    ('https://www.finanz.ru/'),
    ('https://vc.ru/'),
    ])
def test_file_existance(url):
    with tempfile.TemporaryDirectory() as temp_dir:
        # Generate file_name from given URL
        file_name = url_to_filename(url)

        # Download HTML content into temp_dir
        download(url, temp_dir)

        # Make assert
        assert os.path.exists(f'{temp_dir}/{file_name}') == True  # noqa E712
