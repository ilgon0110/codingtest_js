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

arr = [sys.maxsize for _ in range(5001)]

arr[3] = 1
arr[5] = 1

for i in range(6,N+1,3):
    arr[i] = min(arr[i], arr[i-3]+1)
for j in range(10,N+1,5):
    arr[j] = min(arr[j], arr[j-5]+1)
    
for i in range(5,N+1):
    arr[i] = min(arr[i], arr[i-3]+1,arr[i-5]+1)

if arr[N] == sys.maxsize:
    print(-1)
else:
    print(arr[N])
