#!/usr/bin/python3
import string
import random
with open("path.txt") as f:
    data = f.read()
#print(data)

datasplit = data.split("\n")
datasplit.pop()
#print(datasplit)

print(len(datasplit))
print(len(datasplit[0]))

x_coords = 0
y_coords = 0
s = [0,0]
e = [0,0]
for ypos in datasplit:
    for xpos in ypos:
        if xpos == "S":
            s[0] = x_coords
            s[1] = y_coords
        if xpos == "E":
            e[0] = x_coords
            e[1] = y_coords       
        x_coords += 1
    y_coords += 1
    x_coords = 0

#print(s,e)
#print(datasplit[20][0], datasplit[20][46])

#Create scoring matrix
alph = string.ascii_letters
score = list(range(53))
scoring = {}
counter = 1
for letter in alph:
   scoring[letter] = scoring.get(letter, score[counter]) 
   counter += 1
#scoring["S"] = 0
starty = 21 
startx = 0
endy = 20
endx = 46
diff = [1000, 1000, 1000, 1000]
counter2 = 0
no_min = 0
counter3 = 0
print(scoring[datasplit[20][0]])
minimal = []
for cycle in range(0,100000):
    counter3 += 1
    try:  
        if abs(scoring[datasplit[starty][startx]]- scoring[datasplit[starty+1][startx]]) == 0 or abs(scoring[datasplit[starty][startx]]- scoring[datasplit[starty+1][startx]]) == 1: 
            diff[0] = abs((starty + 1) - endy) + abs(startx - endx)
            print(scoring[datasplit[starty][startx]], scoring[datasplit[starty+1][startx]], datasplit[starty][startx], datasplit[starty+1][startx])

        if abs(scoring[datasplit[starty][startx]]- scoring[datasplit[starty][startx+1]]) == 0 or abs(scoring[datasplit[starty][startx]]- scoring[datasplit[starty][startx+1]]) == 1: 
            diff[1] =  abs((starty) - endy) + abs(startx + 1 - endx) 


        if abs(scoring[datasplit[starty][startx]]- scoring[datasplit[starty-1][startx]]) == 0 or abs(scoring[datasplit[starty][startx]]- scoring[datasplit[starty-1][startx]]) == 1: 
            diff[2] = abs((starty - 1) - endy) + abs(startx - endx)  

        if abs(scoring[datasplit[starty][startx]]- scoring[datasplit[starty][startx-1]]) == 0 or abs(scoring[datasplit[starty][startx]]- scoring[datasplit[starty][startx-1]]) == 1: 
            diff[3] = abs((starty) - endy) + abs(startx - 1 - endx) 
    except:
        placeholder = ""
    
    numbers = []
    pos_no = 0
    for dif in diff:
        if dif == min(diff):
            no_min += 1
            numbers.append(pos_no)
        pos_no += 1
    if no_min == 2:
        random.shuffle(numbers)
        if numbers[0] == 0:
            starty += 1
            counter2 += 1
        elif numbers[0] == 1:
            startx += 1
            counter2 += 1
        elif numbers[0] == 2:
            starty -= 1
            counter2 += 1
        elif numbers[0] == 3:
            startx -= 1
            counter2 += 1
    elif no_min == 3:
        print("three lowest values")
    elif no_min == 4:
        print("four lowest values")

    elif diff[0] == min(diff):
        starty += 1
        counter2 += 1
    elif diff[1] == min(diff):
        startx += 1
        counter2 += 1
    elif diff[2] == min(diff):
        starty -= 1
        counter2 += 1
    elif diff[3] == min(diff):
        startx -= 1
        counter2 += 1
    try:
        if datasplit[starty][startx] == "z":
            minimal.append(counter3)
            starty = 20 
            startx = 0
            counter2 = 0
            counter3 = 0
    except:
        placeholder= ""
    no_min = 0

print(minimal)