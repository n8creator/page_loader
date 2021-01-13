"""Tests for links.py module."""
import pytest
from page_loader.links import filter_links, get_links
from bs4 import BeautifulSoup


# Test for filter_links() function
@pytest.mark.parametrize('page_links, url, output', [
    ([
        '/assets/favicon.ico',
        'assets/application.css',
        'https://ru.hexlet.io/professions',
        'https://en.hexlet.io/professions',
        'https://js.stripe.com/v3/',

      ],
     'https://ru.hexlet.io/professions',
     [
         '/assets/favicon.ico',
         '/assets/application.css',
         '/professions'

     ]),
    ])
def test_filter_links(page_links, url, output):
    # Make assert
    assert output == filter_links(links=page_links, url=url)


# Test for get_links()
@pytest.mark.parametrize('tag, attr, output', [
    ('img', 'src', ['assets/professions/frontend.png',
                    'assets/professions/python.png',
                    'assets/professions/php.png',
                    'assets/professions/backend.png',
                    'assets/professions/layout-designer.png',
                    'assets/professions/java.png']),
    ('link', 'href', ['assets/favicon.ico',
                      'assets/application.css',
                      'https://ru.hexlet.io/lessons.rss',
                      'https://ru.hexlet.io/professions',
                      'https://en.hexlet.io/professions']),
    ('script', 'src', ['assets/application.js',
                       'https://js.stripe.com/v3/',
                       'https://cdn2.hexlet.io/assets/application-d9ee2c2029a7654c0bf98a128c9fee0c5977c69a56cd83fc097947e55215f6c1.js', # noqa E501
                       'https://cdn2.hexlet.io/packs/js/runtime-b95232761668dd8b1100.js', # noqa E501
                       'https://cdn2.hexlet.io/packs/js/vendors~application-03cf108a36d337212e5b.chunk.js', # noqa E501
                       'https://cdn2.hexlet.io/packs/js/application-6d2cae17d8f39090c064.chunk.js']), # noqa E501
])
def test_get_links(tag, attr, output):
    # Get fixture data
    data_source = 'tests/fixtures/ru-hexlet-io-professions.html'
    with open(data_source, 'r') as f:
        data = f.read()

    # Create BeautifulSoup object
    soup = BeautifulSoup(data, 'lxml')

    # Make assert
    assert output == get_links(tag, attr, soup)
