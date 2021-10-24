import pytest
from page_loader.url import url_to_string, get_filename, get_foldername, \
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


# Test get_filename() function
@pytest.mark.parametrize('url, output', [
    ('https://site.io/blog/page.php', 'site-io-blog-page.php'),
    ('/temp/skin/banner_desktop.js?2689', 'temp-skin-banner-desktop.js'),
    ('https://site.io/pcode/page/', 'site-io-pcode-page.html'),
    ('https://ru.site.io/js/publishertag.js', 'ru-site-io-js-publishertag.js')
])
def test_get_filename(url, output):
    assert output == get_filename(url=url)


# Test get_foldername()
@pytest.mark.parametrize('url, output', [
    ('https://site.io/blog/page.php',
     'site-io-blog-page_files'),
    ('/templates/skin/banner_desktop.js?2689',
     'templates-skin-banner-desktop_files'),
    ('https://site.io/pcode/page/',
     'site-io-pcode-page_files'),
    ('https://ru.site.io/js/publishertag.js',
     'ru-site-io-js-publishertag_files')
])
def test_get_foldername(url, output):
    assert output == get_foldername(url)
