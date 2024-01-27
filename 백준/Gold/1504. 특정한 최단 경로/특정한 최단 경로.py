import sys
import heapq

N, E = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

v1, v2 = map(int, sys.stdin.readline().split())

def dijkstra(node, dist):
    queue = []
    dist[node] = 0
    heapq.heappush(queue, [node, 0])

    while queue:
        [target, weight] = heapq.heappop(queue)
        for to, nextWeight in graph[target]:
            cost = weight + nextWeight
            if dist[to] <= cost:
                continue
            dist[to] = cost
            heapq.heappush(queue, [to, cost])
    return dist


result = [[]]

result.append(dijkstra(1, [sys.maxsize for _ in range(N+1)]))
result.append(dijkstra(v1, [sys.maxsize for _ in range(N+1)]))
result.append(dijkstra(v2, [sys.maxsize for _ in range(N+1)]))

ans = min(result[1][v1] + result[2][v2] + result[3][N],
          result[1][v2] + result[3][v1] + result[2][N])

if ans >= sys.maxsize:
    print(-1)
else:
    print(ans)
