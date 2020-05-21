#!/usr/bin/python3

from hashlib import md5
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
my_hash = md5()
for line in read_file.readlines():
    my_hash.update(line.encode('utf-8'))
read_file.close()
print(filename, ":", my_hash.hexdigest())
