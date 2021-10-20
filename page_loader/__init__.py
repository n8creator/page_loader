import os
from bs4 import BeautifulSoup
from operator import itemgetter
from page_loader.logger import logger
from progress.bar import IncrementalBar
from page_loader.editor import edit_soup
from page_loader.loader import make_request
from page_loader.links import get_links, get_abs_link
from page_loader.file import create_dir, save_file, get_full_path
from page_loader.url import split_path_and_ext, get_filename, get_foldername


ASSET_TAGS = {"img": "src", "link": "href", "script": "src"}
DEFAULT_PATH = os.getcwd()


def download(url, path=DEFAULT_PATH):
    """Download HTML page and page assets (img, css files) from given 'url'."""
    # Generate output 'page_name' and 'file_path' and load page
    page_name = get_filename(url=url, ext='html')
    file_path = get_full_path(path, page_name)

    # Make request, edit Soup object and save data into output file
    content = make_request(url)
    soup = BeautifulSoup(content, "html.parser")

    # Get list of links
    links = get_links(tag_meta=ASSET_TAGS, url=url, soup=soup)

    # Edit Soup object and replace links to loclal files
    if links:
        # Generate folder_name and create directory
        folder_name = get_foldername(url=url)
        create_dir(local_path=get_full_path(path, folder_name))

        to_download = []  # Initiate download queue

        # Iterate links and edit Soup object
        for link, tag in links:
            # Generate 'absolute_url' to load and 'file_name' for item

            # ################# КОММЕНТАРИЙ МЕНТОРУ START #################

            # Я осознанно оставил вызов функции get_abs_link(), хотя в
            # в замечаниях Вы предложили возвращать абсолютные пути
            # непосредственно при вызове функции get_links() (28 строка выше).
            # Проблема в том, что при редактировании HTML-страницы нам нужно
            # менять ФАКТИЧЕСКИЕ URL, которые встречаются на странице -
            # а они могуть быть как абсолютными, так и относительными.

            # Поэтому для редактирования HTML-страницы мы получаем с помощью
            # функции get_links() фактически встречающиеся URL, а для
            # скачивания ресурсов преобразуем их в абсолютные...

            # ################# КОММЕНТАРИЙ МЕНТОРУ END #################

            absolute_url = get_abs_link(page_url=url, local_link=link)
            ext = itemgetter('ext')(split_path_and_ext(link))
            file_name = get_filename(url=absolute_url, ext=ext)

            # Generate local path & local link for item
            local_path = get_full_path(path, folder_name, file_name)
            local_link = get_full_path(folder_name, file_name)
            soup = edit_soup(url=link, tag=tag, meta=ASSET_TAGS[tag],
                             local_link=local_link, soup=soup)

            # Add asset's absolute url and local_path into queue
            to_download.append((absolute_url, local_path))

    # Save modified soup
    save_file(data=soup.prettify(), local_path=file_path, mode='w')

    # Initiate progress bar and download assets
    progress_bar = IncrementalBar('Loading resourses:', max=len(to_download))
    for absolute_url, local_path in to_download:
        try:
            content = make_request(absolute_url)
            save_file(data=content, local_path=local_path)
        except Exception:
            logger.error(f'Asset \'{link}\' was not downloaded.')
        progress_bar.next()  # Iterate progress bar

    # Finish progess_bar & return output's file path
    progress_bar.finish()
    return file_path
