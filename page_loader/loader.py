"""Module makes request to some URL and returns HTML code."""
import requests
from page_loader.file import save_file
from page_loader.logger import logger


def make_request(url: str) -> bin:
    """Make request, return binary data or raise exception.

    Args:
        url ([str]): URL as a string

    Returns:
        [bin]: binary code containing server response
    """

    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        return r.content
    except requests.HTTPError as err:
        msg = (f'Can\'t connect to "{url}". HTTPError: {r.status_code} '
               f'response')
        logger.error(msg)
        raise Exception(msg) from err
    except requests.ConnectionError as err:
        msg = (f'Can\'t reach "{url}" due to ConnectionError (DNS failure, '
               f'refused connection, etc)')
        logger.error(msg)
        raise Exception(msg) from err
    except requests.Timeout as err:
        msg = (f'Can\'t connect to "{url}". Сonnection timeout exceeded')
        logger.error(msg)
        raise Exception(msg) from err
    except requests.RequestException as err:
        msg = f'Can\'t connect to "{url}". Error: {err}'
        logger.error(msg)
        raise Exception(msg) from err


def load_single_asset(url, local_path):
    # Make request and get content or exception
    try:
        content = make_request(url)
    except Exception as err:
        raise err
    # Save page if request was successfull
    else:
        try:
            save_file(data=content, local_path=local_path)
        except Exception as err:
            print('An error occurred while file saving:' + str(err))
            logger.warning('An error occurred while file saving:' + {str(err)})


if __name__ == "__main__":
    print(load_single_asset('https://ecworld1.fund/', '/var/tmp/ec.html'))
