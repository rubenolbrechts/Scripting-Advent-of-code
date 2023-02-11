#!/usr/bin/python3

with open('rope.txt') as f:
    data = f.read().split("\n")
data.pop()

'''
up = 0
down = 0
left = 0
right = 0
for dir in data:
    dir = dir.split(' ')
    if dir[0] == 'R':
        right += int(dir[1])
    elif dir[0] == 'L':
        left += int(dir[1])    
    elif dir[0] == 'U':
        up += int(dir[1]) 
    elif dir[0] == 'D':
        down += int(dir[1])    

height = up - down
width = left - right
print(up, down, left, right)
print('height: {}, width {}' .format(height, width))
'''

x_posH = 500
y_posH = 500
x_posT = 500
y_posT = 500
grid = []
counter = 0
for x in range(0,1000):
    grid.append([])
    for y in range(0, 1000):
        grid[counter].append('0')
    counter += 1
grid[500][500] = '#'
for dir in data:
    dir = dir.split(' ')
    for x in range(0,int(dir[1])):
        if dir[0] == 'R':
            x_posH += 1
        elif dir[0] == 'L':
            x_posH -= 1   
        elif dir[0] == 'U':
            y_posH += 1
        elif dir[0] == 'D':
            y_posH -= 1  
        
        if abs(x_posH-x_posT) + abs(y_posH-y_posT) > 2:
            if x_posH-x_posT >= 1 and y_posH-y_posT >= 1:
                x_posT += 1
                y_posT += 1
                grid[x_posT][y_posT] = '#'
            elif x_posH-x_posT <= -1 and y_posH-y_posT >= 1: 
                x_posT -= 1
                y_posT += 1
                grid[x_posT][y_posT] = '#'
            elif x_posH-x_posT <= -1 and y_posH-y_posT <= -1: 
                x_posT -= 1
                y_posT -= 1
                grid[x_posT][y_posT] = '#'
            elif x_posH-x_posT >= 1 and y_posH-y_posT <= -1: 
                x_posT += 1
                y_posT -= 1
                grid[x_posT][y_posT] = '#'
        elif x_posH - x_posT > 1:
             x_posT += 1
             grid[x_posT][y_posT] = '#'
        elif x_posH - x_posT < -1:
            x_posT -= 1
            grid[x_posT][y_posT] = '#'
        elif y_posH - y_posT > 1:
            y_posT += 1
            grid[x_posT][y_posT] = '#'
        elif y_posH - y_posT < -1:
            y_posT -= 1
            grid[x_posT][y_posT] = '#'

print(x_posH, y_posH, x_posT, y_posT)
positions = 0
for y in grid:
    for x in y:
        if x == '#':
            positions +=1

print(positions)

# part 2
x_posH = 500
y_posH = 500
grid = []
counter = 0
for x in range(0,1000):
    grid.append([])
    for y in range(0, 1000):
        grid[counter].append('0')
    counter += 1

grid[500][500] = '#'
x_pos = {}
y_pos = {}
for x in range(1,10):
    x_pos[x] = 500
    y_pos[x] = 500
print(x_pos, y_pos)

for dir in data:
    dir = dir.split(' ')
    for x in range(0,int(dir[1])):
        if dir[0] == 'R':
            x_posH += 1
        elif dir[0] == 'L':
            x_posH -= 1   
        elif dir[0] == 'U':
            y_posH += 1
        elif dir[0] == 'D':
            y_posH -= 1  
        for x in range(1,10):
            if x == 1:
                if abs(x_posH-x_pos[x]) + abs(y_posH-y_pos[x]) > 2:
                    if x_posH-x_pos[x] >= 1 and y_posH-y_pos[x] >= 1:
                        x_pos[x] += 1
                        y_pos[x] += 1
                        grid[x_pos[9]][y_pos[9]] = '#'
                    elif x_posH-x_pos[x] <= -1 and y_posH-y_pos[x] >= 1: 
                        x_pos[x] -= 1
                        y_pos[x] += 1
                        grid[x_pos[9]][y_pos[9]] = '#'
                    elif x_posH-x_pos[x] <= -1 and y_posH-y_pos[x] <= -1: 
                        x_pos[x] -= 1
                        y_pos[x] -= 1
                        grid[x_pos[9]][y_pos[9]] = '#'
                    elif x_posH-x_pos[x] >= 1 and y_posH-y_pos[x] <= -1: 
                        x_pos[x] += 1
                        y_pos[x] -= 1
                        grid[x_pos[9]][y_pos[9]] = '#'
                elif x_posH - x_pos[x] > 1:
                    x_pos[x] += 1
                    grid[x_pos[9]][y_pos[9]] = '#'
                elif x_posH - x_pos[x] < -1:
                    x_pos[x] -= 1
                    grid[x_pos[9]][y_pos[9]] = '#'
                elif y_posH - y_pos[x] > 1:
                    y_pos[x] += 1
                    grid[x_pos[9]][y_pos[9]] = '#'
                elif y_posH - y_pos[x] < -1:
                    y_pos[x] -= 1
                    grid[x_pos[9]][y_pos[9]] = '#'
            else: 
                if abs(x_pos[x-1]-x_pos[x]) + abs(y_pos[x-1]-y_pos[x]) > 2:
                    if x_pos[x-1]-x_pos[x] >= 1 and y_pos[x-1]-y_pos[x] >= 1:
                        x_pos[x] += 1
                        y_pos[x] += 1
                        grid[x_pos[9]][y_pos[9]] = '#'
                    elif x_pos[x-1]-x_pos[x] <= -1 and y_pos[x-1]-y_pos[x] >= 1: 
                        x_pos[x] -= 1
                        y_pos[x] += 1
                        grid[x_pos[9]][y_pos[9]] = '#'
                    elif x_pos[x-1]-x_pos[x] <= -1 and y_pos[x-1]-y_pos[x] <= -1: 
                        x_pos[x] -= 1
                        y_pos[x] -= 1
                        grid[x_pos[9]][y_pos[9]] = '#'
                    elif x_pos[x-1]-x_pos[x] >= 1 and y_pos[x-1]-y_pos[x] <= -1: 
                        x_pos[x] += 1
                        y_pos[x] -= 1
                        grid[x_pos[9]][y_pos[9]] = '#'
                
                elif x_pos[x-1] - x_pos[x] > 1:
                    x_pos[x] += 1
                    grid[x_pos[9]][y_pos[9]] = '#'
                elif x_pos[x-1] - x_pos[x] < -1:
                    x_pos[x] -= 1
                    grid[x_pos[9]][y_pos[9]] = '#'
                elif y_pos[x-1] - y_pos[x] > 1:
                    y_pos[x] += 1
                    grid[x_pos[9]][y_pos[9]] = '#'
                elif y_pos[x-1] - y_pos[x] < -1:
                    y_pos[x] -= 1
                    grid[x_pos[9]][y_pos[9]] = '#'

positions = 0
for y in grid:
    for x in y:
        if x == '#':
            positions +=1

print("last:", positions)
print(x_posH, y_posH,x_pos, y_pos)