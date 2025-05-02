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

text1 = str(input().rstrip())
text2 = str(input().rstrip())

N = len(text1)
M = len(text2)

dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
ans = 0
for i in range(1,N+1):
    for j in range(1,M+1):
        if text2[j-1] == text1[i-1]:
            dp[i][j] = max(dp[i-1][j-1]+1,dp[i-1][j],dp[i][j-1])
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        ans = max(ans,dp[i][j])

print(ans)
