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
arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))

arr.sort(key=lambda x : (x[1],x[0]))

for x in arr:
    print(x[0],x[1])