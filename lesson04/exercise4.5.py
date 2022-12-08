#!/usr/bin/python3
import datetime

print("Current date : {}" .format(datetime.datetime.now().strftime("%Y-%m-%d")))

next1 =  (datetime.datetime.now() + datetime.timedelta(days=7)).strftime("%Y-%m-%d")

print("Date next week : {}" .format(next1))

before = (datetime.datetime.now() + datetime.timedelta(days=-5)).strftime("%Y-%m-%d")

print("Five days before : {}" .format(before))