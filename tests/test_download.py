import os
import pytest
import tempfile
import requests_mock
from pathlib import PurePath as PP
from page_loader import download
from page_loader.file import read_file
from page_loader.links import get_absolute_link


URL = 'https://ru.hexlet.io/professions'
FIXTURES_PATH = PP('tests/fixtures/')

INPUT_FIXTURE = PP('inputs/ru-hexlet-io-professions.html')
INPUT_ASSETS = [  # (asset_hyperlink, asset_local_path)
    ('assets/frontend.png', PP('inputs/assets/frontend.png')),
    ('assets/python.png', PP('inputs/assets/python.png')),
    ('favicon.ico', PP('inputs/favicon.ico')),
    ('assets/application.css', PP('inputs/assets/application.css')),
    ('https://ru.hexlet.io/professions', PP('inputs/ru-hexlet-io-professions.html')),  ## noqa
    ('assets/application.js', PP('inputs/assets/application.js')),
    ('/', PP('inputs/ru-hexlet-io-professions.html')),
]

EXPECTED_FIXTURE = PP('expected/ru-hexlet-io-professions.html')
EXPECTED_FILENAME = PP('ru-hexlet-io-professions.html')
EXPECTED_ASSETS = [
    PP('ru-hexlet-io-professions_files/ru-hexlet-io-assets-frontend.png'),
    PP('ru-hexlet-io-professions_files/ru-hexlet-io-assets-python.png'),
    PP('ru-hexlet-io-professions_files/ru-hexlet-io-favicon.ico'),
    PP('ru-hexlet-io-professions_files/ru-hexlet-io-assets-application.css'),
    PP('ru-hexlet-io-professions_files/ru-hexlet-io-professions.html'),
    PP('ru-hexlet-io-professions_files/ru-hexlet-io-assets-application.js'),
    PP('ru-hexlet-io-professions.html'),
]


def test_download():
    with tempfile.TemporaryDirectory() as temp_dir:
        with requests_mock.Mocker() as mock:
            # create mock for main html page
            html = read_file(os.path.join(FIXTURES_PATH, INPUT_FIXTURE))
            mock.get(URL, text=html)

            # create mock's for all assets
            for hyperlink, local_path in INPUT_ASSETS:
                asset_hyperlink = get_absolute_link(
                    page_url=URL, local_link=hyperlink)

                asset_fixture_path = os.path.join(FIXTURES_PATH, local_path)
                bytecode = read_file(file_path=asset_fixture_path, mode='rb')
                mock.get(asset_hyperlink, content=bytecode)

            # download page from URL
            download(URL, temp_dir)

            # assert if downloaded html in 'tmp' folder equals expected in fixtures
            expected = read_file(os.path.join(FIXTURES_PATH, EXPECTED_FIXTURE))
            downloaded = read_file(os.path.join(temp_dir, EXPECTED_FILENAME))
            assert expected == downloaded

            # assert if expected assets exists in temp folder
            for asset in EXPECTED_ASSETS:
                assert os.path.exists(f'{temp_dir}/{asset}') is True


@pytest.mark.parametrize('status_code', [
    400, 404, 500, 503
])
def test_http_status(requests_mock, tmpdir, status_code):
    requests_mock.get(URL, status_code=status_code)
    with pytest.raises(Exception):
        download(URL, tmpdir)
