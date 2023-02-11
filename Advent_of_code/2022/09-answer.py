#!/usr/bin/python3

with open("addx.txt") as f:
    data = f.read().split("\n")
data.pop()

cycle = 0
x = 1
screen = {1 : "",2 : "", 3 : "", 4 : "", 5 : "", 6 : "", 7 : ""}
row = 1
flag = 41
for dat in data:
    dat = dat.split(" ")
    '''
    if cycle % flag == 0:
        row += 1
        cycle = 1
        print(flag)
    '''
    if cycle == x or cycle == x-1 or cycle == x+1:
        screen[row] += "#"
    else:
        screen[row] += "." 
    if dat[0] == "noop":
        cycle += 1
        if cycle % flag == 0:
            row += 1
            cycle = 1
            print(flag)
    if dat[0] == "addx":
        cycle += 1
        if cycle % flag == 0:
            row += 1
            cycle = 1
            print(flag)
        if cycle == x or cycle == x-1 or cycle == x+1:
            screen[row] += "#"
        else:
            screen[row] += "." 
        cycle += 1
        x = x + int(dat[1])
        if cycle % flag == 0:
            row += 1
            cycle = 1
            print(flag)
        '''
        if cycle == x or cycle == x-1 or cycle == x+1:
            screen[row] += "#"
        else:
            screen[row] += "." 
        '''
print("\n",screen[1],"\n",screen[2], "\n",screen[3], "\n",screen[4], "\n",screen[5], "\n",screen[6], "\n",)
#print(len(screen[1]), len(screen[2]),len(screen[3]),len(screen[4]),len(screen[5]),len(screen[6]))
#print(screen)
