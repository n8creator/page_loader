import pytest
from page_loader.file import read_file
from page_loader.path import get_full_path
from page_loader.loader import make_request
from requests.exceptions import HTTPError

FIX_PATH = 'tests/fixtures/inputs/'
URL = 'https://ru.hexlet.io/professions'


@pytest.mark.parametrize('url, fixture', [
    ('https://ru.hexlet.io/professions', 'ru-hexlet-io-professions.html')
])
def test_requests(requests_mock, url, fixture):
    bytecode = read_file(get_full_path(FIX_PATH, fixture), mode='rb')
    requests_mock.get(url, content=bytecode)
    assert bytecode == make_request(url=url)


@pytest.mark.parametrize('status_code', [
    404, 500
])
def test_requests_http_error(requests_mock, status_code):
    requests_mock.get(URL, status_code=status_code)
    with pytest.raises(HTTPError):
        make_request(url=URL)
