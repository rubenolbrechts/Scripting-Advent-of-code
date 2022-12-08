#!/usr/bin/python3

#3.4.a

Countries_AND_province = {"Belgium" : "Brussels", "UK" : "London", "France" : "Paris", "Catalonië" : "Barcelona"}

#print(Countries_and_province)

print("List of capitals:\n====================")
for country, capital in Countries_AND_province.items() :
    print(capital)

#3.4.b

counter = 1
rows = 0
rows2 = 3
while counter <= 4 :
    while rows < counter:
        rows = rows +1
        if rows <= 5:
            print("* ", end="")
    rows = 0
    counter = counter+1 
    print("")

counter2 = 7
while counter <= 9:
    rows3 =  counter - rows2
    while rows3 < counter2:
        rows3 = rows3 +1
        print("* ", end="")
    counter = counter+1 
    print("")

#see leho for better example!!!
