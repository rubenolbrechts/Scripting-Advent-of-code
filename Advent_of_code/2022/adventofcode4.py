#!/usr/bin/python3

#FUCK DEZE OEFENING
with open("cleaning_pairs.txt", 'r') as f:
    data = f.read()

pairs = data.split("\n")
pairs.pop()
counter = 0
#dups = []
for pair in pairs:
    
    pair = pair.split(",")
    pair1 = pair[0].split("-")
    pair2 = pair[1].split("-")

    '''
    if int(pair1[0]) == int(pair1[1]):
        dups.append(pair1)
    if int(pair2[0]) == int(pair2[1]):
        dups.append(pair2)
    '''
  
    if int(pair2[0]) in range(int(pair1[0]), int(pair1[1])+1) and int(pair2[1]) in range(int(pair1[0]), int(pair1[1])+1):
        counter +=1
        
    elif int(pair1[0]) in range(int(pair2[0]), int(pair2[1])+1) and int(pair1[1]) in range(int(pair2[0]), int(pair2[1])+1):
        counter +=1

print(counter)
#print(len(dups))

#4.2
counter = 0
for pair in pairs:

    pair = pair.split(",")
    pair1 = pair[0].split("-")
    pair2 = pair[1].split("-")

    if int(pair2[0]) in range(int(pair1[0]), int(pair1[1])+1) or int(pair2[1]) in range(int(pair1[0]), int(pair1[1])+1):
        counter +=1
        
    elif int(pair1[0]) in range(int(pair2[0]), int(pair2[1])+1) or int(pair1[1]) in range(int(pair2[0]), int(pair2[1])+1):
        counter +=1

print(counter)