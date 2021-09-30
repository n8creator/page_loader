from bs4 import BeautifulSoup
from page_loader.path import split_path_and_ext, get_full_path, get_local_name
from page_loader.loader import load_data
from page_loader.links import get_links, get_absolute_link
from page_loader.file import create_dir, read_file, save_file
from page_loader.editor import edit_soup
from page_loader.logger import logger
from operator import itemgetter


ASSET_TAGS = {"img": "src", "link": "href", "script": "src"}


def download(url, path):

    page_name = get_local_name(url=url, mode='file', ext='html')
    file_path = get_full_path(path, page_name)

    try:
        load_data(url=url, local_path=file_path)
    except Exception as err:
        logger.critical(err)
        # sys.exit(1)
        # sys.exit(colored(f'Error! {err}. Script has been stopped.', 'red'))

    # Parse downloaded page into 'soup' variable
    content = read_file(file_path)
    soup = BeautifulSoup(content, "html.parser")

    # Get list of links
    links = get_links(tag_meta=ASSET_TAGS, url=url, soup=soup)

    # If links[] is not empty -> create dir to save asset files
    if links:
        # Generate folder_name and create directory
        folder_name = get_local_name(url=url, mode='folder')
        create_dir(local_path=get_full_path(path, folder_name))

        for link, tag in links:
            # Generate 'absolute_url' to load and 'file_name' for item
            absolute_url = get_absolute_link(page_url=url, local_link=link)
            ext = itemgetter('ext')(split_path_and_ext(link))
            file_name = get_local_name(url=absolute_url, mode='file', ext=ext)

            # Generate local path & local link for item
            local_path = get_full_path(path, folder_name, file_name)
            local_link = get_full_path(folder_name, file_name)

            # Download item and edit soup object
            try:
                load_data(url=absolute_url, local_path=local_path)
                soup = edit_soup(url=link, tag=tag, meta=ASSET_TAGS[tag],
                                 local_link=local_link, soup=soup)
                logger.debug(f'"{link}" successfully saved to "{path}"')
            except:  # noqa
                logger.error(f'"{link}" can not be loaded')

    # Save modified soup
    save_file(data=soup.prettify(), local_path=file_path, mode='w')

    # Return path to output file
    return file_path
