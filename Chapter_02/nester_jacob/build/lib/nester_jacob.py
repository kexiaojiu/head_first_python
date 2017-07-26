#!/usr/bin/env python
#coding=utf-8

"""这是nester.py模块，提供了一个名为print_lol()的函数，该函数可以打印列表"""
def print_lol(the_list):
    """位置参数the_list是列表，所指定的列表每个数据项会递归地输出到屏幕，各数据占一行"""
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)

if __name__ == "__main__":
    movies = [
            "The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
            ["Graham Chapman",
                ["Michael palin", "John Cheese", "Terry Gilliam"]]]
    print_lol(movies)
