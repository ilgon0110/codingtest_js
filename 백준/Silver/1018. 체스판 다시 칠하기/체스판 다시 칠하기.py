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
for _ in range(N):
    board.append(list(input().rstrip()))
startW = ['W','B','W','B','W','B','W','B']
startB = ['B','W','B','W','B','W','B','W']

def findOtherBoard(x,y):
    paintW = 0
    paintB = 0
    if x+8 > N or y+8 > M:
        return 999999
    startNode = board[x][y]
    
    for i in range(x,x+8):
            for j in range(y,y+8):
                if (i-x)%2 == 0:
                    if board[i][j] != startW[j-y]:
                        paintW+=1
                else:
                    if board[i][j] != startB[j-y]:
                        paintW+=1
                        
    for i in range(x,x+8):
            for j in range(y,y+8):
                if (i-x)%2 == 0:
                    if board[i][j] != startB[j-y]:
                        paintB+=1
                else:
                    if board[i][j] != startW[j-y]:
                        paintB+=1

    return min(paintW,paintB)

ans = 99999999

for i in range(N):
    for j in range(M):
        ans = min(ans, findOtherBoard(i,j))

print(ans)
