import pytest
from page_loader.path import remove_url_ext, url_to_string, get_filename,\
    get_foldername, get_ext


# Test remove_url_ext() function
@pytest.mark.parametrize('url, output', [
    ('https://yastatic.net/pcode/adfox/header-bidding.js',
     'https://yastatic.net/pcode/adfox/header-bidding'),
    ('/templates/skin/smart-lab-x3/js/adfox_hb_desktop.js?2689',
     '/templates/skin/smart-lab-x3/js/adfox_hb_desktop'),
    ('https://yastatic.net/pcode/adfox/',
     'https://yastatic.net/pcode/adfox/'),
    ('https://smart-lab.ru/blog/669977.php',
     'https://smart-lab.ru/blog/669977')
])
def test_remove_extension(url, output):
    assert output == remove_url_ext(url)


# Test get_ext() function
@pytest.mark.parametrize('url, output', [
    ('/templates/cache/69e1154aa47f1.css?2708', 'css'),
    ('/templates/cache/69e1154aa47f1.css', 'css'),
    ('/templates/adfox_hb_desktop.js?2708', 'js'),
    ('https://ya.ru/templates/adfox_hb_desktop.js?2708', 'js'),
    ('https://www.recaptcha.net/recaptcha/api.js?render=6LenGbgZ', 'js'),
    ('http://www.youtube.com/watch?v=gwS1tGLB0vc', 'html'),
    ('www.example.com/test.php?id=12', 'php'),
    ('www.example.com/test', 'html'),
    ('www.example.com/test/', 'html'),
    ('https://site.ru', 'html')
])
def test_get_ext(url, output):
    assert output == get_ext(url)


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
    assert output == get_filename(url=link, ext=ext)


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
