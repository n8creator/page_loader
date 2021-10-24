import os
from bs4 import BeautifulSoup
from operator import itemgetter
from page_loader.logger import logger
from progress.bar import IncrementalBar
from page_loader.editor import edit_soup
from page_loader.loader import make_request
from page_loader.links import get_links, get_abs_link
from page_loader.url import get_filename, get_foldername
from page_loader.file import create_dir, save_file, get_full_path


ASSET_TAGS = {"img": "src", "link": "href", "script": "src"}
DEFAULT_PATH = os.getcwd()


def download(url, path=DEFAULT_PATH):
    """Download HTML page and page assets (img, css files) from given 'url'."""
    # Generate output 'page_name' and 'file_path' and load page
    page_name = get_filename(url=url)
    file_path = get_full_path(path, page_name)

    # Make request, edit Soup object and save data into output file
    content = make_request(url)
    soup = BeautifulSoup(content, "html.parser")

    # Get list of links
    links = get_links(tag_meta=ASSET_TAGS, url=url, soup=soup)

    # Edit Soup object and replace links to loclal files
    if links:
        # Generate folder name and path
        folder_name = get_foldername(url=url)
        folder_path = get_full_path(path, folder_name)

        # Create output directory (id doesn't exist)
        if not os.path.isdir(folder_path):
            create_dir(local_path=folder_path)

        to_download = []  # Initiate download queue

        # Iterate links and edit soup object
        for link_dict in links:
            # Destructure link's dict
            fact_link, abs_link, tag = itemgetter(
                'fact_link', 'abs_link', 'tag')(link_dict)

            # Generate file_name, local path & local link for item
            file_name = get_filename(url=abs_link)
            local_path = get_full_path(path, folder_name, file_name)
            local_link = get_full_path(folder_name, file_name)

            # Edit soup object
            soup = edit_soup(url=fact_link, tag=tag, meta=ASSET_TAGS[tag],
                             local_link=local_link, soup=soup)

            # Add asset's absolute url and local_path into queue
            to_download.append((abs_link, local_path))

    # Save modified soup
    save_file(data=soup.prettify(), local_path=file_path, mode='w')

    # Initiate progress bar and download assets
    progress_bar = IncrementalBar('Loading resourses:', max=len(to_download))
    for abs_link, local_path in to_download:
        try:
            content = make_request(abs_link)
            save_file(data=content, local_path=local_path)
        except Exception:
            logger.error(f'Asset \'{abs_link}\' was not downloaded.')
        progress_bar.next()  # Iterate progress bar

    # Finish progess_bar & return output's file path
    progress_bar.finish()
    return file_path
