#!/usr/bin/python3

#3.3.a
fib = [0]
counter = 0
a = 0
b = 1
c =  1
while c < 50:

    
    fib.append(c)
    a = c
    c = a + b
    print("({}+{} = {})".format(a,b,c))
    b = a
    counter = counter + 1   

print(fib)

#3.3.b
import random

num = random.randint(1, 9)
guess = int(input("Guess the random number: "))

while guess != num :
    print("Try again!")
    guess = int(input("Guess the random number: "))
if guess == num :
    print("Congrats!") 