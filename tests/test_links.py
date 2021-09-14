"""Tests for links.py module."""
import os
import pytest
from page_loader.links import filter_links, parse_links, get_full_link,\
    get_list_of_links
from bs4 import BeautifulSoup


# Test for parse_links()
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
                      '/',
                      'https://en.hexlet.io/professions']),
    ('script', 'src', ['assets/application.js',
                       'https://js.stripe.com/v3/',
                       'https://cdn2.hexlet.io/assets/application-d9ee2c2029a7654c0bf98a128c9fee0c5977c69a56cd83fc097947e55215f6c1.js',  # noqa E501
                       'https://cdn2.hexlet.io/packs/js/runtime-b95232761668dd8b1100.js',  # noqa E501
                       'https://cdn2.hexlet.io/packs/js/vendors~application-03cf108a36d337212e5b.chunk.js',  # noqa E501
                       'https://cdn2.hexlet.io/packs/js/application-6d2cae17d8f39090c064.chunk.js']),  # noqa E501
])
def test_parse_links(tag, attr, output):
    # Get fixture data
    data_source = 'tests/fixtures/ru-hexlet-io-professions.html'
    with open(data_source, 'r') as f:
        data = f.read()

    # Create BeautifulSoup object
    soup = BeautifulSoup(data, 'lxml')

    # Make assert
    assert output == parse_links(tag, attr, soup)


# Test for filter_links() function
@pytest.mark.parametrize('page_links, url, output', [
    ([
        '/assets/favicon.ico',
        'assets/application.css',
        'https://ru.hexlet.io/professions',
        'https://en.hexlet.io/professions',
        'https://js.stripe.com/v3/',
        '/'
    ],
        'https://ru.hexlet.io/professions',
        [
        '/assets/favicon.ico',
        'assets/application.css',
        'https://ru.hexlet.io/professions',
        '/'
    ]),
])
def test_filter_links(page_links, url, output):
    # Make assert
    assert output == filter_links(links=page_links, url=url)


# Test for get_full_link()
@pytest.mark.parametrize('page_url, link, output', [
    ('https://ru.hexlet.io/professions',
     '/assets/favicon.ico',
     'https://ru.hexlet.io/assets/favicon.ico'),
    ('https://ru.hexlet.io/professions',
     '/',
     'https://ru.hexlet.io/'),
    ('http://site.com',
     '/templates/cache/3d7e3f272a5ba13469e1154aa47f1.css?2689',
     'http://site.com/templates/cache/3d7e3f272a5ba13469e1154aa47f1.css?2689'),
    ('https://smart-lab.ru',
     'uploads/logo_company_IDF-eurasia_100x100.png',
     'https://smart-lab.ru/uploads/logo_company_IDF-eurasia_100x100.png'),  # noqa
])
def test_get_full_link(page_url, link, output):
    # Make assert
    assert output == get_full_link(page_url=page_url, link=link)


# Test for get_list_of_links()
@pytest.mark.parametrize('fixture, tag_meta, output, url', [
    ('ru-hexlet-io-professions.html',
     {'img': 'src', 'link': 'href', 'script': 'src'},
     [('assets/professions/frontend.png', 'img'),
      ('assets/professions/python.png', 'img'),
      ('assets/professions/php.png', 'img'),
      ('assets/professions/backend.png', 'img'),
      ('assets/professions/layout-designer.png', 'img'),
      ('assets/professions/java.png', 'img'),
      ('assets/favicon.ico', 'link'),
      ('assets/application.css', 'link'),
      ('https://ru.hexlet.io/lessons.rss', 'link'),
      ('https://ru.hexlet.io/professions', 'link'),
      ('/', 'link'),
      ('assets/application.js', 'script')],
     'https://ru.hexlet.io/professions'),
])
def test_get_list_of_links(fixture, tag_meta, output, url):

    # Generate Paths to Fixture File
    args_path = 'tests/fixtures/'
    data_file = os.path.join(args_path, fixture)

    # Load data from fixture file into variable
    with open(data_file, 'r') as f:
        data = f.read()

    # Generate BeautifulSoup Object
    soup = BeautifulSoup(data, 'lxml')

    # Make assert
    assert output == get_list_of_links(tag_meta=tag_meta, url=url, soup=soup)
