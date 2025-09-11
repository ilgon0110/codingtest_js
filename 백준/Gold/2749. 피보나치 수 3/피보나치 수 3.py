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

n = int(input())
N = 2
arr = [[0,1],[1,1]]

def multiple(arr1,arr2):
    newArr = [[0 for _ in range(N)] for _ in range(N)]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                newArr[k][i] += arr1[k][j]*arr2[j][i]
            newArr[k][i] = newArr[k][i] % 1000000
    
    return newArr

def divide(arr,B):
    if B == 2:
        return multiple(arr,arr)
    elif B == 1:
        return arr
    elif B%2 == 1:
        return multiple(divide(multiple(arr,arr), B//2),arr)
    elif B%2 == 0:
        return divide(multiple(arr,arr), B//2)

result = divide(arr,n)
print(result[0][1])