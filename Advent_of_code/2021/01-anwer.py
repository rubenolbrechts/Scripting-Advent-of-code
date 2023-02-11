#!/usr/bin/python3

#formatting data
with open("01-input.txt") as f:
    data = f.read()
lines = data.split("\n")
lines.pop()

#answer 1
x_pos = 0
y_pos = 0

for line in lines:
    
    line = line.split(" ")

    if line[0][0] == 'f':
        x_pos += int(line[1])

    elif line[0][0] == 'd':
        y_pos += int(line[1])

    else:
        y_pos -= int(line[1])

solution = x_pos * y_pos
print('The x position is {} and the depth is {}. Hence, the solution is {}' .format(x_pos, y_pos,solution))

#answer 2
x_pos = 0
y_pos = 0
aim = 0

for line in lines:
    
    line = line.split(" ")

    if line[0][0] == 'f':
        x_pos += int(line[1])
        y_pos += (int(line[1])*aim)

    elif line[0][0] == 'd':
        aim += int(line[1])

    else:
        aim -= int(line[1])

solution = x_pos * y_pos
print('The x position is {} and the depth is {}. Hence, the solution is {}' .format(x_pos, y_pos,solution))