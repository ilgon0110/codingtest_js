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

R,C = map(int,input().split())
board = []
visited = [[0 for _ in range(C)] for _ in range(R)]
for _ in range(R):
    board.append(list(str(input().rstrip())))
dx = [-1,0,1,0]
dy = [0,-1,0,1]
ans = 0
visited = [0 for _ in range(100)]

def dfs(x,y,total):
    global ans,visited
    ans = max(total,ans)
    for k in range(4):
        nx = x+dx[k]
        ny = y+dy[k]
        if nx<0 or nx >= R or ny<0 or ny>=C:
            continue
        target = ord(board[nx][ny])
        if visited[target] == 0:
            visited[target] = 1
            dfs(nx,ny,total+1)
            visited[target] = 0
visited[ord(board[0][0])] = 1
dfs(0,0,1)
print(ans)