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

H,W,N,M = map(int,input().split())

row=0
col=0

for i in range(0,W,M+1):
    row+=1

for i in range(0,H,N+1):
    col+=1

print(row*col)
