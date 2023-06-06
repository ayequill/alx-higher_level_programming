#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
print(str.split(',')[2].split(' ')[1]+' '+str.split(',')[2].split(' ')
      [2] + ' ' + str.split(',')[2].split(' ')[-4] + ' ' + str[:6])
