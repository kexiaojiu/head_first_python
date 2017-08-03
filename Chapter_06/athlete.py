#!/usr/bin/env python
#coding=utf-8

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
    
    
class Athlete:
    def __init__(self, name, dob=None, times=[]):
        self.name = name
        self.dob = dob
        self.times = times
        
    def top3(self):
        return(sorted(set([sanitize(t) for t in self.times]))[0:3])
    
    def add_time(self, time):
        self.times.append(time)
        
    def add_times(self, times=[]):
        for time in times:
           self.times.append(time) 


class AthleteList(list):
    def __init__(self, name, dob=None, times=[]):
        list.__init__([])
        self.name = name
        self.dob = dob
        self.extend(times)
        
    def top3(self):
        return(sorted(set([sanitize(t) for t in self]))[0:3])
        
        
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        return (Athlete(templ.pop(0), templ.pop(0), templ))
    except IOError as ioerr:
        print('File error:' + str(ioerr))
        return(None)

james = get_coach_data('james2.txt')
print(james.name + "'s fastest times are: " + str(james.top3()))

A = Athlete('kejie', '19996', ['3.56', '4.58'])
print("\n#####################################")
print(A.times)
A.add_time('3.69')
print(A.times)
A.add_times(['5.36', '9.63'])
print(A.times)

B = AthleteList('kejie', '19996', ['3.56', '4.58'])
print("\n#####################################")
print(B.top3())
B.append('1.36')
print(B.top3())
B.extend(['1.36','9.63'])
print(B.top3())

