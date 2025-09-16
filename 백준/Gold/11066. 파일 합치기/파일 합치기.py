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

T = int(input())

for _ in range(T):
    K = int(input())
    files = list(map(int,input().split()))
    subtotal = [0 for _ in range(K+1)]
    
    for i in range(1,K+1):
        subtotal[i] = files[i-1]
        subtotal[i] += subtotal[i-1]
    
    # dp[i][j] = i에서 j까지 합친 최소값 저장
    dp = [[sys.maxsize for _ in range(K)] for _ in range(K)]
    
    for i in range(K):
        dp[i][i] = 0
    
    for i in range(2,K+1): #길이
        for j in range(K-i+1): #시작 인덱스
            for k in range(j,j+i-1): #하나하나씩
                dp[j][j+i-1] = min(dp[j][j+i-1], dp[j][k]+dp[k+1][j+i-1]+subtotal[j+i]-subtotal[j])
    
    print(dp[0][K-1])