#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    o=['(','[','{']
    c=[')',']','}'] 
    stack = []
    for i in s:
        if i in o :
            stack.append(i)
        elif i in c :
            if len(stack) == 0 :
                return "NO"
            ch=stack[len(stack)-1]
            ch1=c[o.index(ch)]
            if ch1==i : 
                stack.pop()
            else : 
                return "NO"

    if len(stack) == 0 : return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
