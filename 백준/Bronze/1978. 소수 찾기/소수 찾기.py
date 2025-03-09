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
cnt = 0
N = int(input())
arr = list(map(int,input().split()))

def isPrime(number):
    if number < 2:
        return False
    for i in range(2,math.floor(math.ceil(number))):
        if number % i == 0:
            return False
    
    return True

for x in arr:
    if isPrime(x):
        cnt+=1

print(cnt)