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

R,C,K = map(int,input().split())
board = []
for _ in range(3):
    board.append(list(map(int,input().split())))

def my_sort(arr):
    my_dict = dict()
    for num in arr:
        if num != 0:
            my_dict[num] = arr.count(num)
    newArr = list(my_dict.items())
    newArr.sort(key=lambda x : (x[1], x[0]))
    result = []
    for x,y in newArr:
        result.append(x)
        result.append(y)
    return result

def R_cal(board):
    newBoard = []

    for i in range(len(board[0])):
        tmp = []
        for j in range(len(board)):
            tmp.append(board[j][i])
        row = my_sort(tmp)
        newBoard.append(row)
    
    maxLen = 0
    for i in range(len(newBoard)):
        maxLen = max(len(newBoard[i]), maxLen)
    
    for i in range(len(newBoard)):
        while len(newBoard[i]) < maxLen:
            newBoard[i].append(0)
    
    N = len(newBoard[0])
    M = len(newBoard)
    
    if N >= 100:
        N = 100
    if M >= 100:
        M = 100
    
    result = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(M):
        for j in range(N):
            result[j][i] = newBoard[i][j]
    return result
    
def C_cal(board):
    newBoard = []
    for i in range(len(board)):
        tmp = my_sort(board[i])
        newBoard.append(tmp)
        
    maxLen = 0
    for i in range(len(newBoard)):
        maxLen = max(maxLen, len(newBoard[i]))
    
    for x in newBoard:
        while len(x) < maxLen:
            x.append(0)
        
        while len(x) > 100:
            x.pop()
    
    return newBoard

def bfs(board):
    global R,C
    queue = deque()
    queue.append((board,0))

    while queue:
        board , time = queue.popleft()
        if time > 100:
            return -1
        if R <= len(board) and C <= len(board[0]) and board[R-1][C-1] == K:
            return time
        if len(board) < len(board[0]):
            r_board = R_cal(board)
            queue.append((r_board,time+1))
        else:
            c_board = C_cal(board)
            queue.append((c_board,time+1))

print(bfs(board))
