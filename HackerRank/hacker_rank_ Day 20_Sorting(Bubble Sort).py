#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    is_sorted = False
    count = 0

    while not is_sorted:
        is_sorted = True 
        i = 1
        while i < n:
            if a[i-1] > a[i]:
                count += 1
                a[i-1],a[i] = a[i],a[i-1]
                is_sorted = False
            i +=1

    print(f"Array is sorted in {count} swaps.")    
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")
            
    




    
