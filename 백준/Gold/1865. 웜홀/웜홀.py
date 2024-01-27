import sys

input = sys.stdin.readline

TC = int(input())

def velman(start):
    dist[start] = 0
    for check in range(N):
        for node in range(1, N+1):
            for weight, to in graph[node]:
                if dist[to] > dist[node] + weight:
                    dist[to] = dist[node] + weight
                    if check == N-1:
                        return False
    return True


for _ in range(TC):
    N, M, W = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a].append((c, b))
        graph[b].append((c, a))
    for _ in range(W):
        a, b, c = map(int, input().split())
        graph[a].append((-c, b))
    dist = [sys.maxsize for _ in range(N+1)]

    if velman(1) == True:
        print('NO')
    else:
        print('YES')
