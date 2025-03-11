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

M,N = map(int,input().split())

def isPrime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    for i in range(2, math.ceil(math.sqrt(num))+1):
        if num%i == 0:
            return False
    
    return True

for i in range(M,N+1):
    if isPrime(i):
        print(i)