#!/usr/bin/python3

with open("trees.txt") as f:
    data = f.read()

data = data.split("\n")
data.pop()
data[0] = data[0] + "#"
data[-1] = data[-1] + "#"
flag = "stop"
row = 1
counter = 0
visible = 0

for trees in data:
    if trees[-1] == "#":
        print('hi')
        continue
    '''
    elif data[row][-1] == "#":
        print(trees, "hi")
        print(visible)
        exit()
    
    elif flag == "stop":
        flag = "start"
        continue
    '''
    for tree in trees:
        if counter == 0:
            counter += 1
            continue
        elif counter == 98:
            print(trees, row, "stop")
            counter = 0
            row += 1
            break
                        
        if tree > data[row][counter-1]:
            #print('a')
            if tree > data[row][counter+1]:
                #print('b')
                if tree > data[row+1][counter]:
                    #print('c')
                    if  tree > data[row-1][counter]:
                        #print('d')
                        visible += 1
                        print(tree, "\t", counter)
                        print(data[row][counter-1])
                        print(data[row][counter+1])
                        print(data[row+1][counter])
                        print(data[row-1][counter])
                       
        counter += 1
print(visible)