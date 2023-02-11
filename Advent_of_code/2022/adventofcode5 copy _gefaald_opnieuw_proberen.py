#!/usr/bin/python3
import itertools as it
with open('crane.txt') as f:
    data = f.read()

data = data.split("\n")

moves = data[9::]
moves.pop()
moves.remove('')
#print(moves) 

stack1 = ['F','T', 'C', 'L', 'R', 'P', 'G', 'Q']
stack2 = ['N', 'Q', 'H', 'W', 'R', 'F', 'S', 'J']
stack3 = ['F','B', 'H', 'W', 'P', 'M', 'Q']
stack4 = ['V', 'S', 'T', 'D', 'F']
stack5 = ['Q', 'L', 'D', 'W', 'V', 'F', 'Z']
stack6 = ['Z', 'C', 'L', 'S']
stack7 = ['Z', 'B', 'M', 'V','D', 'F']
stack8 = ['T', 'J', 'B']
stack9 = ['Q','N', 'B', 'G', 'L', 'S', 'P', 'H']
stacks = {1 : stack1, 2 : stack2, 3 : stack3, 4 : stack4, 5 : stack5, 6: stack6, 7 : stack7, 8: stack8, 9: stack9}
#print(stacks)


for move in moves:
    move = move.split(" ")
    for _ in it.repeat(None, int(move[1])):
        popped = stacks[int(move[3])].pop()
        stacks[int(move[5])] = stacks.get(int(move[5]), stacks[int(move[5])].append(popped))
#print(stacks)


#5.2
with open('crane.txt') as f:
    data = f.read()

data = data.split("\n")

moves = data[9::]
moves.pop()
moves.remove('')

stack1 = ['F','T', 'C', 'L', 'R', 'P', 'G', 'Q']
stack2 = ['N', 'Q', 'H', 'W', 'R', 'F', 'S', 'J']
stack3 = ['F','B', 'H', 'W', 'P', 'M', 'Q']
stack4 = ['V', 'S', 'T', 'D', 'F']
stack5 = ['Q', 'L', 'D', 'W', 'V', 'F', 'Z']
stack6 = ['Z', 'C', 'L', 'S']
stack7 = ['Z', 'B', 'M', 'V','D', 'F']
stack8 = ['T', 'J', 'B']
stack9 = ['Q','N', 'B', 'G', 'L', 'S', 'P', 'H']

stacks = {1 : stack1, 2 : stack2, 3 : stack3, 4 : stack4, 5 : stack5, 6: stack6, 7 : stack7, 8: stack8, 9: stack9}

popped = []
counter = 0
for move in moves:
        move = move.split(" ")
        number = int(move[1])
        for _ in it.repeat(None, number):
            if len(stacks[int(move[3])]) > 0:
                pop = stacks[int(move[3])].pop()
                print(pop)
                popped.append(pop)
                print(popped)
        for po in popped:
            stacks[int(move[5])] = stacks.get(int(move[5]), stacks[int(move[5])].append(po))
        popped = []

print(stacks)
print(stacks[1][-1],stacks[2][-1],stacks[3][-1],stacks[4][-1],stacks[5][-1],stacks[6][-1],stacks[7][-1],stacks[8][-1],stacks[9][-1])



''' DICTIONAIRY TESTING
list1 = [1,2,3,4,5,6]
list2  = [11,12,13,14,15]
diction1 = {1: list1, 2 : list2}
print(diction1)
list1.append(diction1.get(2)[-1])
print(diction1)


popped = stacks[1].pop() 
stacks[9] = stacks.get(9, stacks[9].append(popped))
print(stacks)


number = -1
popped = stacks[9][number:]
print(popped)
to_rem = ['L', 'S', 'P', 'H']
for rem in to_rem:
    stack9.remove(rem)
print(stack9)


'''