"""
pngdiscovery.py
assignment part 3

built on what was done in class but looking at that code now I had trouble following what we did.
Added the last few lines, along with 'list_of_list' object to provide what the assignment required.
sorry if its hard to follow.
"""

import os
from pprint import pprint

data = {}
list_of_list = []


def find_files(folder, file_extension):
    # list_of_list = []
    list_of_list.append(folder)
    for item in os.listdir(folder):
        item = "/".join([folder, item])
        # item = "/" + str(item)
        if os.path.isdir(item):
            data[item] = []

            # recursion
            find_files(item, file_extension)

            if len(data[item]) == 0:
                del data[item]

        else:
            if item[-1*len(file_extension):] == file_extension:
                basename = os.path.basename(item)
                dirname = os.path.dirname(item).strip("/")
                data[dirname].append(basename)

            # print([list_of_list[-1], [item]])
            # print(data)
            # print(item)

                list_item = item.split('/')
                last_item = list_item.pop()
                print(['/'.join(list_item), [last_item]])

                # print(last_item)


find_files(".", ".png")

