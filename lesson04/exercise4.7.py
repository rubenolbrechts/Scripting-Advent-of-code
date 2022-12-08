#!/usr/bin/python3
import random 
import itertools as it

ranks = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
suits = ['hette', 'koeke', 'schoppe', 'kloavere']

#Deck as tuples
deck = []
counter=it.count(start=1, step=1)
count = list(next(counter) for _ in range(2))
'''
for suit in suits:
    for rank in ranks:
        deck.append((suit, rank))
'''
#OR
deck = list(it.product(suits,ranks))



for i in count:
    random.shuffle(deck)
    print('DECK' + str(i) + ":\n" , deck)

print("Counter: {}" .format(count)) 