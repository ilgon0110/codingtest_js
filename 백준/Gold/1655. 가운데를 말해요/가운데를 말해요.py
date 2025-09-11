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
min_queue = []
max_queue = []

mid = sys.maxsize

for _ in range(N):
    char = int(input())
    
    if char <= mid:
        heapq.heappush(max_queue, -char)
    else:
        heapq.heappush(min_queue, char)
    
    if len(max_queue) > len(min_queue)+1:
        left = heapq.heappop(max_queue)
        heapq.heappush(min_queue, -left)
    elif len(max_queue) < len(min_queue):
        right = heapq.heappop(min_queue)
        heapq.heappush(max_queue, -right)
    
    #print(max_queue)
    #print(min_queue)
    
    print(-max_queue[0])
    mid = -max_queue[0]