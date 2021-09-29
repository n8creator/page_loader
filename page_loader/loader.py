import requests
from page_loader.file import save_file
from page_loader.logger import logger


def make_request(url: str) -> bin:
    """Make request and return bytecode (or throw exception)."""
    if not url:
        requests.exceptions.InvalidURL
    r = requests.get(url, stream=True, timeout=5)
    r.raise_for_status()
    return r.content


def load_data(url, local_path):
    """Load data from url and save it into local file."""
    try:
        content = make_request(url)
    except Exception as err:
        raise err
    else:
        try:  # Save data if request was successfull
            save_file(data=content, local_path=local_path)
        except Exception as err:
            print('An error occurred while file saving:' + str(err))
            logger.warning('An error occurred while file saving:' + {str(err)})
