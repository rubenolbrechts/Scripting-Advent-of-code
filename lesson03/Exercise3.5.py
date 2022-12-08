#!/usr/bin/python3

#3.5.a
'''

list1 = input("Give me a list: ")

list1 = list1.split(",")

int_list1= [eval(i) for i in list1]

max1 = max(int_list1)

print("The largest number of the list is {}" .format(max1))
#see leho for the actual loop answer



#3.5.b

num = int(input("Enter integers to calculate sum and average.\n Input 0 to exit.\n"))
num_lst = []

while num != 0:
    num_lst.append(num)
    num = int(input(""))

print("Calculating sum and avarage for the above numbers:")

sum1 = sum(num_lst)
print("Sum = {}" .format(sum1))

avg = round(sum1 / len(num_lst),2)
print("Average = {}" .format(avg))

'''

#3.5.c

#Input.split apperently also works (in 1 line!)
list2 = input("Give me a list with strings bro: ")

list2 = list2.split(",")

print("Input words: {}".format(list2))

#Actual question was to only use STRINGS larger than 2, not the list larger than 2
if len(list2) > 2:

    length = len(list2)
    print("Number of strings: {}" .format(length))

list3 = []
for string in list2:

    if string[0] == string[len(string) - 1]:
        #last character is also just [-1]
        list3.append(string)

print("List of these words: {}" .format(list3))

