import os
from pprint import pprint

data = {}


def find_files(folder, file_extension):
    for item in os.listdir(folder):
        item = "/".join([folder, item])
        if os.path.isdir(item):
            data[item] = []
            find_files(item, file_extension)  # RECURSION TIME
            if len(data[item]) == 0:
                del data[item]
        else:
            if item[-1*len(file_extension):] == file_extension:
                # print(item)
                basename = os.path.basename(item)
                dirname = os.path.dirname(item).strip("/")
                data[dirname].append(basename) #key error here, dunno why?

find_files(".", ".png")

pprint(data)
