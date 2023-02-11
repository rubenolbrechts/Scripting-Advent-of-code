#!/usr/bin/python3

#Data formatting
with open("00-input.txt") as f:
    data = f.read()
lines = data.split("\n")
lines.pop()
lines = [eval(i) for i in lines]

#Answer 1
value = int(lines[0])
amount = 0

for line in lines[1::]:

    if int(line) > int(value):
        amount+= 1
    value = line

print("The depth is incremented {} times." .format(amount))

#Anwer 2
first = 3
amount = 0
sum1 = 0
sum2 = 0
length = len(lines)

for window in range(0,length+1):

    sum1 = sum(lines[window:first])
    sum2 = sum(lines[window+1:first+1])
    first += 1
    
    if sum2 > sum1:
        amount += 1

print("The values in the sliding windows are incremented {} times." .format(amount))