import sys
import collections
import math
from collections import deque
import copy
import bisect
import itertools
import heapq

#sys.stdin = open("input.txt", "r")

N,M = map(int,input().split())
trees = list(map(int,input().split()))

lt = 0
rt = max(trees)
ans = 0

def cutting(num):
    total = 0
    for tree in trees:
        if tree > num:
            total += tree-num
    return total

while lt<=rt:
    mid = (lt+rt)//2
    if cutting(mid) >= M:
        lt = mid+1
        ans = mid
    else:
        rt = mid-1

print(ans)