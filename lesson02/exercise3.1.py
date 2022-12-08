#!/usr/bin/python3
#3.1.a

list1 = [1, 4, 9, 16, 25, 46, 64, 81, 100]
list2 = []
for item in list1 :
    if item % 2 == 0 :
        list2.append(item)
print(list2)

#3.2.b
from datetime import date 

birth = [1990, 1995, 1990, 1991, 1992, 1991]
ages = []
for years in birth:
    yob = date.today().year - years
    ages.append(yob)
print(ages)
