#!/usr/bin/env python
#coding=utf-8
import os
from nester_jacob import print_lol

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
    
try:
    man_file = open('man_file.txt', 'w')
    other_file = open('other_file.txt', 'w')
    print_lol(man, fh=man_file)
    print_lol(other, fh=other_file)

    
except FileNotFoundError:
    print('File error!')

finally:
    man_file.close()
    other_file.close()

