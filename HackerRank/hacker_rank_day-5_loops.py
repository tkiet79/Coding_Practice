import math
import os
import random
import re
import sys

def operation(n):
    for i in range(1,11):
        result = n*i
        print(f"{n} x {i} = {result}")
        

if __name__ == '__main__':
    n = int(input().strip())
    operation(n)

