"Page Loader Executable Script"
from page_loader.cli import get_args
from page_loader import download


def main():
    """Main page_loader script."""
    # Parse Arguments Entered By The User
    args = get_args()

    # Print Result of Download function
    print(download(page_url=args.URL,
                   local_path=args.output))


if __name__ == "__main__":
    main()
