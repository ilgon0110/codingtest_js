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
A = [0]+list(map(int,input().split()))
C = [0]+list(map(int,input().split()))

#dp[i][j] = i번째 어플까지 확인했을 때 j cost에서 얻을 수 있는 최대 메모리
dp = [[0 for _ in range(sum(C)+1)] for _ in range(N+1)]
result = sys.maxsize

for i in range(1,N+1):
    byte = A[i]
    cost = C[i]
    
    for j in range(sum(C)+1):
        if j < cost:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-cost]+byte, dp[i-1][j])
        
        if dp[i][j] >= M:
            result = min(result,j)

print(result)