"Page Loader executable script"
from page_loader.cli import get_args
from page_loader import download
from page_loader.logger import logger
import sys


def main():
    """Main page_loader script."""
    try:
        logger.info('Page-loader script started!')
        url, path = get_args().URL, get_args().output
        file_path = download(url=url, path=path)
    except Exception as err:
        print(err)
        logger.info('Page-loader script finished.')
        sys.exit(1)
    else:
        logger.info('Page-loader script finished.')
        print(f'Output page had been saved to \'{file_path}\'')
        sys.exit(0)


if __name__ == "__main__":
    main()
