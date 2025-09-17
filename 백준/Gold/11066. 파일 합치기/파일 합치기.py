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

# 다시 풀어보기
T = int(input())
for _ in range(T):
    K = int(input())
    files = list(map(int,input().split()))
    
    dp = [[sys.maxsize for _ in range(K)] for _ in range(K)]
    subtotal = [0 for _ in range(K+1)]
    subtotal[1] = files[0]
    for i in range(1,K):
        subtotal[i+1] = subtotal[i]
        subtotal[i+1] += files[i]

    for i in range(K):
        dp[i][i] = 0
    
    for i in range(2,K+1):
        for j in range(K-i+1):
            for k in range(j,j+i-1):
                #print(i,j,k)
                dp[j][j+i-1] = min(dp[j][j+i-1], dp[j][k]+dp[k+1][j+i-1]+subtotal[j+i]-subtotal[j])

    print(dp[0][K-1])