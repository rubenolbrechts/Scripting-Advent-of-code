#!/usr/bin/python3

file1 = input("Give me a file name: ")

name = file1.split(".")

print("Sample filename:" + file1)
print("Output: " + name[0])