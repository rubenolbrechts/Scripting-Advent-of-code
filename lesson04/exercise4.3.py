#!/usr/bin/python3

input1 = input("Give me a DNA sequence bro: ")

def freq(seq):
    bases = {"A" : 0, "T" : 0, "G" : 0, "C" : 0}
    c = 0
    for nt in seq:
        '''
        if nt == "A":
            bases["A"] +=1
        elif nt == "T":
            bases["T"] +=1
        elif nt == "G":
            bases["G"] +=1
        elif nt == "C":
            bases["C"] +=1
        '''
        bases[nt]+=1
        c = c + 1
    freqs = {}
    for nt, amount in bases.items() :
        freqs[nt] = freqs.get(nt,round(amount/c,2)*100) 

    print("Calculate base counts\n", bases)
    print("Calculate base frequencies\n", freqs)

freq(input1)
