#!/usr/bin/env python
#coding=utf-8
import os

man =[]
other =[]

filename = 'sketch.txt'

try:
    data = open(filename)
except FileNotFoundError:
    print("Sorry, the file doesnot exist.")
else:
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            else:
                other.append(line_spoken)
                
        except ValueError:
            print("The strings are wrong!")
        else:
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')

    data.close()
print(man)
print(other)
