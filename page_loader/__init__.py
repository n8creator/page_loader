"""Module downloading HTML content from specified URL into file."""
from page_loader.url import get_filepath
from page_loader.loader import get_html
from page_loader.saver import save_file


def download(url, local_path):
    """Download data from specified URL & save it into file.

    Args:
        url ([str]): url, like "https://python.org/3/library/exceptions.html"
        local_path ([str]): local path, like: "/var/tmp"
    """
    # Generate file_path to save data
    file_path = get_filepath(url=url, local_path=local_path)

    # # Get HTML data from URL
    html = get_html(url)

    # Save parsed data into file
    try:
        save_file(data=html, local_path=file_path)
        return(file_path)
    except Exception as err:
        print('An error occurred:' + str(err))
