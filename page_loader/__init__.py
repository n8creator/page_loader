"""Module downloading HTML content from specified URL into file."""
from bs4 import BeautifulSoup
from page_loader.path import get_file_name, get_foldername, split_path_and_ext
from page_loader.loader import load_data
from page_loader.links import get_links, get_absolute_link
from page_loader.file import create_dir, read_file, save_file
from page_loader.editor import edit_soup
from page_loader.logger import logger
import sys
import os


ASSET_TAGS = {"img": "src", "link": "href", "script": "src"}


def download(url, local_path):

    page_name = get_file_name(url=url, ext="html")  # REFACTOR
    file_path = os.path.join(local_path, page_name)

    try:
        load_data(url=url, local_path=file_path)
    except Exception as err:
        logger.critical(err)
        sys.exit(1)
        # sys.exit(colored(f'Error! {err}. Script has been stopped.', 'red'))

    content = read_file(file_path)
    soup = BeautifulSoup(content, "html.parser")

    # Get list of links
    links = get_links(tag_meta=ASSET_TAGS, url=url, soup=soup)

    # If links[] is not empty -> create dir to save asset files
    if links:
        folder_name = get_foldername(url=url)   # REFACTOR
        create_dir(local_path=os.path.join(local_path, folder_name))

        for link, tag in links:
            asset_url = get_absolute_link(page_url=url, local_link=link)
            asset_name = get_file_name(url=asset_url,
                                       ext=split_path_and_ext(link)['ext'])    # REFACTOR

            # Generate local path to save asset
            asset_local_path = os.path.join(local_path, folder_name, asset_name)

            # Download asset and edit soup object
            try:
                load_data(url=asset_url, local_path=asset_local_path)
                soup = edit_soup(
                    hyperlink=link,
                    tag=tag,
                    meta=ASSET_TAGS[tag],
                    local_link=os.path.join(
                        folder_name, asset_name),  # REFACTOR
                    soup=soup,
                )
                logger.debug(f'"{link}" successfully saved to "{local_path}"')
            except:  # noqa
                logger.error(f'"{link}" can not be loaded')

    # Save modified soup
    save_file(data=soup.prettify(), local_path=file_path, mode='w')

    # Return path to output file
    return file_path
