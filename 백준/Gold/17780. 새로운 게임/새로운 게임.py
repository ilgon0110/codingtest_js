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
board = []
dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]
soliders = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(N):
    board.append(list(map(int,input().split())))
    
for i in range(K):
    x,y,d = map(int,input().split())
    soliders[x-1][y-1].append([i+1,d])

cnt = 0
 
def blueOrOut(x,y,direction):
    #print('blueOrOut')
    nDirection = 0
    if direction == 1:
        nDirection = 2
    elif direction == 2:
        nDirection = 1
    elif direction == 3:
        nDirection = 4
    elif direction == 4:
        nDirection = 3
    nx = x+dx[nDirection]
    ny = y+dy[nDirection]
    
    soliders[x][y][0][1] = nDirection
    # 방향 전환 후 가려는 방향이 보드 밖이면
    if nx<0 or nx>=N or ny<0 or ny>=N:
        return
    # 방향 전환 후 가려는 방향이 파란색이면
    if board[nx][ny] == 2:
        return
    elif board[nx][ny] == 1:
        # 말들을 모두 이동
        tmp = []
        for solider in soliders[x][y]:
            tmp.append(solider)
        tmp.reverse()
        for solider in tmp:
            soliders[nx][ny].append(solider)
        # 이동되면 기존 위치 말들 초기화
        soliders[x][y] = []
    else:
        for solider in soliders[x][y]:
            soliders[nx][ny].append(solider)
        soliders[x][y] = []
        

def red(x,y,direction):
    nx = x+dx[direction]
    ny = y+dy[direction]
    
    tmp = []
    for solider in soliders[x][y]:
        tmp.append(solider)
    tmp.reverse()
    
    # 말들 이동
    for solider in tmp:
        soliders[nx][ny].append(solider)
    
    # 이동 후 기존 위치 초기화
    soliders[x][y] = []

def white(x,y,direction):
    nx = x+dx[direction]
    ny = y+dy[direction]

    for solider in soliders[x][y]:
        soliders[nx][ny].append(solider)
    
    soliders[x][y] = []

flag = False
while cnt < 1001:
    cnt+=1
    if flag:
        break
    for turn in range(1,K+1):
        check = False
        if flag:
            break
        for i in range(N):
            if flag:
                break
            for j in range(N):
                if len(soliders[i][j]) >= 4:
                        flag = True
                        break
                    
                if len(soliders[i][j]) > 0 and check == False:
                    
                    # 가장 아래 있는 말
                    num,direction = soliders[i][j][0]
                    if num == turn:
                        nx = i+dx[direction]
                        ny = j+dy[direction]
                        
                        # 벗어나거나 파란색인 경우
                        if nx<0 or nx>=N or ny<0 or ny>=N:
                            #print('out')
                            blueOrOut(i,j,direction)
                            check = True
                        
                        elif board[nx][ny] == 2:
                            #print('blue')
                            blueOrOut(i,j,direction)
                            check = True
                        
                        # 빨간색인 경우
                        elif board[nx][ny] == 1:
                            #print('red')
                            red(i,j,direction)
                            check = True
                        
                        # 흰색인 경우
                        elif board[nx][ny] == 0:
                            #print('white')
                            white(i,j,direction)
                            check = True
                            
    for i in range(N):
        for j in range(N):
            if len(soliders[i][j]) >= 4:
                flag = True
                break
    
    if flag:
        break

if flag:
    print(cnt)
else:
    print(-1)



