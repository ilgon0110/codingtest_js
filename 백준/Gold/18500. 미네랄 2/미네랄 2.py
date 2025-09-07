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
for _ in range(R):
    board.append(list(input().rstrip()))
    
N = int(input())
heights = list(map(int,input().split()))

dx = [-1,0,1,0]
dy = [0,-1,0,1]

for _ in range(N):
    height = heights[_]
    # 해당 칸 미네랄 파괴
    if _%2 == 0:
        for j in range(C):
            if board[R-height][j] == 'x':
                board[R-height][j] = '.'
                break
    else:
        for j in range(C-1,-1,-1):
            if board[R-height][j] == 'x':
                board[R-height][j] = '.'
                break
    
    # 파괴된 후 클러스터 계산
    newBoard = [[0 for _ in range(C)] for _ in range(R)]
    visited = [[0 for _ in range(C)] for _ in range(R)]
    index = 0
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'x' and visited[i][j] == 0:
                index+=1
                queue = deque()
                queue.append((i,j))
                visited[i][j] == 1
                newBoard[i][j] = index
                
                while queue:
                    x,y = queue.popleft()
                    for k in range(4):
                        nx = x+dx[k]
                        ny = y+dy[k]
                        if nx<0 or nx>=R or ny<0 or ny>=C or visited[nx][ny]:
                            continue
                        if board[nx][ny] == 'x':
                            visited[nx][ny] = 1
                            newBoard[nx][ny] = index
                            queue.append((nx,ny))

    # 중력으로 내려갈 수 있을 만큼 내려가기
    for idx in range(1,index+1):
        blocks = []
        for j in range(R):
            for k in range(C):
                if newBoard[j][k] == idx:
                    blocks.append((j,k))
        
        Flag = True
        cnt = 1
        while Flag:
            isCanDown = True
            for x,y in blocks:
                nx = x+cnt
                ny = y
                if nx<R and (newBoard[nx][ny] == idx or newBoard[nx][ny] == 0):
                    continue
                else:
                    Flag = False
                    isCanDown = False
                    break
            if isCanDown == False:
                break
            cnt +=1
        
        for i in range(R):
            for j in range(C):
                if newBoard[i][j] == idx:
                    newBoard[i][j] = 0
        
        for x,y in blocks:
            newBoard[x+cnt-1][y] = idx

    # newBoard를 board에 반영
    for i in range(R):
        for j in range(C):
            if newBoard[i][j] > 0:
                board[i][j] = 'x'
            elif newBoard[i][j] == 0:
                board[i][j] = '.'
    if _ == N-1:
        ans = [['.' for _ in range(C)] for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if newBoard[i][j] != 0:
                    ans[i][j] = 'x'
            
        for x in ans:
            print(''.join(x))
            