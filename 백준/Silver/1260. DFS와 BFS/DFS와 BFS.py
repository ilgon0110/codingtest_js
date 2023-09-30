import sys
from collections import deque

# sys.stdin = open("input.txt", "r")

[N, M, V] = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(M)]

graph = [list() for _ in range(N + 1)]

for [a, b] in arr:
    graph[a].append(b)
    graph[b].append(a)

visited = list(0 for _ in range(N+1))
dfsAns = []

for v in graph:
    if (len(v) > 0):
        v = v.sort()
    else:
        v = v


def DFS(L):
    dfsAns.append(L)
    for i in range(0, len(graph[L])):
        node = graph[L][i]
        if (visited[node]):
            continue
        visited[node] = 1
        DFS(node)


visited[V] = 1
DFS(V)


def BFS(graph):
    visited = list(0 for _ in range(N+1))
    queue = deque()
    ans = []
    queue.append(V)
    visited[V] = 1

    while len(queue) > 0:
        node = queue.popleft()
        ans.append(node)
        for i in range(0, len(graph[node])):
            nv = graph[node][i]
            if (visited[nv] == 1):
                continue
            visited[nv] = 1
            queue.append(nv)
    return ans


print(*dfsAns)
print(*BFS(graph))
