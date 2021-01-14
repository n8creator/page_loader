import pytest
from page_loader.path import remove_url_ext, url_to_string, get_filename,\
    get_foldername


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


# Test url_to_string() function
@pytest.mark.parametrize('url, output', [
    ('https://smart-lab.ru/blog/669977.php',
     'smart-lab-ru-blog-669977'),
    ('/templates/skin/smart-lab-x3/js/adfox_hb_desktop.js?2689',
     'templates-skin-smart-lab-x3-js-adfox-hb-desktop'),
    ('https://yastatic.net/pcode/adfox/',
     'yastatic-net-pcode-adfox'),
    ('https://static.criteo.net/js/ld/publishertag.js',
     'static-criteo-net-js-ld-publishertag')
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




# @pytest.mark.parametrize('url, local_path, output', [
#     ('http://yandex.ru/',
#      '/var/temp',
#      '/var/temp/yandex-ru.html'),
#     ('https://www.notion.so/14-2-b22045cb63d24a28974dd5d094fddee8',
#      '/var/temp/',
#      '/var/temp/www-notion-so-14-2-b22045cb63d24a28974dd5d094fddee8.html'),
#     ('https://requests-mock.readthedocs.io/_/downloads/en/latest/pdf/',
#      '/var/temp',
#      '/var/temp/requests-mock-readthedocs-io-downloads-en-latest-pdf.html'),
#     ('https://ru.hexlet.io/blog/posts/developers-business-value',
#      '/var/temp',
#      '/var/temp/ru-hexlet-io-blog-posts-developers-business-value.html'),
#     ('https://ru.hexlet.io/projects/50/members/11333/mentor',
#      '/var/temp/',
#      '/var/temp/ru-hexlet-io-projects-50-members-11333-mentor.html'),
#     ])
# def test_filepaths(url, local_path, output):
#     assert output == get_localpath(url, local_path)
