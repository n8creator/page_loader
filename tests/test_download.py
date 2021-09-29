import os
import tempfile
import requests_mock
from page_loader import download
from page_loader.file import read_file
from page_loader.links import get_full_link


URL = 'https://ru.hexlet.io/professions'
FIXTURES_PATH = 'tests/fixtures/'

INPUT_FIXTURE = 'inputs/ru-hexlet-io-professions.html'
INPUT_ASSETS = [  # (asset_hyperlink, asset_local_path)
    ('assets/frontend.png', 'inputs/assets/frontend.png'),
    ('assets/python.png', 'inputs/assets/python.png'),
    ('favicon.ico', 'inputs/favicon.ico'),
    ('assets/application.css', 'inputs/assets/application.css'),
    ('https://ru.hexlet.io/professions', 'inputs/ru-hexlet-io-professions.html'),  # noqa
    ('assets/application.js', 'inputs/assets/application.js'),
    ('/', 'inputs/ru-hexlet-io-professions.html'),
]

EXPECTED_FIXTURE = 'expected/ru-hexlet-io-professions.html'
EXPECTED_FILENAME = 'ru-hexlet-io-professions.html'
EXPECTED_ASSETS = [
    'ru-hexlet-io-professions_files/ru-hexlet-io-assets-frontend.png',
    'ru-hexlet-io-professions_files/ru-hexlet-io-assets-python.png',
    'ru-hexlet-io-professions_files/ru-hexlet-io-favicon.ico',
    'ru-hexlet-io-professions_files/ru-hexlet-io-assets-application.css',
    'ru-hexlet-io-professions_files/ru-hexlet-io-professions.html',
    'ru-hexlet-io-professions_files/ru-hexlet-io-assets-application.js',
    'ru-hexlet-io-professions.html'
]


def test_download():
    with tempfile.TemporaryDirectory() as temp_dir:
        with requests_mock.Mocker() as mock:
            # create mock for main html page
            html = read_file(os.path.join(FIXTURES_PATH, INPUT_FIXTURE))
            mock.get('https://ru.hexlet.io/professions', text=html)

            # create mock's for all assets
            for hyperlink, local_path in INPUT_ASSETS:
                asset_hyperlink = get_full_link(page_url=URL, link=hyperlink)

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
