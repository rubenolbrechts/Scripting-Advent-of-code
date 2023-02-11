#!/usr/bin/python3

#########################################################################################################
''' 
--- Day 5: Supply Stacks ---
The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of marked crates, but because the needed supplies are buried under many other crates, the crates need to be rearranged.

The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, the desired crates will be at the top of each stack.

The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her which crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.

They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input). For example:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top. Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a single crate, P.

Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:

[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 
In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate to be moved (D) ends up below the second and third crates:

        [Z]
        [N]
    [C] [D]
    [M] [P]
 1   2   3
Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up below crate M:

        [Z]
        [N]
[M]     [D]
[C]     [P]
 1   2   3
Finally, one crate is moved from stack 1 to stack 2:

        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3
The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.

After the rearrangement procedure completes, what crate ends up on top of each stack?

Your puzzle answer was SHMSDGZVC.
'''
#########################################################################################################

# Extracting information from file
import re

collect = open("crane.txt", "r")
lines = collect.readlines()
collect.close()

# Saving all of the different lines in 2 distinct lists: rows and moves
# Rows = Boxes per line
# Moves = Moves per line

flag = "boxes"
rows = []
moves = []
for x in lines:
    y = x.strip("\n")
    
    # There is a newline between the boxes and the moves. 
    # If this newline is encountered, the lines are stored in moves.
    if y == "":
        flag = "moves"
        continue

    # The boxes per line are stored in the variable rows
    if flag == "boxes":
        rows.append(re.findall("\\s{4}|[A-Z]|[0-9]", y))
    
    # The moves per line are stored in the variable moves
    if flag == "moves":
        moves.append(y)

# We have a variable called rows. 
# Here, the boxed are saved per line and not per stack.
# To convert boxes per line to boxes per stack, we do the following:

flag2 = "NOK"
stacks = []
for x in rows:
    
    if flag2 == "NOK":
        
        for y in range(0, len(x)):
            stacks.append([])
        print(stacks)
        flag2 = "OK"

    for y in range(0, len(x)):
        if x[y] == "    ":
            continue
        else:    
            stacks[y].append(x[y])
print(stacks)

# The stacknumber is still attached at the end of each stack sublist.
# We remove the numbers at the end of each stack sublist
for x in stacks:
    x.pop()


# Next, we will take a look at the moves.
# The moves are described as 'move a from b to c'
# We want to extract the numbers a, b and c
move_extract = []

for x in moves:
    move_extract.append(re.findall("[0-9]{1,100}", x))

# Now that we have simplified the moves, we will arrange the blocks!
for y in move_extract:
    for x in range(0,int(y[0])):
        popped = stacks[int(y[1]) - 1].pop(0)
        stacks[int(y[2]) - 1].insert(0, popped)

# Let us determine the highest stack!
max = 0
for x in stacks:
    if len(x) > max:
        max = len(x)

# Let's put empty blocks (4 spaces) on top of the stacks that are lower than the highest stack!
for x in stacks:
    if max > len(x):
        for y in range(0, (max - len(x))):
            x.insert(0, "")

# Let's prinrt the stacks again!
for x in range(0, len(stacks[0])):
    for y in stacks:
        if y[x] ==  "":
            print("    ", end = "")
        else:
            print("[{}] ".format(y[x]), end = "")
    
    print("")

for x in range(1, len(stacks)+1):
    print(" {}  ".format(x), end = "")
print("")