#!/usr/bin/python3

with open('03-input.txt') as f:
    data = f.read()
lines = data.split('\n')
lines.pop()

#awnser 1

#define variables

numbers = lines[0].split(",")
lines = lines[2::]
first = []
second = []
third = []
fourth = []
fifth = []
row = 0
board = 0
bingo_turn = {}
turns = 0   
last_value = 0
flag = 'no'
score = {}

#define functions

def n_to_x(list,index,value):
    if list[index] == value:
        list[index] = 'x'
    
def vert_row(index):
    row = first[index] + second[index] + third[index] + fourth[index] + fifth[index]
    return row

def calc_score(lists):
    for list in lists:
        for x in list:
            if x != 'x':
                score[board] += int(x)   
    score[board] = score[board] * int(last_value)   

for line in lines:

    #first make 5 lists with rows, when line = '': do calculations
    if line == '':
        row = 0
        board += 1
 
        for number in numbers:

            last_value = number
            
            #change called numbers to an x in the list
            for n in range(len(first)):

                n_to_x(first,n,number)
                n_to_x(second,n,number)
                n_to_x(third,n,number)
                n_to_x(fourth,n,number)
                n_to_x(fifth,n,number)

            #check for bingo (5 times x) in horizontal rows
            if ''.join(first) == 'xxxxx':
                bingo_turn[board] = turns   
                flag = 'BINGO' 

            elif ''.join(second) == 'xxxxx':
                bingo_turn[board] = turns   
                flag = 'BINGO'
            
            elif ''.join(third) == 'xxxxx':
                bingo_turn[board] = turns   
                flag = 'BINGO' 
             
            elif ''.join(fourth) == 'xxxxx':
                bingo_turn[board] = turns   
                flag = 'BINGO'  
             
            elif ''.join(fifth) == 'xxxxx':
                bingo_turn[board] = turns   
                flag = 'BINGO'  

            #check for bingo in vertical rows
            else:
                for index in range(0,5):
                    if vert_row(index) == 'xxxxx': 
                        bingo_turn[board] = turns   
                        flag = 'BINGO'
                        break
            
            #calculate the score when a row is bingo
            if flag == 'BINGO':
                score[board] = 0
                calc_score([first,second,third,fourth,fifth])
                break
               
            turns += 1

        #reset the world for the next board
        first = []
        second = []
        third = []
        fourth = []
        fifth = []
        turns = 0
        flag = 'no'
        continue

    #if line is not '': we have a row of the board => split it and add values to list of current row
    line = line.split(' ')

    for value in line:

        #disregard spaces 
        if value == '':
            continue

        if row == 0:
            first.append(value)
        
        elif row == 1:
            second.append(value)
        
        elif row == 2:
            third.append(value)
        
        elif row == 3:
            fourth.append(value)    

        else:
            fifth.append(value)  

    #signal next row is coming up       
    row += 1

#search for board with quickest bingo and find it's score
best_board = min(bingo_turn, key=bingo_turn.get)
best_score = score[best_board]

print("Board {} has the quickest bingo. It's score is {}." .format(best_board, best_score))

#anwer 2

#search for board with slowest bingo and find it's score
worst_board = max(bingo_turn, key=bingo_turn.get)
worst_score = score[worst_board]

print("Board {} has the slowest bingo. It's score is {}." .format(worst_board, worst_score))