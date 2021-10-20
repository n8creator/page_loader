"""Tests for links.py module."""
import os
import pytest
from bs4 import BeautifulSoup
from page_loader.links import get_abs_link
from page_loader.links import get_links, filter_links_in_domain

FIXTURES_PATH = 'tests/fixtures/inputs/'


@pytest.mark.parametrize('url, links_tags, output', [
    (
        'https://ru.hexlet.io/professions',
        [('assets/frontend.png', 'img'),  # links_tags
         ('assets/python.png', 'img'),
         ('favicon.ico', 'link'),
         ('assets/application.css', 'link'),
         ('https://ru.hexlet.io/professions', 'link'),
         ('https://en.hexlet.io/professions', 'link'),
         ('assets/application.js', 'script'),
         ('https://js.stripe.com/v3/', 'script')],
        [('assets/frontend.png', 'img'),  # output
         ('assets/python.png', 'img'),
         ('favicon.ico', 'link'),
         ('assets/application.css', 'link'),
         ('https://ru.hexlet.io/professions', 'link'),
         ('assets/application.js', 'script')]
    ),
])
def test_filter_links_in_domain(url, links_tags, output):
    assert output == filter_links_in_domain(links_tags=links_tags, url=url)


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
    assert expected == get_abs_link(page_url=page_url, local_link=link)


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

    soup = BeautifulSoup(data, 'html.parser')
    assert output == get_links(tag_meta=tag_meta, url=url, soup=soup)
