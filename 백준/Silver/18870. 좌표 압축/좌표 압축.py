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
arr = list(map(int,input().split()))
my_set = set()
my_dict = dict()

for num in arr:
    my_set.add(num)

numbers = list(my_set)
numbers.sort()

for i in range(len(numbers)):
    my_dict[numbers[i]] = i
ans = []
for num in arr:
    ans.append(my_dict[num])

print(*ans)




