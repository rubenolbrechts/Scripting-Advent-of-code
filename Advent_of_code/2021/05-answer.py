#!/usr/bin/python3
with open('05-input.txt') as f:
    line = f.read()

#preprocess data
#delete all commas so we have a string of only numbers
line = line.replace(',' , '')
#delete \n at the end of string
line = line[:-1]
fishies = []

#Add numbers in new list fishies, do 1 generation at the same time
for j in line:

    #move internal timer
    j = int(j[0]) - 1 
    fishies.append(str(j))


#For answer 1: do next 79 generations
#For answer 2: do next 255 generations => too inefficient to handle this! Better algoritms below!!!!!!!!!!!!!!!!
gens = 79

new_fishies = []
index = 0

for i in range(0,gens):

    index = 0
    new_fishies = []

    for j in fishies:

        #if the character is 0 => create new fish with internal timer of 8. 
        # BUT this fish's clock will not be moved this iteration => add 2nd character which will be removed this iteration(bigger than 0 or j-1 will leave the first char at 7)
        if int(j) == 0:
            fishies[index] = '6'
            new_fishies.append('8')
            index += 1
            continue

        #move internal timer
        j = int(j[0]) - 1 
        fishies[index] = str(j)
        index += 1

    fishies.extend(new_fishies)

print(len(fishies))

#More efficient algorithm to handle more generations! big O(n)
fishies = [0,0,0,0,0,0,0,0,0]

#create list with the fishies with their current internal clock at the start
gens = 256
for j in line:

    fishies[int(j)] += 1

print(fishies)

for reps in range(gens):

    zeros = fishies[0]
    eights = fishies[8]
    
    #The sum of the fishes with their respective timer is moved one index lower => simulates each fish getting one day closer to spawning new ones
    fishies[0:-1] = fishies[1:-1]
    #append newborn fishes with timer 8: zeros from current gen
    fishies.append(zeros)
    #Fishes with clock 0 just gave birth and became fishes with clock 6 => add them to list
    fishies[6] += zeros

print(fishies)
print(sum(fishies))
