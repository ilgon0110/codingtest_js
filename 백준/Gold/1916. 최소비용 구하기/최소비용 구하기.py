import sys
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

start, end = map(int, input().split())
dist = [sys.maxsize for _ in range(N+1)]

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        weight, node = heapq.heappop(q)
        if node == end:
            break
        for nextWeight, to in graph[node]:
            cost = weight + nextWeight
            if dist[to] <= cost:
                continue
            dist[to] = cost
            heapq.heappush(q, (cost, to))

dijkstra(start)
print(dist[end])
