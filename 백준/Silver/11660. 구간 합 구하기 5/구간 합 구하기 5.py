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
board = []
dp = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(N):
    board.append(list(map(int,input().split())))

for i in range(N):
    dp[i][0] = board[i][0]
    for j in range(1,N):
        dp[i][j] = board[i][j] + dp[i][j-1]
        
for _ in range(M):
    a,b,c,d = map(int,input().split())
    x1 = a-1
    y1 = b-1
    x2 = c-1
    y2 = d-1
    total = 0
    
    for i in range(x1,x2+1):
        if y1 >= 1:
            total += dp[i][y2] - dp[i][y1-1]
        else:
            total += dp[i][y2]
            
    print(total)
    
    