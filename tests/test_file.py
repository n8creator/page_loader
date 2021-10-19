from page_loader.file import get_full_path


# Test get_full_path() function
def get_get_full_path():
    assert get_full_path('site', 'blog', 'page.html') == 'site/blog/page.html'
