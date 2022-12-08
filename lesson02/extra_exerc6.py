#!/usr/bin/python3

sample = input("Give me comma-serepated numbers: ")

list1 = sample.split(",")
tuple1 = tuple(list1)
print(list1)
print(tuple1)