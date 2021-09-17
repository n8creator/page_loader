"Parse arguments defined by user."
import argparse
import os
import sys
import textwrap


def get_args(argv=None):
    """Parse user-defined arguments."""

    # Define arguments and 'epilog_text'
    epilog_text = '''
        Supported combination of arguments and flags:
         page-loader
            ├── URL               - download page into current folder
            └── URL -o            - download page into 'output' folder
            '''
    parser = argparse.ArgumentParser(
        description='Page Loader CLI quick help.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(epilog_text))

    parser.add_argument('URL', help='specify URL which should be downloaded')
    parser.add_argument('-o', '--output', default=os.getcwd(),
                        help='specify local path to save output or skip \
                            to save in current directory')

    # Print '--help' if no arguments were passed
    if len(sys.argv) == 1:
        parser.print_help()
        parser.exit()

    # Parse & return arguments
    args = parser.parse_args(argv)
    return args
