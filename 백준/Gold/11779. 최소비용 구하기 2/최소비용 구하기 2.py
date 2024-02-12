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
    dist[start] = 0
    queue = []
    heapq.heappush(queue, [0, start, [start]])

    while queue:
        [weight, node, track] = heapq.heappop(queue)
        if node == end:
            return dist[end], track
        for nextWeight, to in graph[node]:
            cost = weight + nextWeight
            if dist[to] <= cost:
                continue
            dist[to] = cost
            heapq.heappush(queue, [cost, to, track + [to]])


answer, list = dijkstra(start)

print(answer)
print(len(list))
print(*list)
