import sys

N = int(input())
V = int(input())
arr = [list(map(int, input().split())) for _ in range(V)]

graph = [[] for _ in range(N+1)]

for [a, b] in arr:
    graph[a].append(b)
    graph[b].append(a)

vistied = [0 for _ in range(N+1)]

count = -1


def DFS(L):
    global count
    count += 1
    for nextNode in graph[L]:
        if (vistied[nextNode] > 0):
            continue
        vistied[nextNode] = 1
        DFS(nextNode)


vistied[1] = 1
DFS(1)
print(count)
