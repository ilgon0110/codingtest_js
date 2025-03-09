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

N,M = map(int,input().split())
arr = list(map(int,input().split()))
answer = 0

def combine(L, visited, total):
    if total > M:
        return
    if L == 3:
        global answer
        answer = max(answer,total)
    else:
        for i in range(N):
            if visited[i] == 1:
                continue
            visited[i] = 1
            combine(L+1,visited, total + arr[i])
            visited[i] = 0

combine(0,[0 for _ in range(N)],0)

print(answer)