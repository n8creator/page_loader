"Module Parsing Arguments Entered By The User."
import argparse
import os


def get_args():
    """Function Returning Arguments Entered By The User.

    Returns:
        [tuple]: args entered by the user
    """
    parser = argparse.ArgumentParser(description='Page Loader')
    parser.add_argument('-o', '--output',
                        default=os.getcwd(),
                        help='specify local path on your system to save output\
                              or leave it blank to save in current directory')
    parser.add_argument('URL')
    args = parser.parse_args()
    return args
