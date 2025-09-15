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

R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]

def idx(x, y):
    return x * C + y

N = R * C
parent = list(range(N))
size = [1] * N

def find(a):
    # iterative with path compression
    while parent[a] != a:
        parent[a] = parent[parent[a]]
        a = parent[a]
    return a

def union(a, b):
    ra = find(a)
    rb = find(b)
    if ra == rb:
        return
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]

dx = (-1, 0, 1, 0)
dy = (0, -1, 0, 1)

ducks = []
ice_visited = [[0] * C for _ in range(R)]
ice_queue = deque()

# Initial union of existing water cells and collect adjacent ice (once)
for x in range(R):
    for y in range(C):
        if board[x][y] != 'X':
            if board[x][y] == 'L':
                ducks.append((x, y))
            a = idx(x, y)
            # union with previously-seen neighbors that are water
            for k in range(4):
                nx = x + dx[k]; ny = y + dy[k]
                if 0 <= nx < R and 0 <= ny < C:
                    if board[nx][ny] != 'X':
                        union(a, idx(nx, ny))
                    else:
                        if not ice_visited[nx][ny]:
                            ice_visited[nx][ny] = 1
                            ice_queue.append(idx(nx, ny))

# if ducks are already connected
s1 = idx(ducks[0][0], ducks[0][1])
s2 = idx(ducks[1][0], ducks[1][1])
day = 0
if find(s1) == find(s2):
    print(0)
    sys.exit(0)

# simulate day by day, each ice cell is processed once (when it was first adjacent to water)
while ice_queue:
    day += 1
    next_queue = deque()
    # process all ice cells queued to melt today
    while ice_queue:
        cur = ice_queue.popleft()
        x = cur // C; y = cur % C
        if board[x][y] == '.':
            continue  # already melted earlier by adjacency
        board[x][y] = '.'
        # union with adjacent water (or melted) cells
        for k in range(4):
            nx = x + dx[k]; ny = y + dy[k]
            if 0 <= nx < R and 0 <= ny < C:
                if board[nx][ny] != 'X':
                    union(cur, idx(nx, ny))
                else:
                    if not ice_visited[nx][ny]:
                        ice_visited[nx][ny] = 1
                        next_queue.append(idx(nx, ny))
    # after melting today's cells, check swan connectivity
    if find(s1) == find(s2):
        print(day)
        break
    # move to next day's candidates
    ice_queue = next_queue
