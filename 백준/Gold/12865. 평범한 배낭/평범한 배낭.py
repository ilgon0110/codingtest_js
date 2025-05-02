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

N,K = map(int,input().split())
items = []
for _ in range(N):
    W,V = map(int,input().split())
    items.append((W,V))

dp = [0 for _ in range(K+1)]
items.sort(key=lambda x : -x[0])

for W,V in items:
    for i in range(K,W-1,-1):
        dp[i] = max(dp[i-W]+V,dp[i])

print(max(dp))