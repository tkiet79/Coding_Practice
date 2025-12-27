#!/bin/python3

import math
import os
import random
import re
import sys


def most_common_characters(s):
    word_counts = {}
    for word in s:
        word_counts[word] = word_counts.get(word, 0) + 1
    
    sorted_list = sorted(word_counts.items(), key=lambda item:(-item[1], item[0]))
    for i in range(3):
        print(*sorted_list[i])
    
    


if __name__ == '__main__':
    s = input()
    most_common_characters(s)
