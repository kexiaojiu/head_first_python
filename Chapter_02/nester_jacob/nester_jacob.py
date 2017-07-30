#!/usr/bin/env python
#coding=utf-8
from os import sys

"""这是nester.py模块，提供了一个名为print_lol()的函数，该函数可以打印列表"""
# @the_list     列表名
# @indent       是否缩进
# @level        缩进Tab值
# @sys.stdout   数据写入位置标识
def print_lol(the_list, indent=False, level=0, fh=sys.stdout):
    """位置参数the_list是列表，所指定的列表每个数据项会递归地输出到屏幕，各数据占一行"""
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent,level + 1, fh)
        else:
            if indent == True:
                for tab_stop in range(level):
                    print("\t", end='', file=fh)
            print(each_item, file=fh)

if __name__ == "__main__":
    movies = [
            "The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
            ["Graham Chapman",
                ["Michael palin", "John Cheese", "Terry Gilliam"]]]
    print("\n#################################")
    print_lol(movies)
    print("\n#################################")
    print_lol(movies, 2)
    print("\n#################################")
    print_lol(movies, True, 2)
