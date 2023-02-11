#!/usr/bin/python3

with open("rps.txt", 'r') as f:
    data = f.read()

rps=data.split("\n")
rps.pop()
score = 0
for pick in rps:
    
    first = pick[0]
    last = pick[2]
    
    if last == "X":
        score += 1
        if first == "A":
            score += 3
        elif first == "C":
            score += 6
    elif last == "Y":
        score += 2
        if first == "A":
            score += 6
        elif first == "B":
            score += 3
    else:
        score += 3
        if first == "B":
            score += 6
        elif first == "C":
            score += 3
print(score)
   