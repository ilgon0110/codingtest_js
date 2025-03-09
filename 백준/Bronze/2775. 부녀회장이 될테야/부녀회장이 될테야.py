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
    k = int(input())
    n = int(input())
    
    board = [[i for i in range(15)] for _ in range(15)]
    
    for i in range(1,15):
        for j in range(1,15):
            board[j][i] = board[j][i-1] + board[j-1][i]
    
    print(board[k][n])
    
    #print(board)