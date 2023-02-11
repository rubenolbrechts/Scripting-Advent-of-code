#!/usr/bin/python3

with open("rps.txt", 'r') as f:
    data = f.read()

rps=list(data)
score = 0
counter = 0
#2.1
for pick in rps:
    if pick == "A":
        if rps[counter+2] == "X":
            score += 4
        elif rps[counter+2] == "Y":
            score += 8
        else:
            score += 3
    if pick == "B":
        if rps[counter+2] == "X":
            score += 1
        elif rps[counter+2] == "Y":
            score += 5
        else:
            score += 9
    if pick == "C":
        if rps[counter+2] == "X":
            score += 7
        elif rps[counter+2] == "Y":
            score += 2
        else:
            score += 6
    counter += 1
print(score)

#2.2
score = 0
counter = 0
for pick in rps:
    if pick == "A":
        if rps[counter+2] == "X":
            score += 3+0
        elif rps[counter+2] == "Y":
            score += 1+3
        else:
            score += 2+6
    if pick == "B":
        if rps[counter+2] == "X":
            score += 1+0
        elif rps[counter+2] == "Y":
            score += 2+3
        else:
            score += 3+6
    if pick == "C":
        if rps[counter+2] == "X":
            score += 2+0
        elif rps[counter+2] == "Y":
            score += 3+3
        else:
            score += 1+6
    counter += 1
print(score)