import sys
import collections
import math
from collections import deque
import copy
import bisect
import itertools
import heapq

#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

stack = []
text = list(input().rstrip())
bomb = list(input().rstrip())

def isBomb():
    flag = True
    for i in range(len(bomb)):
        if stack[len(stack)-len(bomb)+i] != bomb[i]:
            flag = False
    return flag

for char in text:
    stack.append(char)
    
    if len(stack) >= len(bomb):
        bombCheck = isBomb()
        if bombCheck:
            for i in range(len(bomb)):
                stack.pop()

if len(stack):
    print("".join(stack))
else:
    print('FRULA')