import sys
import heapq

N, M, X = map(int, sys.stdin.readline().split())


graph = [[] for _ in range(N+1)]

for _ in range(M):
    [start, to, weight] = list(map(int, sys.stdin.readline().split()))
    graph[start].append([to, weight])


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        weight, now = heapq.heappop(q)
        if dist[now] < weight:
            continue
        for to, nowWeight in graph[now]:
            cost = weight + nowWeight
            if cost < dist[to]:
                dist[to] = cost
                heapq.heappush(q, (cost, to))


result = [[]]

for i in range(1, N+1):
    dist = [sys.maxsize for _ in range(N+1)]
    dijkstra(i)
    result.append(dist)

ans = 0
for i in range(1, N+1):
    ans = max(ans, result[i][X] + result[X][i])

print(ans)
