#!/usr/bin/python3

import sys
import os

if len(sys.argv) != 2:
    print("Usage: ", sys.argv[0], "file1")
    sys.exit()

filename=sys.argv[1]
if not os.access(filename, os.F_OK):
    print(filename, "isn't a valid filename!")
    sys.exit()

read_file = open(filename, "r")
file_contents = list(read_file.readlines())
read_file.close()
print("Read in",len(file_contents),"lines from",filename)
print("The first line reads:", file_contents[0])
