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
arr = list(map(int,input().split()))

arr.sort()
waiting = 0
time = 0

for cost in arr:
    waiting += cost
    time += waiting

print(time)
