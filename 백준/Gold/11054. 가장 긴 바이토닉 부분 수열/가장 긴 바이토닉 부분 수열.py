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

dp_max = [0 for _ in range(N)]
dp_min = [0 for _ in range(N)]

for i in range(N):
    max_num = 0
    target = arr[i]
    for j in range(i+1):
        if arr[j] < target:
            max_num = max(max_num,dp_max[j]) 
    dp_max[i] = max_num+1
    
    min_num = 0

for i in range(N-1,-1,-1):
    max_num = 0
    target = arr[i]
    for j in range(N-1,i,-1):
        if arr[j] < target:
            max_num = max(max_num,dp_min[j])
    dp_min[i] = max_num+1

ans = 0
for i in range(N):
    ans = max(ans,dp_max[i]+dp_min[i]-1)

print(ans)