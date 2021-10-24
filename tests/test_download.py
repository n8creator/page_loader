import os
import pytest
import tempfile
import requests_mock
from page_loader.file import get_full_path
from pathlib import PurePath as PP
from page_loader import download
from page_loader.links import get_abs_link


URL = 'https://ru.hexlet.io/professions'
FIXTURES_PATH = PP('tests/fixtures/')

INPUT_FIXTURE = PP('inputs/ru-hexlet-io-professions.html')
EXPECTED_FIXTURE = PP('expected/ru-hexlet-io-professions.html')
EXPECTED_FILENAME = PP('ru-hexlet-io-professions.html')

ASSETS = [  # (link, fixture_path, expected_file)
    ('assets/frontend.png',
     PP('inputs/assets/frontend.png'),
     PP('ru-hexlet-io-professions_files/ru-hexlet-io-assets-frontend.png'),
     ),
    ('assets/python.png',
     PP('inputs/assets/python.png'),
     PP('ru-hexlet-io-professions_files/ru-hexlet-io-assets-python.png'),
     ),
    ('favicon.ico',
     PP('inputs/favicon.ico'),
     PP('ru-hexlet-io-professions_files/ru-hexlet-io-favicon.ico'),
     ),
    ('assets/application.css',
     PP('inputs/assets/application.css'),
     PP('ru-hexlet-io-professions_files/ru-hexlet-io-assets-application.css'),
     ),
    ('https://ru.hexlet.io/professions',
     PP('inputs/ru-hexlet-io-professions.html'),
     PP('ru-hexlet-io-professions_files/ru-hexlet-io-professions.html'),
     ),
    ('assets/application.js',
     PP('inputs/assets/application.js'),
     PP('ru-hexlet-io-professions_files/ru-hexlet-io-assets-application.js'),
     ),
]


def read_file(file_path, mode='r', encoding=None):
    """Read & return data from some file at given 'file_path'."""
    with open(file_path, mode, encoding=encoding) as file:
        data = file.read()
    return data


def test_download():
    with tempfile.TemporaryDirectory() as temp_dir:
        with requests_mock.Mocker() as mock:
            # create mock for main html page
            html = read_file(os.path.join(FIXTURES_PATH, INPUT_FIXTURE))
            mock.get(URL, text=html)

            # create mock's for all assets
            for link, fixture_path, _ in ASSETS:
                asset_link = get_abs_link(page_url=URL, local_link=link)

                asset_fixture_path = os.path.join(FIXTURES_PATH, fixture_path)
                bytecode = read_file(file_path=asset_fixture_path, mode='rb')
                mock.get(asset_link, content=bytecode)

            # download page from URL
            download(URL, temp_dir)

            # assert if downloaded html in temp folder equals expected in fixtures
            expected = read_file(os.path.join(FIXTURES_PATH, EXPECTED_FIXTURE))
            downloaded = read_file(os.path.join(temp_dir, EXPECTED_FILENAME))
            assert expected == downloaded

            # assert if expected assets exists in temp folder
            for _, _, expected_file in ASSETS:
                assert os.path.exists(f'{temp_dir}/{expected_file}') is True

            # assert if asset's content equals to asset's fixture
            for _, fixture_path, expected_file in ASSETS:
                fixture = read_file(get_full_path(FIXTURES_PATH, fixture_path),
                                    mode='rb')
                expected = read_file(get_full_path(temp_dir, expected_file),
                                     mode='rb')
                assert fixture == expected


@pytest.mark.parametrize('status_code', [
    400, 404, 500, 503
])
def test_http_status(requests_mock, tmpdir, status_code):
    requests_mock.get(URL, status_code=status_code)
    with pytest.raises(Exception):
        download(URL, tmpdir)
