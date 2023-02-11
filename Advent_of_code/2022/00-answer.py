#!/usr/bin/python3
import os

#print(os.listdir("/home/guest/Shared/Adventofcode"))

with open("calories.txt", 'r') as f:
    data = f.read()

per_elf=data.split("\n")
elf_list = {}
#cal_list = []
total = 0
count = 1
for cal in per_elf:
    if cal != '':
        #cal_list.append(cal)
        total = total + int(cal)
        current_elf = "Elf " + str(count)
        #elf_list[current_elf] = cal_list
        elf_list[current_elf] = total
    else:   
        count +=1
        #cal_list = []
        total = 0

MVP_elf = max(elf_list, key=elf_list.get)

print("\n{} carries the most amount of calories: {}\n" .format(MVP_elf,elf_list[MVP_elf]))

#1.2

elf_list2 = {k: v for k, v in sorted(elf_list.items(), key=lambda item: item[1])}

total = list(elf_list2.values())[-1] + list(elf_list2.values())[-2] + list(elf_list2.values())[-3] 

print("Best elf: ", list(elf_list2)[-1], "Calories: ", list(elf_list2.values())[-1], "2nd Best elf: ", list(elf_list2)[-2], "Calories: ", list(elf_list2.values())[-2], " 3rd Best elf: ", list(elf_list2)[-3], "Calories: ", list(elf_list2.values())[-3], "Total amount: ", total,"\n")
 
#print("{} carries the most amount of calories: {} ; {} the 2nd most: {} ; {} the 3rd most {}" .format(MVP_elf,elf_list[MVP_elf],elf_list2.keys()[-2], elf_list2.values()[-2], elf_list2.keys()-[3], elf_list2.values()[-3]))