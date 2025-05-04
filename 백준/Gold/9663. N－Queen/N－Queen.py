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
board = [[0 for _ in range(N)] for _ in range(N)]
arr = [0]*N

def is_possible(row):
    for i in range(row):
        # 같은 세로줄에 위치
        if arr[row] == arr[i]:
            return False
        # 대각 방향에 위치
        if(abs(row-i) == abs(arr[row]-arr[i])):
            return False
    return True
        
ans = 0
def dfs(row):
    if row == N:
        global ans
        ans +=1
        return
    else:
        for i in range(N):
            arr[row] = i
            if is_possible(row):
                dfs(row+1)

dfs(0)
print(ans)