#!/usr/bin/python3

import sys
import os
import hashlib

def md5(file_path):
    """ return the md5sum of a file """
    if os.path.isdir(file_path):
        return '1'
    read_file = open(file_path,"rb")
    the_hash = hashlib.md5()
    the_hash.update(read_file.read())
    read_file.close()
    return the_hash.hexdigest()

def directory_listing(dir_name):
    """Return list of all files in directory"""
    dir_file_list = {}
    dir_root = None
    dir_trim = 0
    for path, dirs, files in os.walk(dir_name):
        if dir_root is None:
            dir_root = path
            dir_trim = len(dir_root)
            print("dir",dir_name)
            print("root is",dir_root)
        trimmed_path=path[dir_trim:]
        if trimmed_path.startswith(os.path.sep):
            trimmed_path=trimmed_path[1:] #strip off the leading /
        for each_file in files + dirs:
            file_path=os.path.join(trimmed_path,each_file)
            dir_file_list[file_path]=True
    return (dir_file_list, dir_root)


if len(sys.argv) != 3:
    print("Usage: ", sys.argv[0], "<directory 1> <directory 2>")
    sys.exit()

directory1 = sys.argv[1]
directory2 = sys.argv[2]

print("Comparing ", directory1, directory2)
print()

dir1_file_list, dir1_root = directory_listing(directory1)
dir2_file_list, dir2_root = directory_listing(directory2)
results = {}

for file_path in dir2_file_list.keys():
    if file_path not in dir1_file_list:
        results[file_path]="not found in "+ directory1
    else:
        filename1=os.path.join(dir1_root, file_path)
        filename2=os.path.join(dir2_root, file_path)
        if md5(filename1) != md5(filename2):
            results[file_path]="different between"+directory1+" and "+directory2
        else:
            results[file_path]="same in both directories"

for file_path in dir1_file_list.keys():
    if file_path not in results:
        results[file_path]="not found in "+ directory2

for file_path, result in sorted(results.items()):
    if os.path.sep not in file_path and "same" not in result:
        print(file_path, result)

for path, result in sorted(results.items()):
    if os.path.sep in path and "same" not in result:
        print(path, result)

