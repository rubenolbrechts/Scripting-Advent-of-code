#!/usr/bin/python3
#Pyhton basic part II ! ! 

num = input("Give me sequence of numbers: ")
num_lst = []

for numbers in num :
    if numbers not in num_lst:
        num_lst.append(numbers)

if len(num_lst) < len(num):
    print("They are not all different")
else:
    print("They are all different")