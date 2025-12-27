#!/bin/python3

import math
import os
import random
import re
import sys

def hourclass(arr):
 
    total_sums = []

 
    for i in range(4):
        for j in range(4):

            top_sum = sum(arr[i][j:j+3])

            middle_num = arr[i+1][j+1]

            bottom_sum = sum(arr[i+2][j:j+3])

            hourglass_sum = top_sum + middle_num + bottom_sum

            total_sums.append(hourglass_sum)

    print(max(total_sums))


if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    hourclass(arr)



