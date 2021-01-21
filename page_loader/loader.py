"""Module makes request to some URL and returns HTML code."""
import requests
from page_loader.file import save_file


def load_content(url: str) -> str:
    """Make request & return bytecode or exit depending on the response code.

    Args:
        url ([str]): URL as a string

    Returns:
        [str]: string containing HTML code
    """
    r = requests.get(url)

    if r.ok:  # 200
        return r.content
    else:  # 40x, 30x, 50x
        raise Exception(f'Request returned {r.status_code} response. '
                        f'"{url}" can not be loaded')


def load_single_asset(url, local_path):
    # Make request and get content or exception
    try:
        content = load_content(url)
    except Exception as e:
        raise e
    else:
        # Save page if request was successfull
        try:
            save_file(data=content, local_path=local_path)
        except Exception as err:
            print('An error occurred while file saving:' + str(err))
