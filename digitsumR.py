#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#
def call(s,i,sum):
    if i==len(s):
        return sum
    sum=sum+int(s[i])
    return call(s,i+1,sum)

def superDigit(n,k):
    s=str(n)*k
    while(len(str(s))!=1):
        s=str(call(s,0,0))
    return s

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n,k)

    print(str(result) )
