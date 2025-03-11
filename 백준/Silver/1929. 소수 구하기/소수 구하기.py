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

M,N = map(int,input().split())

arr = [i for i in range(2,N+1)]
visited = [0 for i in range(2,N+1)]
ans = []
before = 0

L = len(arr)

while True:
    tmp = -1
    for i in range(before, L):
        if visited[i] != 1:
            tmp = arr[i]
            ans.append(arr[i])
            visited[i] = 1
            break
            
    if tmp == -1:
        break
    idx = tmp - 2
    for i in range(idx+tmp,L,tmp):
        visited[i] = 1
    before = idx
    #print(arr)
    #print(visited)
    #print(ans)

for x in ans:
    if x >= M:
        print(x)

