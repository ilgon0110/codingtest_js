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

newArr = sorted(arr, key=lambda x:(x[0], x[1]))

for x in newArr:
    print(x[0],x[1])