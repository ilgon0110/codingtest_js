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

K,N = map(int,input().split())
arr = []

for _ in range(K):
    arr.append(int(input()))

lt = 1
rt = max(arr)
ans = 0

def cutting(num):
    total = 0
    for x in arr:
        total += x//num
    return total

while lt <= rt:
    mid = (lt+rt)//2

    if(cutting(mid) >= N):
        ans = mid
        lt = mid+1
    else:
        rt = mid-1
        
print(ans)

