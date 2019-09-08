import os
data = {}


def find_files(folder, file_extension, dirs=[], result=[]):
    dirs.append(folder)
    print(f"Checking folder: {folder}")
    current_dir = "/".join(dirs)
    print(f"current_dir: {current_dir}")
    for item in os.listdir(current_dir):
        print(f"Checking directory: {item}")
        if os.path.isdir(current_dir + "/" + item):
            find_files(item, file_extension, dirs, result)

        else:
            if item[-1*len(file_extension):] == file_extension:
                png_path = "/".join(dirs) + "/" + item
                print(f"Found png: {png_path}")
                result.append(png_path)
    dirs.pop()

    return result


result = find_files("../data", ".png")
pprint(result)
