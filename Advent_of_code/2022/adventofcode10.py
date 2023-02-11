#!/usr/bin/python3

with open("addx.txt") as f:
    data = f.read().split("\n")
data.pop()

cycle = 1
x = 1
signalsum = 0
flag = 0
for dat in data:
    dat = dat.split(" ")
    if cycle % (20+flag) == 0:
        signalsum = signalsum + (cycle*x)
        flag = flag + 40
    if dat[0] == "noop":
        cycle += 1
    if dat[0] == "addx":
        cycle += 1
        if cycle % (20+flag) == 0:
            signalsum = signalsum + (cycle*x)
            flag = flag + 40
        cycle += 1
        x = x + int(dat[1])
        if cycle % (20+flag) == 0:
            signalsum = signalsum + (cycle*x)
            flag = flag + 40
         
   
print(signalsum, cycle)
