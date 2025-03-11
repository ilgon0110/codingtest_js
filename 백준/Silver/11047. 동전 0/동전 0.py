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
coins = []
ans = 0
for _ in range(N):
    coins.append(int(input()))

for i in range(N-1,-1,-1):
    if K//coins[i] > 0:
        ans += K//coins[i]
        K -= coins[i] * (K//coins[i])
        
print(ans)