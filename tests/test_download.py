import tempfile
import requests_mock
from page_loader import download
import os
from page_loader.links import get_full_link


# Read data from file
def get_data(path: str, name: str):
    file = os.path.join(path, name)
    with open(file, 'r', encoding='utf-8') as f:
        data = f.read()
    return data


def get_byte(path: str, name: str):
    file = os.path.join(path, name)
    with open(file, 'rb') as f:
        data = f.read()
    return data


def test_download():
    # Init variables
    url = 'https://ru.hexlet.io/professions'
    source_file = 'inputs/ru-hexlet-io-professions.html'
    expected_file = 'expected/ru-hexlet-io-professions.html'
    fixtures_path = 'tests/fixtures/'

    with tempfile.TemporaryDirectory() as temp_dir:
        with requests_mock.Mocker() as mock:
            # Create mock request for MAIN PAGE
            html_data = get_data(fixtures_path, source_file)
            mock.get('https://ru.hexlet.io/professions', text=html_data)

            # Create mock requests for ALL ASSETS
            assets = [  # Assets as tuples (url_link, asset_path)
                ('assets/frontend.png', 'inputs/assets/frontend.png'),  # noqa
                ('assets/python.png', 'inputs/assets/python.png'),  # noqa
                ('favicon.ico', 'inputs/favicon.ico'),
                ('assets/application.css', 'inputs/assets/application.css'),
                ('https://ru.hexlet.io/professions', 'inputs/ru-hexlet-io-professions.html'),  # noqa
                ('assets/application.js', 'inputs/assets/application.js'),
                ('/', 'inputs/ru-hexlet-io-professions.html'),
            ]
            for link, asset_path in assets:
                mock.get(get_full_link(page_url=url, link=link),
                         content=get_byte(path=fixtures_path, name=asset_path))

            # Download HTML content into temp_dir
            download(url, temp_dir)

            # Assert if output files exists
            output_files = [
                'ru-hexlet-io-professions_files/ru-hexlet-io-assets-frontend.png',  # noqa
                'ru-hexlet-io-professions_files/ru-hexlet-io-assets-python.png',  # noqa
                'ru-hexlet-io-professions_files/ru-hexlet-io-favicon.ico',  # noqa
                'ru-hexlet-io-professions_files/ru-hexlet-io-assets-application.css',  # noqa
                'ru-hexlet-io-professions_files/ru-hexlet-io-professions.html',  # noqa
                'ru-hexlet-io-professions_files/ru-hexlet-io-assets-application.js',  # noqa
                'ru-hexlet-io-professions.html'
            ]
            for file in output_files:
                assert os.path.exists(f'{temp_dir}/{file}') is True  # noqa

            # Assert for expected file output
            expected_data = get_data(fixtures_path, expected_file)
            downloaded_data = get_data(temp_dir, 'ru-hexlet-io-professions.html')  # noqa
            # print(downloaded_data)
            assert expected_data == downloaded_data
