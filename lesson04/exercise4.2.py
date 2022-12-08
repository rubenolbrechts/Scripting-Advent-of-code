#!/usr/bin/python3

input1 = input("Give me a string to seperate bro: ")
sep = input("Give me a character to seperate the string bro: ")

def seperator(string,seper):
    txt=string.split(seper)
    txt.sort()
    print(seper.join(txt))

seperator(input1, sep)

#see leho 