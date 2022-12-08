#!/usr/bin/python3
import os

#print(os.listdir("/home/guest/Shared/Adventofcode"))

with open("calories.txt", 'r') as f:
    data = f.read()


per_elf=data.split("\n")
print(per_elf)
cal_list = []
count = 1
cal_list.append(count)
for cal in per_elf:
    if cal != '':
        cal_list.append(cal)
    else:
        count +=1
        cal_list.append(count)


print(cal_list)