"""
a png discovery program in Python, using recursion,
that works from a parent directory called images
provided on the command line. The program will take
the parent directory as input. As output, it will
return a list of lists structured like this:
[“full/path/to/files”, [“file1.png”, “file2.png”,…],
“another/path”,[], etc]
"""
import argparse
import os
from pprint import pprint


global list_output
list_output = []


def parse_cmd_arguments():
    try:
        parser = argparse.ArgumentParser(description='Find Files.')
        parser.add_argument('-d', '--directory',
                            help='Starting directory default "..//data"',
                            required=False,
                            default="..//data")
        parser.add_argument('-e', '--extention',
                            help='Extention type default ".png"',
                            required=False,
                            default=".png")
        return parser.parse_args()
    except Exception as exception:
        print(f"Invalid Arguments. {exception}")


def find_files(folder, file_extension):
    match_extention = []
    for item in os.listdir(folder):
        if item[-1 * len(file_extension):] == file_extension:
            match_extention.append(item)
        else:
            sub_folder = "/".join([folder, item])
            find_files(sub_folder, file_extension)
    if match_extention:
        list_output.append(folder)
        list_output.append(match_extention)
    return list_output


if __name__ == "__main__":
    args = parse_cmd_arguments()
    pprint(find_files(args.directory, args.extention))
