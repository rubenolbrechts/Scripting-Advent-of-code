#!/usr/bin/python3
import re
pswd =input("Give me a valid password pls: ")

while True:
    if re.search("[A-Z]", pswd) and re.search("[a-z]", pswd) and re.search("[$,#,@]", pswd) and re.search("[\d]", pswd) and 6<len(pswd)<16:
        exit("Valid password")

    else :
        print("Not a valid password")
        pswd =input("Give me a valid password pls: ")


'''
Validation :
 At least 1 letter between [a-z] and 1 letter between [A-Z].
 At least 1 number between [0-9].
 At least 1 character from [$#@].
 Minimum length 6 characters.
 Maximum length 16 characters.
Tip: use the re (regular expressions) module in combination with while and if 
'''