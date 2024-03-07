import sys
input = sys.stdin.readline

TC = int(input())
INF = sys.maxsize

def velman_ford(start):
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
        S, E, T = map(int, input().split())
        graph[S].append((T, E))
        graph[E].append((T, S))
    for _ in range(W):
        S, E, T = map(int, input().split())
        graph[S].append((-T, E))

    dist = [INF for _ in range(N+1)]
    if velman_ford(1) == True:
        print('NO')
    else:
        print('YES')
