import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

trees = []
snakes = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    trees.append([x, y])

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    snakes.append([x, y])

dist = [0 for _ in range(101)]
visited = [0 for _ in range(101)]
queue = deque()
visited[1] = 1
queue.append(1)

while queue:
    pos = queue.popleft()
    if pos == 100:
        break
    for i in range(1, 7):
        nPos = pos + i
        if nPos > 100 or visited[nPos] > 0:
            continue
        for tree in trees:
            if tree[0] == nPos:
                nPos = tree[1]
        for snake in snakes:
            if snake[0] == nPos:
                nPos = snake[1]
        if not visited[nPos]:
            visited[nPos] = 1
            dist[nPos] = dist[pos] + 1
            queue.append(nPos)

print(dist[100])
