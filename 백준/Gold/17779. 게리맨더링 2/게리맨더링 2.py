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
board = []

for _ in range(N):
    board.append(list(map(int,input().split())))

def divide(x,y,d1,d2, visited):
    visited[x][y] = 5
    result = [(x,y)]
    #1번
    nx = 0
    ny = y
    for i in range(x,x+d1+1):
        if i < 0 or i >= N or ny < 0 or ny >= N:
            continue
        visited[i][ny] = 5
        ny-=1
        nx = i
    result.append((nx,ny+1))
    
    #3번
    nx = 0
    ny = y-d1
    for i in range(x+d1,x+d1+d2+1):
        if i < 0 or i >= N or ny < 0 or ny >= N:
            continue
        visited[i][ny] = 5
        ny+=1
        nx = i
    result.append((nx,ny-1))
    
    #2번
    nx = 0
    ny = y
    for i in range(x,x+d2+1):
        if i < 0 or i >= N or ny < 0 or ny >= N:
            continue
        visited[i][ny] = 5
        ny+=1
        nx = i
    result.append((nx,ny-1))

    #4번
    nx = 0
    ny = y+d2
    for i in range(x+d2,x+d2+d1+1):
        if i < 0 or i >= N or ny < 0 or ny >= N:
            continue
        visited[i][ny] = 5
        ny -= 1
        nx = i
        
    for i in range(N):
        tmp1 = -1
        tmp2 = -1
        flag = False
        for j in range(N):
            if visited[i][j] == 5:
                tmp1 = j
                break
        for j in range(N-1,-1,-1):
            if visited[i][j] == 5:
                tmp2 = j
                flag = True
                break
        if flag:
            for j in range(tmp1,tmp2+1):
                visited[i][j] = 5
            
    return (visited, result)


def select(visited,corner):
    one,two,three,four = corner

    for i in range(0,two[0]):
        for j in range(0,one[1]+1):
            if visited[i][j] == 5:
                break
            visited[i][j] = 1
    
    for i in range(0,four[0]+1):
        for j in range(one[1]+1,N):
            if visited[i][j] == 5:
                continue
            visited[i][j] = 2
    
    for i in range(two[0],N):
        for j in range(0,three[1]):
            if visited[i][j] == 5:
                break
            visited[i][j] = 3
    for i in range(four[0]+1,N):
        for j in range(three[1],N):
            if visited[i][j] == 5:
                continue
            visited[i][j] = 4
    return visited

ans = sys.maxsize
for d1 in range(N):
    for d2 in range(N):
        for x in range(N):
            for y in range(N):
                if d1 >= 1 and d2 >= 1 and 0 <= x and x+d1+d2 < N and 0 <= y-d1 and y-d1 < y and y < y+d2 and y+d2 < N:
                    visited , corner = divide(x,y,d1,d2,[[0 for _ in range(N)] for _ in range(N)])
                    d_board = select(visited,corner)
                    tmp = [0,0,0,0,0]
                    for i in range(N):
                        for j in range(N):
                            target = d_board[i][j]
                            tmp[target-1] += board[i][j]
                    
                    minT = min(tmp)
                    maxT = max(tmp)
                    ans = min(maxT-minT,ans)

print(ans)