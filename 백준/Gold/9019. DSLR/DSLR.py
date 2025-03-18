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

def D(num):
    return (2*num)%10000

def S(num):
    if num == 0:
        return 9999
    return num-1
def L(num):
    return (num%1000)*10+(num//1000)
def R(num):
    return (num-(num//10)*10)*1000+(num//10)
for _ in range(T):
    A,B = map(int,input().split())
    
    def bfs(start):
        queue = deque()
        visited = [0 for _ in range(10001)]
        queue.append((start,""))
        visited[start] = 1
        
        while queue:
            num,track = queue.popleft()
            if num == B:
                return track

            d = D(num)
            if visited[d] == 0:
                visited[d] = 1
                queue.append((d,track+'D'))
            
            s = S(num)
            if visited[s] == 0:
                visited[s] = 1
                queue.append((s,track+'S'))
            
            l = L(num)
            if visited[l] == 0:
                visited[l] = 1
                queue.append((l,track+'L'))
            
            r = R(num)
            if visited[r] == 0:
                visited[r] = 1
                queue.append((r,track+'R'))
    
    print(bfs(A))