"""Module downloading HTML content from specified URL into file."""
from bs4 import BeautifulSoup
from page_loader.path import get_file_name, get_foldername, get_ext
from page_loader.loader import load_html, load_bin
from page_loader.links import get_list_of_links, get_full_link
from page_loader.file import create_dir, read_file, save_soup
from page_loader.editor import edit_soup
from page_loader.logger import logger
from termcolor import colored


ASSET_TAGS = {
    'img': 'src',
    'link': 'href',
    'script': 'src'
}


def download(page_url, local_path):

    page_name = get_file_name(url=page_url, ext='html')
    file_path = str(local_path + '/' + page_name)

    try:
        load_html(url=page_url, local_path=file_path)
    except Exception as err:
        logger.critical(err)
        # sys.exit(1)
        # sys.exit(colored(f'Error! {err}. Script has been stopped.', 'red'))

    content = read_file(file_path)
    soup = BeautifulSoup(content, 'html.parser')

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
        asset_name = get_file_name(url=asset_full_url, ext=get_ext(link))

        # Generate local path to save asset
        asset_path = str(local_path + '/' + folder_name + '/' + asset_name)

        # Download asset and edit soup object
        try:
            load_bin(url=asset_full_url, local_path=asset_path)
            soup = edit_soup(remote_link=link, tag=tag, meta=ASSET_TAGS[tag],
                             local_link=folder_name + '/' + asset_name,
                             soup=soup)
            logger.debug(f'"{link}" successfully saved to "{local_path}"')
            print(colored(f'File {asset_name} had been downloaded', 'green'))
        except:  # noqa
            logger.error(f'"{link}" can not be loaded')

    # Save modified soup
    save_soup(data=soup.prettify(formatter='html5'), local_path=file_path)

    # Return path to output file
    return file_path
