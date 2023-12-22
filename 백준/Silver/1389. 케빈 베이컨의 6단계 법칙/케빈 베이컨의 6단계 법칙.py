import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)


def BFS(node, target):
    queue = deque()
    queue.append(node)
    dist = [0 for _ in range(N+1)]
    visited = [0 for _ in range(N+1)]
    while (queue):
        nextNode = queue.popleft()
        if nextNode == target:
            break
        for v in graph[nextNode]:
            if visited[v] > 0:
                continue
            queue.append(v)
            visited[v] = 1
            dist[v] = dist[nextNode] + 1
    return dist[target]


tmp = []
for i in range(1, N+1):
    ans = 0
    for j in range(1, N+1):
        if i == j:
            continue
        ans += BFS(i, j)
    tmp.append(ans)

target = min(tmp)
for i in range(len(tmp)):
    if tmp[i] == target:
        print(i+1)
        break
