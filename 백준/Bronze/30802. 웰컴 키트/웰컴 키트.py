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
#S,M,L,XL,XXL,XXXL = map(int,input().split())
arr = list(map(int,input().split()))
T,P = map(int,input().split())

shirt = 0

for x in arr:
    shirt += math.ceil(x/T)
    
print(shirt)
print(N//P, N%P)
