#!/usr/bin/python3
import string

with open("rucksack.txt", 'r') as f:
    data = f.read()

items = data.split("\n")

#3.1

faulty = ''
for item in items:
    length = int(len(item)/2)
    first = item[0:length]
    second = item[length::]
    for w in set(first):
        if w in second:
            faulty += w

#print(faulty)

#Create scoring matrix
alph = string.ascii_letters
score = list(range(53))
scoring = {}
counter = 1
for letter in alph:
   scoring[letter] = scoring.get(letter, score[counter]) 
   counter += 1

#print(scoring)

summ = 0
for w in faulty:
    if w in scoring:
        summ += scoring.get(w)
print(summ)

#3.2

badges = []
counter = -1
for item in items:
    counter += 1
    if counter % 3 == 0:
        for w in item:
            if w in items[counter+1] and w in items[counter+2]:
                badges.append(w)
                break
    
#print(badges)

summ = 0
for w in badges:
    if w in scoring:
        summ += scoring.get(w)
print(summ)