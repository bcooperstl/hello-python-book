#!/usr/bin/python3

import sys
import os

if len(sys.argv) != 2:
    print("Usage: ", sys.argv[0], "file1")
    sys.exit()

filename=sys.argv[1]
if os.access(filename, os.F_OK):
    print(filename, "already exists!")
    sys.exit()

write_file = open(filename, "w")
write_file.write("This is the first line in the file\n")
write_file.writelines(["and the second\n","and the third\n"])
write_file.close()

