import sys
import collections
import math
from collections import deque
import copy
import bisect
import itertools
import heapq

#sys.stdin = open("input.txt", "r")

#input = sys.stdin.readline

while True:
    sr = str(input())
    stack = list()
    
    if sr == '.':
        break
    
    for char in sr:
        if (char == "(" or char == "["):
            stack.append(char)
        
        if char == ")":
            if (stack and stack[-1] == "("):
                stack.pop()
            else:
                stack.append(char)
                break
        elif char == "]":
            if (stack and stack[-1] == "["):
                stack.pop()
            else:
                stack.append(char)
                break
    
    if stack:
        print('no')
    else:
        print('yes')