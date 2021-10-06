import pytest
from page_loader.url import url_to_string, get_local_name, get_full_path, \
    split_path_and_ext


# Test split_path_and_ext() function
@pytest.mark.parametrize('url, output', [
    ('https://site.io/adfox/header-bidding.js',
     {'path': 'https://site.io/adfox/header-bidding', 'ext': 'js'}),
    ('/templates/js/desktop.js?2689',
     {'path': '/templates/js/desktop', 'ext': 'js'}),
    ('https://site.io/page/',
     {'path': 'https://site.io/page/', 'ext': 'html'}),
    ('https://site.io/blog/page-1.php',
     {'path': 'https://site.io/blog/page-1', 'ext': 'php'})
])
def test_split_path_and_ext(url, output):
    assert output == split_path_and_ext(path=url)


# Test url_to_string() function
@pytest.mark.parametrize('url, output', [
    ('https://site.io/blog/page_1.php', 'site-io-blog-page-1'),
    ('/templates/skin/js/desktop.js?2689', 'templates-skin-js-desktop'),
    ('https://site.io/pcode/page/', 'site-io-pcode-page'),
    ('http://site.io/js/ld/publishertag.js', 'site-io-js-ld-publishertag'),
    ('https://site.io', 'site-io'),
    ('https://site.io/', 'site-io'),
])
def test_url_to_string(url, output):
    assert output == url_to_string(url)


# Test get_full_path() function
def get_get_full_path():
    assert get_full_path('site', 'blog', 'page.html') == 'site/blog/page.html'


# Test get_local_name() function for 'file' mode only
@pytest.mark.parametrize('url, mode, ext, output', [
    ('https://site.io/blog/page.php', 'file', 'php',
     'site-io-blog-page.php'),
    ('/templates/skin/banner_desktop.js?2689', 'file', 'js',
     'templates-skin-banner-desktop.js'),
    ('https://site.io/pcode/page/', 'file', 'html',
     'site-io-pcode-page.html'),
    ('https://ru.site.io/js/publishertag.js', 'file', 'js',
     'ru-site-io-js-publishertag.js')
])
def test_get_local_name_files(url, mode, ext, output):
    assert output == get_local_name(url, mode, ext)


# Test get_local_name() function for 'folder' mode only
@pytest.mark.parametrize('url, mode, output', [
    ('https://site.io/blog/page.php', 'folder',
     'site-io-blog-page_files'),
    ('/templates/skin/banner_desktop.js?2689', 'folder',
     'templates-skin-banner-desktop_files'),
    ('https://site.io/pcode/page/', 'folder',
     'site-io-pcode-page_files'),
    ('https://ru.site.io/js/publishertag.js', 'folder',
     'ru-site-io-js-publishertag_files')
])
def test_get_local_name_folderes(url, mode, output):
    assert output == get_local_name(url, mode)
