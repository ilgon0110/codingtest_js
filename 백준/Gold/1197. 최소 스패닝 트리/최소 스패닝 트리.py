import sys
import collections
import math
from collections import deque
import copy
import bisect
import itertools
import heapq

#sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

V,E = map(int,input().split())
trees = []

for _ in range(E):
    a,b,c = map(int,input().split())
    trees.append((c,a,b))
trees.sort()

parent = [i for i in range(V+1)]

def find(node):
    if parent[node] == node:
        return node
    else:
        parent[node] = find(parent[node])
        return parent[node]

def union(x,y):
    root1, root2 = find(x), find(y)
    if root1 == root2:
        return False
    else:
        parent[root2] = root1
        return True

ans = 0
for x in trees:
    cost,a,b = x
    if union(a,b):
        ans += cost

print(ans)