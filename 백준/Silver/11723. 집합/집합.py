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

my_set = set()

M = int(input())

for _ in range(M):
    tmp = str(input()).rstrip()
    command = ""
    number = 0
    if 'all' in tmp or 'empty' in tmp:
        command = tmp
    else:
        x,y = map(str, tmp.split())
        command = x
        number = int(y)
        
    if command == "add":
        my_set.add(number)
    
    if command == "remove":
        if number in my_set:
            my_set.remove(number)
    
    if command == "check":
        if number in my_set:
            print(1)
        else:
            print(0)
    
    if command == "toggle":
        if number in my_set:
            my_set.remove(number)
        else:
            my_set.add(number)
    
    if command == "all":
        my_set = set([i for i in range(1,21)])
    
    if command == "empty":
        my_set = set()