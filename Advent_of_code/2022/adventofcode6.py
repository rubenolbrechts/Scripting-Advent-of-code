#!/usr/bin/python3

with open("device.txt") as f:
    data = f.read()
check1 = ""
check2 = ""
check3 = ""
check4 = ""
full = ""
flag = 'true'
counter = 1


for let in data:
    full += let
    if flag == 'true':
        if len(check1) == 0:
            check1 += let
            #print(check1)
        elif (counter + 3) % 4 == 0:
            check2 += check1
            check2 += let
            counter += 1
            #print(check2)
        elif (counter + 2) % 4 == 0:
            check3 += check2
            check2 = ""
            check3 += let
            counter += 1
            #print(check3)
        elif (counter + 1) % 4 == 0:
            check4 += check3
            check4 += let
            check3 = ""
            counter += 1
            #print(check4) 
            flag = 'false'
    else:
        if counter % 4 == 0: 
            check1 = ""
            check1 += check4
            check1 += let
            check1 = check1[1::]
            check4 = ""
            counter += 1  
            if len(set(check1)) == len(check1):
                found = check1
                print(found)
                break
        elif (counter + 3) % 4 == 0:
            check2 += check1
            check1 = ""
            check2 += let
            check2 = check2[1::]
            counter += 1
            if len(set(check2)) == len(check2):
                found = check2
                print(found)
                break
        elif (counter + 2) % 4 == 0:
            check3 += check2
            check2 = ""
            check3 += let
            check3 = check3[1::]
            counter += 1
            if len(set(check3)) == len(check3):
                found = check3
                print(found)
                break
        elif (counter + 1) % 4 == 0:
            check4 += check3
            check4 += let
            check3 = ""
            check4 = check4[1::]
            counter += 1
            if len(set(check4)) == len(check4):
                found = check4
                print(found)
                break

print("The first marker appears after {} characters" .format(len(full)))

