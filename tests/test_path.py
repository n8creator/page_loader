import pytest
from page_loader.path import url_to_string, get_file_name, get_foldername,\
    split_path_and_ext


@pytest.mark.parametrize('url, output', [
    ('https://site.com/adfox/header-bidding.js',
     {'path': 'https://site.com/adfox/header-bidding', 'ext': 'js'}),
    ('/templates/js/adfox_desktop.js?2689',
     {'path': '/templates/js/adfox_desktop', 'ext': 'js'}),
    ('https://site.com/adfox/',
     {'path': 'https://site.com/adfox/', 'ext': 'html'}),
    ('https://site.com/blog/669977.php',
     {'path': 'https://site.com/blog/669977', 'ext': 'php'})
])
def test_split_path_and_ext(url, output):
    assert output == split_path_and_ext(path=url)


# Test url_to_string() function
@pytest.mark.parametrize('url, output', [
    ('https://smart-lab.ru/blog/669977.php',
     'smart-lab-ru-blog-669977'),
    ('/templates/skin/smart-lab-x3/js/adfox_hb_desktop.js?2689',
     'templates-skin-smart-lab-x3-js-adfox-hb-desktop'),
    ('https://yastatic.net/pcode/adfox/',
     'yastatic-net-pcode-adfox'),
    ('https://static.criteo.net/js/ld/publishertag.js',
     'static-criteo-net-js-ld-publishertag'),
    ('https://abc-lab.ru', 'abc-lab-ru'),
    ('https://abc-lab.ru/', 'abc-lab-ru'),
])
def test_url_to_string(url, output):
    assert output == url_to_string(url)


# Test get_filename() function
@pytest.mark.parametrize('link, ext, output', [
    ('https://smart-lab.ru/blog/669977.php',
     'php',
     'smart-lab-ru-blog-669977.php'),
    ('/templates/skin/smart-lab-x3/js/adfox_hb_desktop.js?2689',
     'js',
     'templates-skin-smart-lab-x3-js-adfox-hb-desktop.js'),
    ('https://yastatic.net/pcode/adfox/',
     'html',
     'yastatic-net-pcode-adfox.html'),
    ('https://static.criteo.net/js/ld/publishertag.js',
     'js',
     'static-criteo-net-js-ld-publishertag.js')
])
def test_get_filename(link, ext, output):
    assert output == get_file_name(url=link, ext=ext)


# Test get_foldername() function
@pytest.mark.parametrize('link, output', [
    ('https://smart-lab.ru/blog/669977.php',
     'smart-lab-ru-blog-669977_files'),
    ('/templates/skin/smart-lab-x3/js/adfox_hb_desktop.js?2689',
     'templates-skin-smart-lab-x3-js-adfox-hb-desktop_files'),
    ('https://yastatic.net/pcode/adfox/',
     'yastatic-net-pcode-adfox_files'),
    ('https://static.criteo.net/js/ld/publishertag.js',
     'static-criteo-net-js-ld-publishertag_files')
])
def test_get_foldername(link, output):
    assert output == get_foldername(url=link)
