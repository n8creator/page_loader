"""Tests for links.py module."""
import os
import pytest
from bs4 import BeautifulSoup
from page_loader.links import filter_links, parse_links, get_full_link
from page_loader.links import get_list_of_links

FIXTURES_PATH = 'tests/fixtures/inputs/'


@pytest.mark.parametrize('fixture, tag, attr, output', [
    ('ru-hexlet-io-professions.html', 'img', 'src',
     ['assets/frontend.png', 'assets/python.png'],),
    ('ru-hexlet-io-professions.html', 'link', 'href',
     ['favicon.ico',
      'assets/application.css',
      'https://ru.hexlet.io/professions',
      'https://en.hexlet.io/professions'],),
    ('ru-hexlet-io-professions.html', 'script', 'src',
     ['assets/application.js',
      'https://js.stripe.com/v3/'],),
])
def test_parse_links(tag, attr, output, fixture):
    data_source = os.path.join(FIXTURES_PATH, fixture)
    with open(data_source, 'r') as f:
        data = f.read()

    soup = BeautifulSoup(data, 'lxml')
    assert output == parse_links(tag, attr, soup)


@pytest.mark.parametrize('url, page_links, output', [
    (
        'https://ru.site.io/about',  # url
        ['https://ru.site.io/about',  # page_links
         'https://en.site.io/about',
         'https://js.stripe.com/v3/',
         '/assets/favicon.ico',
         'assets/application.css',
         '/'],
        ['https://ru.site.io/about',  # output
         '/assets/favicon.ico',
         'assets/application.css',
         '/']
    ),
])
def test_filter_links(url, page_links, output):
    assert output == filter_links(links=page_links, url=url)


@pytest.mark.parametrize('page_url, link, expected_output', [
    ('https://ru.site.io/professions',
     '/assets/favicon.ico',
     'https://ru.site.io/assets/favicon.ico'),
    ('https://localhost/page',
     '/',
     'https://localhost/'),
    ('http://site.com',
     '/cache/style.css?26',
     'http://site.com/cache/style.css?26'),
    ('http://localhost.io',
     'uploads/logo_100x100.png',
     'http://localhost.io/uploads/logo_100x100.png'),
])
def test_get_full_link(page_url, link, expected_output):
    assert expected_output == get_full_link(page_url=page_url, link=link)


@pytest.mark.parametrize('url, fixture, tag_meta, output', [
    ('https://ru.hexlet.io/professions',  # url
     'ru-hexlet-io-professions.html',  # fixture
     {'img': 'src',  # tag_meta
      'link': 'href',
      'script': 'src'},
     [
         ('assets/frontend.png', 'img'),  # output
         ('assets/python.png', 'img'),
         ('favicon.ico', 'link'),
         ('assets/application.css', 'link'),
         ('https://ru.hexlet.io/professions', 'link'),
         ('assets/application.js', 'script'),
     ]
     ),
])
def test_get_list_of_links(fixture, tag_meta, output, url):
    data_file = os.path.join(FIXTURES_PATH, fixture)
    with open(data_file, 'r') as f:
        data = f.read()

    soup = BeautifulSoup(data, 'lxml')
    assert output == get_list_of_links(tag_meta=tag_meta, url=url, soup=soup)
