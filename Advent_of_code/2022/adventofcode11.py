#!/usr/bin/python3

with open("monkey.txt") as f:
    data = f.read().split("\n\n")

monkeys = {}
monkey_throw = {}
flag = "monkey"
counter = 0
for dat in data:
    dat = dat.split(" ")
    if "Monkey" in dat[0]:
        for da in dat:
            if da == '':
                continue
            if flag == "monkey":
                flag = "number"
                continue
            if flag == "number":
                monkeys[counter] = []
                monkey_throw[counter] = []
                flag = "starting"
            if flag == "starting":
                flag = "items"
                continue
            if flag == "items":
                flag = "item_no"
                continue
            if flag == "item_no":
                monkeys[counter] += da
                print(monkeys)
                exit()

print(monkeys)