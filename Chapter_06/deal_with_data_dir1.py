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
    
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        return ({'Name':templ.pop(0),
                'DOB':templ.pop(0),
                'Times':str(sorted(set([sanitize(t) for t in templ]))[0:3])
                })
    except IOError as ioerr:
        print('File error:' + str(ioerr))
        return(None)

sarah_data = get_coach_data('sarah2.txt')

print(sarah_data['Name'] + "'s fastest times are: " + sarah_data['Times'])
