#!/usr/bin/env python
#coding=utf-8
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
"""使用pickle示例"""

import os
import pickle
from nester_jacob import print_lol

man = []
other = []
new_man = []

filename = 'sketch.txt'
filename1 = 'man_data.txt'
filename2 = 'other_data'

try:
    with open(filename) as data:
        for each_line in data:
            try:
                (role, line_spoken) = each_line.split(':', 1)
                line_spoken = line_spoken.strip()
                if role == 'Man':
                    man.append(line_spoken)
                else:
                    other.append(line_spoken)
                    
            except ValueError:
                pass
                #~ print("The strings are wrong!")
except FileNotFoundError:
    print("Sorry, the file doesnot exist.")


try:
    #~ with open(filename1, 'w') as man_file, open(filename2, 'w') as other_file:
        #~ print_lol(man)
        #~ print_lol(other)
    with open(filename1, 'wb') as man_file, open(filename2, 'wb') as other_file:  
        pickle.dump(man, man_file)
        pickle.dump(other, other_file)  
except IOError as error:
    print('File Error:' + str(error))
except pickle.PickleError as perr:
    print('Pickling error: ' + str(perr))

try:
    with open(filename1, 'rb') as man_file:
        new_man = pickle.load(man_file)
except IOError as error:
    print('File Error:' + str(error))
except pickle.PickleError as perr:
    print('Pickling error: ' + str(perr))
    
print_lol(new_man)
