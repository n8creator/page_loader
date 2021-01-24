"""Module downloading HTML content from specified URL into file."""
from bs4 import BeautifulSoup
from page_loader.path import get_filename, get_foldername, get_ext
from page_loader.loader import load_single_asset
from page_loader.links import get_list_of_links, get_full_link
from page_loader.file import create_dir, read_file, save_soup
from page_loader.editor import edit_soup
from page_loader.logger import logger
import sys

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

    # Generate main_page_name & saving path
    page_name = get_filename(url=page_url, ext=get_ext(page_url))  # noqa TODO тут лучше сделать ".html"
    save_path = str(local_path + '/' + page_name)

    # Load and save main page as file
    try:
        load_single_asset(url=page_url, local_path=save_path)
    # Raise exception if main page cannot be downloaded
    except Exception as err:
        msg = f'{err}. Script has been stopped.'
        logger.critical(msg)
        sys.exit(msg)

    # Get HTML data & create BeautufulSoup object
    content = read_file(save_path)
    soup = BeautifulSoup(content, 'lxml')

    # Get list of links
    links = get_list_of_links(tag_meta=ASSET_TAGS, url=page_url, soup=soup)

    # If links[] is not empty -> create dir to save asset files
    if links:
        folder_name = get_foldername(url=page_url)
        create_dir(local_path=local_path + '/' + folder_name)

    # Load all assets from links[] list
    for link, tag in links:
        # Generate full asset link to make request & name to save file
        asset_full_url = get_full_link(page_url=page_url, link=link)
        asset_name = get_filename(url=asset_full_url, ext=get_ext(link))

        # Generate local path to save asset
        asset_path = str(local_path + '/' + folder_name + '/' + asset_name)

        # Download asset and edit soup object
        try:
            load_single_asset(url=asset_full_url, local_path=asset_path)
            soup = edit_soup(remote_link=link, tag=tag, meta=ASSET_TAGS[tag],
                             local_link=folder_name + '/' + asset_name,
                             soup=soup)
            logger.debug(f'"{link}" successfully saved to "{local_path}"')
        except:  # noqa
            logger.error(f'"{link}" can not be loaded')

    # Save modified soup
    save_soup(data=soup.prettify(formatter='html5'), local_path=save_path)

    # Return path to output file
    return save_path
