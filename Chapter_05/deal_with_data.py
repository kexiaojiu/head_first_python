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
"""处理数据的示例"""

file_james = 'james.txt'
file_julie = 'julie.txt'
file_mikey = 'mikey.txt'
file_sarah = 'sarah.txt'

def sanitize(time_string):
    """处理时间格式，统一为min.sec"""
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (min, secs) = time_string.split(splitter)
    return(min + '.' + secs)
    
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
            return (data.strip().split(','))
    except IOError as ioerr:
        print('File error:' + str(ioerr))
        return(None)
        
james = get_coach_data(file_james)
julie = get_coach_data(file_julie)
mikey = get_coach_data(file_mikey)
sarah = get_coach_data(file_sarah)
    
#~ # 读入数据
#~ with open(file_james) as f1, open(file_julie) as f2, open(file_mikey) as f3, open(file_sarah) as f4:
    #~ data1 = f1.readline()
    #~ james = data1.strip().split(',')
    #~ data2 = f2.readline()
    #~ julie = data2.strip().split(',')
    #~ data3 = f3.readline()
    #~ mikey = data3.strip().split(',')
    #~ data4 = f4.readline()
    #~ sarah = data4.strip().split(',')
# end 读入数据

print("james: " + str(james))
print("julie: " + str(julie))
print("mikey: " + str(mikey))
print("sarah: " + str(sarah))

#~ clean_james = []
#~ clean_julie = []
#~ clean_mikey = []
#~ clean_sarah = []

#~ for time1 in james:
    #~ clean_james.append(sanitize(time1))
#~ for time2 in julie:
    #~ clean_julie.append(sanitize(time2))
#~ for time3 in mikey:
    #~ clean_mikey.append(sanitize(time3))
#~ for time4 in sarah:
    #~ clean_sarah.append(sanitize(time4)) 
clean_james = [sanitize(time1) for time1 in james]
clean_julie = [sanitize(time2) for time2 in julie]
clean_mikey = [sanitize(time3) for time3 in mikey]
clean_sarah = [sanitize(time4) for time4 in sarah]

print("\n############clean time####################")    
print("james: " + str(clean_james))
print("julie: " + str(clean_julie))
print("mikey: " + str(clean_mikey))
print("sarah: " + str(clean_sarah))
       
print("\n############sort####################")
print("james: " + str(sorted(clean_james)))
print("julie: " + str(sorted(clean_julie)))
print("mikey: " + str(sorted(clean_mikey)))
print("sarah: " + str(sorted(clean_sarah)))

#~ unique_james = []
#~ unique_julie = []
#~ unique_mikey = []
#~ unique_sarah = []

#~ sorted_james = sorted(clean_james)
#~ sorted_julie = sorted(clean_julie)
#~ sorted_mikey = sorted(clean_mikey)
#~ sorted_sarah = sorted(clean_sarah)
#~ for each_t in sorted_james:
    #~ if each_t not in unique_james:
        #~ unique_james.append(each_t)
#~ for each_t in sorted_julie:
    #~ if each_t not in unique_julie:
        #~ unique_julie.append(each_t)
#~ for each_t in sorted_mikey:
    #~ if each_t not in unique_mikey:
        #~ unique_mikey.append(each_t)
#~ for each_t in sorted_sarah:
    #~ if each_t not in unique_sarah:
        #~ unique_sarah.append(each_t)
        
#~ print("\n############sTop 3####################")
#~ print("james: " + str(unique_james[0:3]))
#~ print("julie: " + str(unique_julie[0:3]))
#~ print("mikey: " + str(unique_mikey[0:3]))
#~ print("sarah: " + str(unique_sarah[0:3]))


print("\n############sTop 3####################")
print('james: ' + str(sorted(set(clean_james))[0:3]))
print("julie: " + str(sorted(set([sanitize(t) for t in julie]))[0:3]))
print("mikey: " + str(sorted(set([sanitize(t) for t in mikey]))[0:3]))
print("sarah: " + str(sorted(set([sanitize(t) for t in sarah]))[0:3]))
