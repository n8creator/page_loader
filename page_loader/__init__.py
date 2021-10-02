from bs4 import BeautifulSoup
from page_loader.path import split_path_and_ext, get_full_path, get_local_name
from page_loader.loader import load_data
from page_loader.links import get_links, get_absolute_link
from page_loader.file import create_dir, read_file, save_file
from page_loader.editor import edit_soup
from operator import itemgetter
from progress.bar import IncrementalBar
from page_loader.logger import logger

ASSET_TAGS = {"img": "src", "link": "href", "script": "src"}


def download(url, path):
    """Download HTML page and page assets (img, css files) from given 'url'."""

    # Generate output 'page_name' and 'file_path' and load page
    page_name = get_local_name(url=url, mode='file', ext='html')
    file_path = get_full_path(path, page_name)
    load_data(url=url, local_path=file_path)
    print(f'Index page \'{url}\' was downloaded!')

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

        # Initiate progress bar
        progress_bar = IncrementalBar('Loading resourses:', max=len(links))

        for link, tag in links:
            # Generate 'absolute_url' to load and 'file_name' for item
            absolute_url = get_absolute_link(page_url=url, local_link=link)
            ext = itemgetter('ext')(split_path_and_ext(link))
            file_name = get_local_name(url=absolute_url, mode='file', ext=ext)

            # Generate local path & local link for item
            local_path = get_full_path(path, folder_name, file_name)
            local_link = get_full_path(folder_name, file_name)

            # Download item and edit soup object only if item can be downloaded
            try:
                load_data(url=absolute_url, local_path=local_path)
            except Exception:
                logger.error(f'Asset \'{link}\' was not downloaded.')
            else:
                soup = edit_soup(url=link, tag=tag, meta=ASSET_TAGS[tag],
                                 local_link=local_link, soup=soup)

            # Start progress bar
            progress_bar.next()

    # Finish progess_bar
    progress_bar.finish()

    # Save modified soup
    save_file(data=soup.prettify(), local_path=file_path, mode='w')

    # Return output file local path
    return file_path
