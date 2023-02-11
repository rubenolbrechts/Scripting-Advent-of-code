#!/usr/bin/python3
import string

with open('crane.txt') as f:
    data = f.read()

data = data.split("\n")

crates = data[0:8] 
#print(crates)
counter = 1
crate_dict = {}
crate_dict2 = {}
for crate in crates:
    if crate != '' and crate != ' ':
        crate.strip() 
        crate_dict[counter] = crate_dict.get(counter, crate)
        counter +=1
counter = 1

for key,crate in crate_dict.items():
    crate =list(crate)
    crate_dict2[counter] = crate_dict2.get(counter, crate)
    counter +=1
print(crate_dict2)
crate_dict3 = {}
counter = 1
empty = 0
cool = ''
alph = string.ascii_letters
for key,crate in crate_dict2.items(): 
    for crat in crate:
        if crat not in alp:
            empty += 1
        if empty == 5:
            print(empty)
            empty == 0
            counter += 1
        if crat in alph:
            crate_dict3[counter] = crate_dict3.get(counter, cool.__add__(crat))
            empty == 0
            counter += 1
    counter = 1
    

print(crate_dict3)   

