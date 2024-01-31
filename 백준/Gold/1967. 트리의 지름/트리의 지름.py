import sys
import heapq

input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))


def dijkstra(start):
    queue = []
    dist[start] = 0
    heapq.heappush(queue, (0, start))

    while queue:
        weight, node = heapq.heappop(queue)
        for nextWeight, to in graph[node]:
            cost = weight + nextWeight
            if dist[to] <= cost:
                continue
            dist[to] = cost
            heapq.heappush(queue, (cost, to))


ans = 0

dist = [sys.maxsize for _ in range(N+1)]
dist[0] = -1
dijkstra(1)
start = dist.index(max(dist))
dist = [sys.maxsize for _ in range(N+1)]
dist[0] = -1
dijkstra(start)
print(max(dist))
