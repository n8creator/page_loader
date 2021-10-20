import requests
from requests.exceptions import ConnectionError, HTTPError
from page_loader.logger import logger


def make_request(url: str) -> bin:
    """Make request and return bytecode (or throw exception)."""
    try:
        r = requests.get(url, stream=True, timeout=5)
        r.raise_for_status()
        return r.content
    except ConnectionError as err:
        logger.error(err)
        raise ConnectionError(f'ConnectionError occured: \'{err}\'')
    except HTTPError as err:
        logger.error(err)
        raise HTTPError(f'HTTPError occured: \'{err}\'')
