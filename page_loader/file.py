import os
from page_loader.logger import logger


def save_file(data, local_path, mode='wb'):
    """Save data into file."""
    try:
        with open(local_path, mode) as file:
            file.write(data)
        logger.debug(f'Data had been saved into \'{local_path}\' file')
    except OSError as err:
        logger.error(err)
        raise OSError(err)


def create_dir(local_path: str):
    """Create new directory at 'local_path' or throw exception."""
    try:
        os.mkdir(local_path)
        logger.debug(f'New folder was created at \'{local_path}\'')
    except OSError as err:
        logger.error(err)
        raise OSError(err)


def get_full_path(*args):
    """Generate local path from the list or arguments."""
    return os.path.join(*args)
