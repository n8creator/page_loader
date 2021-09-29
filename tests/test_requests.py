import os
import pytest
import requests

FIX_PATH = 'tests/fixtures/inputs/'


@pytest.mark.parametrize('url, fixture', [
    ('https://ru.hexlet.io/professions', 'ru-hexlet-io-professions.html')
])
def test_requests(requests_mock, url, fixture):
    data_file = os.path.join(FIX_PATH, fixture)
    with open(data_file, 'r') as f:
        data = f.read()

    requests_mock.get(url, text=data)
    assert data == requests.get(url).text
