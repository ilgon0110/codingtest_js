

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
vistied = [0 for _ in range(N+1)]
tmp = set()

for _ in range(M):
    [a, b] = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)


def DFS(L, node):
    if L == 2:
        return
    else:
        for v in graph[node]:
            if v == 1:
                continue
            tmp.add(v)
            DFS(L+1, v)


DFS(0, 1)

print(len(tmp))
