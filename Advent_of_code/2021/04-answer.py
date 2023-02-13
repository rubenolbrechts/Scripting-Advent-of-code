#!/usr/bin/python3
import re

with open('04-input.txt') as f:
    data = f.read()
lines = data.split('\n')
lines.pop()

#answer 1

#coords[x1,y1,x2,y2]
x = []
y = []

#find dimensions of grid => 1000 by 1000
for line in lines:

    coords = re.findall("[\\d]+", line)
    x.append(int(coords[0]))
    x.append(int(coords[2]))
    y.append(int(coords[1]))
    y.append(int(coords[3]))

print(max(x), max(y))

#create 1000x1000 matrix

matrix = {}

for i in range(0,1000):
    matrix[i] = list(0 for j in range(0,1000))

#increase value of matrix where values correspond to coords
for line in lines:

    coords = re.findall("[\\d]+", line)
    
    #look for coords where either x or y doesn't change 
    if coords[0] == coords[2]:
        y_min = min([int(coords[1]),int(coords[3])])
        y_max = max([int(coords[1]),int(coords[3])])

        #increment matrix at coords positions
        for n in range(y_min,y_max+1):
            matrix[n][int(coords[0])] += 1 
    
    if coords[1] == coords[3]:
        x_min = min([int(coords[0]), int(coords[2])])
        x_max = max([int(coords[0]), int(coords[2])])
        
        for n in range(x_min,x_max+1):
            matrix[int(coords[1])][n] += 1 

    else:
        continue

#find how many positions have at least a 2 in the matrix
amount = 0
for rows in matrix.values():

    for value in rows:

        if value >= 2:
            amount += 1

print(amount)

#answer 2

#create 1000x1000 matrix
matrix = {}

for i in range(0,1000):
    matrix[i] = list(0 for j in range(1,1001))

#increase value of matrix where values correspond to coords
for line in lines:

    coords = re.findall("[\\d]+", line) 
    y_min = min([int(coords[1]),int(coords[3])])
    y_max = max([int(coords[1]),int(coords[3])])
    x_min = min([int(coords[0]), int(coords[2])])
    x_max = max([int(coords[0]), int(coords[2])])

    #look for coords where either x or y doesn't change      
    if coords[0] == coords[2]:

        #increment matrix at coords positions
        for n in range(y_min,y_max+1):
            matrix[(n)][int(coords[0])] += 1 
    
    elif coords[1] == coords[3]:
        for n in range(x_min,x_max+1):
            matrix[int(coords[1])][n] += 1 

    else:

        """
        Look for coords where both x and y change => diagonal lines :'(
        Brainstorm about problem:

        if ydiff and xdiff > 0

            s = startpositie, c = stap tot einde
                 0	1	2	3	4	5

            0	    0	0	0	0	0	0
            1	    0	s	0	0	0	0
            2	    0	0	c	0	0	0		start bij minwaarden => +1 tot max waarden
            3	    0	0	0	c	0	0
            4	    0	0	0	0	c	0
            5	    0	0	0	0	0	c

        if ydiff and xdiff < 0

                 0	1	2	3	4	5

            0	    0	0	0	0	0	0
            1	    0	c	0	0	0	0
            2	    0	0	c	0	0	0		start bij maxwaarden => -1 tot minwaarden
            3	    0	0	0	c	0	0
            4	    0   0	0	0	s	0
            5	    0	0	0	0	0	0

        if ydiff > 0 en xdiff < 0

                    0	1	2	3	4	5

            0	    0	0	0	0	0	0
            1	    0	0	0	0	s	0
            2	    0	0	0	c	0	0		start bij ymin en xmax => ymin +1 en xmax -1 tot tot einde
            3	    0	0	c	0	0	0
            4	    0   c	0	0	0	0
            5	    0	0	0	0	0	0

        if ydiff < 0 en xdiff > 0

                    0	1	2	3	4	5

            0	    0	0	0	0	0	0
            1	    0	0	0	0	c	0
            2	    0	0	0	c	0	0		start bij xmin en ymax => ymax -1 en xmin +1 tot einde
            3	    0	0	c	0	0	0
            4	    0	s	0	0	0	0
            5	    0	0	0	0	0	0
        """

        #Code to solve problem visualized above
        x_diff = int(coords[0]) - int(coords[2])
        y_diff = int(coords[1]) - int(coords[3])

        if x_diff > 0 and y_diff > 0:
            while x_min-1 != x_max:
                matrix[y_min][x_min] += 1
                y_min += 1
                x_min += 1

        elif x_diff < 0 and y_diff < 0:
            while x_max+1 != x_min:
                matrix[y_max][x_max] += 1
                y_max -= 1
                x_max -= 1

        elif x_diff < 0 and y_diff > 0:
            while x_max+1 != x_min:
                matrix[y_min][x_max] += 1
                y_min += 1
                x_max -= 1


        elif x_diff > 0 and y_diff < 0:
            while x_min-1 != x_max:   
                matrix[y_max][x_min] += 1
                y_max -= 1
                x_min += 1

#find how many positions have at least a 2 in the matrix
amount = 0
for rows in matrix.values():

    for value in rows:

        if value >= 2:
            amount += 1

print(amount)
