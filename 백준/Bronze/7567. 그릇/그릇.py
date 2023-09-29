import sys
import itertools
import heapq
import bisect
import collections
from collections import deque
import math
import queue
# sys.stdin = open("input.txt", "r")

N = list(str(input()))

queue = deque()
queue.append(N[0])
answer = 10
for i in range(1, len(N)):
    if queue[len(queue) - 1] == N[i]:
        answer += 5
    else:
        answer += 10
    queue.append(N[i])
print(answer)
