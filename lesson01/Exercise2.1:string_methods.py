#!/usr/bin/python3
#2.1.1
'''
IN=input('Give me a sentence: ')
IN=IN.upper()
print(IN)
IN=IN.lower()
print(IN)
'''

''' PACO WAY
str_in = input('Give me a sentence: ')
print("In uppercase: {}\n" 
    "In lowercase {}"
    .format(str_in.upper(), str_in.lower()))
'''

#2.1.2

'''
seq=input('Give me a sequence: ')
mot=input('Give me a motif: ')
print(seq.find(mot)+1)
'''

'''Paco way
Was pretty similar
'''

#2.1.3

seq=input('Give me a sequence: ')
cleave=input('Give me a cleavage site: ')
split=seq.split(cleave)
print('Sequence fragments:{}' .format(split))
