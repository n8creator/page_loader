"""Module saving some variable data into file."""
import os
from page_loader.logger import logger


def save_html(data, local_path):
    try:
        with open(local_path, 'wb') as file:
            file.write(data)
    except Exception as err:
        logger.warning('An error occurred while saving the file:' + str(err))
        print('An error occurred while saving the file:' + str(err))


def save_bin(data, local_path):
    with open(local_path, 'wb') as file:
        file.write(data)


def read_file(file_path, mode='r', encoding=None):
    try:
        with open(file_path, mode, encoding=encoding) as file:
            data = file.read()
        return data
    except Exception as err:
        print('An error occurred while reading the file:' + str(err))


def create_dir(local_path: str):
    try:
        os.mkdir(local_path)
    except OSError as e:
        logger.warning('Creation of the _files directory failed:' + str(e))


def save_soup(data, local_path):
    """Save string data into file with specified path.

    Args:
        data ([str]): some data
        local_path ([str]): local path
    """
    try:
        with open(local_path, 'w') as file:
            file.write(data)
    except Exception as err:
        logger.warning('An error occurred while saving the file:' + str(err))
        print('An error occurred while saving the file:' + str(err))
