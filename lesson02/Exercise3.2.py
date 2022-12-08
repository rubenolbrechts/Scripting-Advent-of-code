#!/usr/bin/python3


day = int(input("What is your day of birth? "))
month = input("What is your month of birth? ")

birth = []
birth.append(month)
birth.append(day)


print(birth) 

if (birth[0] == "march" and birth[1] >= 21) or (birth[0] == "april" and birth[1] <= 19) :
    print("Your sign is aries") 

# AND so on for every astrological sign
# See leho for better code :)