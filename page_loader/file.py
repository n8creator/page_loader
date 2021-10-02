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


def read_file(file_path, mode='r', encoding=None):
    """Read & return data from some file at given 'file_path'."""
    try:
        with open(file_path, mode, encoding=encoding) as file:
            data = file.read()
        return data
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
