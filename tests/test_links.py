"""Tests for links.py module."""
import os
import pytest
from bs4 import BeautifulSoup
from page_loader.links import filter_links, parse_links, get_absolute_link
from page_loader.links import get_links

FIXTURES_PATH = 'tests/fixtures/inputs/'


@pytest.mark.parametrize('fixture, tag, attr, output', [
    ('ru-hexlet-io-professions.html', 'img', 'src',
     ['assets/frontend.png',
      'assets/python.png'],),
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


@pytest.mark.parametrize('page_url, link, expected', [
    ('https://site.io/page',
     '/assets/favicon.ico',
     'https://site.io/assets/favicon.ico'),
    ('https://site.io/page',
     '/',
     'https://site.io/'),
    ('http://site.io',
     '/cache/style.css?26',
     'http://site.io/cache/style.css?26'),
    ('http://site.io',
     'http://site.io/uploads/logo_100x100.png',
     'http://site.io/uploads/logo_100x100.png'),
])
def test_get_absolute_link(page_url, link, expected):
    assert expected == get_absolute_link(page_url=page_url, local_link=link)


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
def test_get_links(fixture, tag_meta, output, url):
    data_file = os.path.join(FIXTURES_PATH, fixture)
    with open(data_file, 'r') as f:
        data = f.read()

    soup = BeautifulSoup(data, 'lxml')
    assert output == get_links(tag_meta=tag_meta, url=url, soup=soup)
