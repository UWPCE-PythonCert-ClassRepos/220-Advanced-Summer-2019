# pylint: disable=C0103
# pylint: disable=W0703

"""
pngdiscover.py
Finds .PNG files recursively in target directory
"""

import argparse
import datetime
import logging
import os
from pprint import pprint
import sys

log_format = "%(asctime)s\t%(message)s"
formatter = logging.Formatter(log_format)

file_handler = logging.FileHandler("png_{}.log".format(datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")))
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.setLevel('INFO')
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

data = {}


def find_files(folder, file_extension='.png'):
    """Finds .PNG files recursively in target directory"""
    for item in os.listdir(folder):
        item = "/".join([folder, item])
        if os.path.isdir(item):
            print(item)
            data[item] = []
            find_files(item, file_extension)
            if not data[item]:
                del data[item]
        elif item[-1*len(file_extension):] == file_extension:
            basename = os.path.basename(item)
            dirname = "/" + os.path.dirname(item).strip("/")
            try:
                data[dirname].append(basename)
            except KeyError:
                logger.warning("%s not found in data", dirname)
                data[dirname] = []
                data[dirname].append(basename)


def parse_cmd_arguments():
    """Processes arguments passed to script via the command line"""
    parser = argparse.ArgumentParser(description='Find .PNGs in directory.')
    parser.add_argument('-d', '--search_dir', help='Path containing .PNG files.', required=True)
    logger.debug("Arguments passed to script: %s", parser.parse_args())
    return parser.parse_args()


if __name__ == '__main__':
    cmd_args = parse_cmd_arguments()
    find_files(cmd_args.search_dir)
    pprint(data)
