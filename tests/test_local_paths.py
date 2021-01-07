import pytest
from page_loader.url import get_filepath


@pytest.mark.parametrize('url, local_path, output', [
    ('http://yandex.ru/',
     '/var/temp',
     '/var/temp/yandex-ru.html'),
    ('https://www.notion.so/14-2-b22045cb63d24a28974dd5d094fddee8',
     '/var/temp/',
     '/var/temp/www-notion-so-14-2-b22045cb63d24a28974dd5d094fddee8.html'),
    ('https://requests-mock.readthedocs.io/_/downloads/en/latest/pdf/',
     '/var/temp',
     '/var/temp/requests-mock-readthedocs-io-downloads-en-latest-pdf.html'),
    ('https://ru.hexlet.io/blog/posts/developers-business-value',
     '/var/temp',
     '/var/temp/ru-hexlet-io-blog-posts-developers-business-value.html'),
    ('https://ru.hexlet.io/projects/50/members/11333/mentor',
     '/var/temp/',
     '/var/temp/ru-hexlet-io-projects-50-members-11333-mentor.html'),
    ])
def test_local_paths(url, local_path, output):
    assert output == get_filepath(url, local_path)
