#!/usr/bin/python3

truth = {"lists" : "stupid", "dictionaries": "awesome"}

for key, values in truth.items():
    print("{} are {}." .format(key, values))