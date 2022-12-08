#!/usr/bin/python3

charged=["Arg", "Lys"]
negative=["Asp", "Glu"]
charged.extend(negative)
print(charged)

# OR charged.extend(["Asp","Glu"])
