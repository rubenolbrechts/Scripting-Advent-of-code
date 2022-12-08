#!/usr/bin/python3

import datetime 
import locale
#mydate = datetime.datetime.now().strftime("%B")
print("Month of the year: {}" .format(datetime.datetime.now().strftime("%B")))

print("Week number of year: {}" .format(datetime.datetime.now().strftime("%U")))

print("Day of year: {}" .format(datetime.datetime.now().strftime("%j")))

print("Day of month: {}" .format(datetime.datetime.now().strftime("%d")))

print("Day of week: {}" .format(datetime.datetime.now().strftime("%A")))

locale.setlocale(locale.LC_ALL, 'nl_NL.utf-8')

print("Maand van het jaar: {}" .format(datetime.datetime.now().strftime("%B")))

print("Dag van de week: {}" .format(datetime.datetime.now().strftime("%A")))