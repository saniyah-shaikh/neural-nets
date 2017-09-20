# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 16:01:17 2017

@author: Saniyah
"""

# file to create multiplaction training file for neural net
    
def write_mult_testdata(filename, x, y):
    file = open(filename,'w')
    for x_num in range(1, x + 1):
        for y_num in range(y):
            s = str(x_num) + ' ' + str(y_num) + ' ' + str(x_num * y_num) + '\n'
            file.write(s)
            
def write_add_testdata(filename, x, y):
    file = open(filename,'w')
    for x_num in range(1, x + 1):
        for y_num in range(y):
            s = str(x_num) + ' ' + str(y_num) + ' ' + str(x_num + y_num) + '\n'
            file.write(s)
            
def write_sub_testdata(filename, x, y):
    file = open(filename,'w')
    for x_num in range(1, x + 1):
        for y_num in range(y):
            s = str(x_num) + ' ' + str(y_num) + ' ' + str(x_num - y_num) + '\n'
            file.write(s)
            
write_sub_testdata("testdata-sub-5-10.txt", 5, 10)