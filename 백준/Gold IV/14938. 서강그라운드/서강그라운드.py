import sys

input = sys.stdin.readline

N, M, R = map(int, input().split())
items = list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
for _ in range(R):
    a, b, l = map(int, input().split())
    graph[a].append((l, b))
    graph[b].append((l, a))

INF = sys.maxsize
dist = [[INF for _ in range(N+1)] for _ in range(N+1)]

for i in range(1, N+1):
    dist[i][i] = 0
    for weight, to in graph[i]:
        dist[i][to] = weight

def fluid():
    for k in range(1,N+1):
        for i in range(1,N+1):
            for j in range(1,N+1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

fluid()
ans = 0
for i in range(1, N+1):
    total = 0
    for j in range(1, N+1):
        if dist[i][j] <= M:
            cost = items[j-1]
            total += cost
    ans = max(ans, total)
print(ans)
