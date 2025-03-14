import sys
import collections
import math
from collections import deque
import copy
import bisect
import itertools
import heapq

#sys.stdin = open("input.txt", "r")

text = str(input()).rstrip()

calc = []

for char in text:
    if char == '+' or char == '-':
        calc.append(char)

tmp = text.replace('+',',')
tmp2 = tmp.replace('-',',')
arr = tmp2.split(',')
numbers = []
arr2 = []
for char in arr:
    numbers.append(int(char))
N = len(calc)
for i in range(N):
    arr2.append(numbers[i])
    arr2.append(calc[i])
arr2.append(numbers[-1])

M = len(arr2)
ans = sys.maxsize

i = 0
while i < len(arr2):
    if arr2[i] == '+':
        tmp2 = arr2[i-1]+arr2[i+1]
        del arr2[i-1]
        del arr2[i-1]
        del arr2[i-1]
        arr2.insert(i-1,tmp2)
    else:
        i+=1
    
ans = arr2[0]

for i in range(2,len(arr2),2):
    ans -= arr2[i]

print(ans)
                
