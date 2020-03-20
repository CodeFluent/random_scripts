# From: https://www.hackerrank.com/challenges/sock-merchant/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    
    hist = {} # histogram of all colors 

    # find the occurences of each color in the list
    for idx, color in enumerate(ar):
        num_of_color = ar.count(color)  
        if (color not in hist):
            hist[color] = num_of_color
    
    print(hist)

    # get the number of pairs
    num_of_pairs = 0
    for color, freq in hist.items():
        if (freq > 1):
            if (freq % 2 == 0):
                num_of_pairs += freq / 2
            else:
                num_of_pairs += (freq - 1) / 2
    
    return int(num_of_pairs)



n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

print("number of pairs", sockMerchant(n, ar))
