#!/usr/bin/python3
import math 

sidea = float(input('give me side 1: '))
sideb = float(input('give me side 2: '))
sidec = float(input('give me side 3: '))

semi = ((sidea + sideb + sidec)/ 2)
#print(semi)

area = (math.sqrt(semi*(semi-sidea)*(semi-sideb)*(semi-sidec)))
print("The area of the triangle is {}" .format(area))

#FOR ALTERNATIVE WITHOUT MATH SEE RECORDING!!!!!!