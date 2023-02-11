#!/usr/bin/python3

with open("02-input.txt") as f:
    data = f.read()
lines = data.split("\n")
lines.pop()

#awnser1

length = len(lines)
position = 0
zeros = 0
ones = 0
gamma = ""
epsilon = ""

#Create repetition for each character in the bit
for repetitions in lines[0]:
    #Create repetition for each bit in the list
    for bin_number in range(0,length):
        if lines[bin_number][position] == '0':
            zeros += 1
        else:
            ones += 1
    if zeros > ones:
        gamma += "0"
        epsilon += "1" 
    else:
        gamma += "1"
        epsilon += "0"         
    position += 1
    zeros = 0
    ones = 0

dec_gamma = int(gamma,2)
dec_epsilon = int(epsilon,2)

consumption = dec_gamma * dec_epsilon
print(consumption)

#anwser2

length = len(lines)
position = 0
zeros_most = 0
ones_most = 0
zeros_least = 0
ones_least = 0
most = ""
least = ""

#Create repetition for each character in the bit
for repetitions in lines[0]:
    #Create repetition for each bit in the list
    for bin_number in range(0,length):
        #find the bits that begin with most common bits
        if lines[bin_number][0:position] == most or position == 0:
            if lines[bin_number][position] == '0':
                zeros_most += 1
            else:
                ones_most += 1
        #find the bits that begin with least common bits
        if lines[bin_number][0:position] == least or position == 0:
            if lines[bin_number][position] == '0':
                zeros_least += 1
            else:
                ones_least += 1

    if zeros_most > ones_most:
        most += '0'
    elif zeros_most <= ones_most:
        most += '1'
    
    #Be careful not to include 0 or 1 when there is no single occurence of the value!
    if zeros_least > ones_least and ones_least != 0:
        least += '1'
    elif zeros_least <= ones_least and zeros_least != 0:
        least += '0'
    elif ones_least == 0:
        least += '0'
    elif zeros_least == 0:
        least += '1'

    zeros_most = 0
    ones_most = 0
    zeros_least = 0
    ones_least = 0
    position += 1


oxygen = int(most,2)
carbon = int(least,2)
life_support = carbon * oxygen

print(life_support)