#!/bin/python3

import math
import os
import random
import re
import sys

def binary_number(n):
    binary_numlist = []
    if n < 2:
        binary_numlist.append(n)
    while n > 1:
        binary_numlist.append(n % 2)
        n = n // 2
    if n == 1 or n == 0:
        binary_numlist.append(n)

    count = 0
    count_list = []
    for i in range(len(binary_numlist)-1):
        if binary_numlist[i] == binary_numlist[i+1]:
            count +=1
        else:
            count_list.append(count)
            count = 0
    count_list.append(count)
    print(max(count_list)+1)
    
if __name__ == '__main__':
    n = int(input().strip())
    binary_number(n)
    
    
