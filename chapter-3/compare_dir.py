#!/usr/bin/python3

import sys
import os

if len(sys.argv) != 3:
    print("Usage: ", sys.argv[0], "<directory 1> <directory 2>")
    sys.exit()

directory1 = sys.argv[1]
directory2 = sys.argv[2]

print("Comparing ", directory1, directory2)
print()

for directory in [directory1, directory2]:
    if not os.access(directory, os.F_OK):
        print(directory, "isn't a valid directory!")
        sys.exit()
    print("Directory", directory)
    for item in os.walk(directory):
        print("",item)
    print()
