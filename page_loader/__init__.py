"""Module downloading HTML content from specified URL into file."""
from bs4 import BeautifulSoup
from page_loader.path import get_filename, get_foldername, guess_ext
from page_loader.loader import load_content, load_single_asset
from page_loader.links import get_list_of_links, get_full_link
from page_loader.file import create_dir

ASSET_TAGS = {
    'img': 'src',
    'link': 'href',
    'script': 'src'
}


def download(page_url, local_path):
    """Download data from specified URL & save it into file.

    Args:
        url ([str]): url, like "https://python.org/3/library/exceptions.html"
        local_path ([str]): local path, like: "/var/tmp"
    """
    # Get HTML data from URL & create BeautufulSoup object
    content = load_content(page_url)
    soup = BeautifulSoup(content, 'lxml')

    # Generate main_page_name
    page_name = get_filename(url=page_url, ext=guess_ext(page_url))

    # Save main page as file
    load_single_asset(url=page_url,
                      local_path=local_path + '/' + page_name)

    # Get list of links
    links = get_list_of_links(tag_meta=ASSET_TAGS, url=page_url, soup=soup)

    # If links[] is not empty -> create dir to save asset files
    if links:
        folder_name = get_foldername(url=page_url)
        create_dir(local_path=local_path + '/' + folder_name)

    # Load all assets from links[] list
    for link, tag in links:
        asset_full_url = get_full_link(page_url=page_url, link=link)
        asset_name = get_filename(url=asset_full_url, ext=guess_ext(link))
        load_single_asset(url=asset_full_url,
                          local_path=(local_path + '/'
                                      + folder_name + '/'
                                      + asset_name))
        output = local_path + '/' + folder_name + '/' + asset_name
        print(f'Asset {link} loaded at {output}')
