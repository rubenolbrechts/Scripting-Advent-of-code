#!/usr/bin/python3
from math import factorial

with open('06-input.txt') as f:
    line = f.read()

#preprocess data
line = line.split(',')

#answer 1
tot_fuel = {}

def fuel(inp, position):

    for i in inp:

        try: 
            tot_fuel[position] += abs(int(i)- position)
        except:
            tot_fuel[position] = abs(int(i)- position)

for j in range(0,1000):

    fuel(line,j)

best_pos = min(tot_fuel, key=tot_fuel.get)
best_fuel = tot_fuel[best_pos]
print(best_fuel)

#answer 2
tot_fuel = {}

def exp_fuel(inp, position):

    for i in inp:

        #Calculate distance between value and certain position => by adding up all numbers from 1 to the difference we find de desired value
        n = sum(range(1,(abs(int(i) - position)+1)))

        try: 
            tot_fuel[position] += n
        except:
            tot_fuel[position] = n

for j in range(0,1000):

    exp_fuel(line,j)

best_pos = min(tot_fuel, key=tot_fuel.get)
best_fuel = tot_fuel[best_pos]
print(best_fuel)