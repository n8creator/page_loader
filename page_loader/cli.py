"Module Parsing Arguments Entered By The User."
import argparse
import os


def get_args(argv=None):
    """Function Returning Arguments Entered By The User.

    Returns:
        [tuple]: args entered by the user
    """
    parser = argparse.ArgumentParser(description='Page Loader')
    parser.add_argument('-o', '--output',
                        default=os.getcwd(),
                        help='specify local path on your system to save output\
                            or skip it to save in current directory')
    parser.add_argument('URL', help='specify URL which should be downloaded')
    args = parser.parse_args(argv)
    print(args)
    return args
