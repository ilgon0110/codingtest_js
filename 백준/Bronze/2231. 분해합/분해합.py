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

N = int(input())

def genSum(num):
    tmp = num
    arr = list(str(num))
    for x in arr:
        tmp+=int(x)
    return tmp

flag = True
for i in range(1,N):
    if genSum(i) == N:
        print(i)
        flag = False
        break

if flag:
    print(0)
        
    