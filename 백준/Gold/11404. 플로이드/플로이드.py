import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

dist = [[sys.maxsize for _ in range(N+1)] for _ in range(N+1)]

for i in range(1, N+1):
    dist[i][i] = 0
    for weight, to in graph[i]:
        dist[i][to] = min(dist[i][to], weight)

def floyd():
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


floyd()

for i in range(1, N+1):
    for j in range(1, N+1):
        if dist[i][j] == sys.maxsize:
            dist[i][j] = 0

for i in range(1, N+1):
    ans = dist[i]
    print(*ans[1:len(ans)])
