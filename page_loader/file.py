"""Module saving some variable data into file."""
import os
from page_loader.logger import logger


def save_file(data, local_path, mode='wb'):
    """Save data into file."""
    try:
        with open(local_path, mode) as file:
            file.write(data)
    except Exception as err:
        logger.warning('An error occurred while saving the file:' + str(err))
        print('An error occurred while saving the file:' + str(err))


def read_file(file_path, mode='r', encoding=None):
    """Read & return data from some file at given 'file_path'."""
    try:
        with open(file_path, mode, encoding=encoding) as file:
            data = file.read()
        return data
    except Exception as err:
        print('An error occurred while reading the file:' + str(err))


def create_dir(local_path: str):
    """Create new directory at 'local_path' or throw exception."""
    try:
        os.mkdir(local_path)
    except OSError as e:
        logger.warning('Creation of the _files directory failed:' + str(e))
