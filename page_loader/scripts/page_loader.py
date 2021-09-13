"Page Loader Executable Script"
from page_loader.cli import get_args
from page_loader import download
from page_loader.logger import logger
import sys


def main():
    """Main page_loader script."""
    # Parse Arguments Entered By The User
    try:
        args = get_args()
        file_path = download(page_url=args.URL, local_path=args.output)
    except Exception as err:
        logger.error(err)
        sys.exit(1)
    else:
        logger.info('Downloading finished')
        print(f'Page had been saved to {file_path}')
        sys.exit(0)


if __name__ == "__main__":
    main()
