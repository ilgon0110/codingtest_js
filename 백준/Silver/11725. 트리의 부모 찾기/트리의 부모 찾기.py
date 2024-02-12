import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]
parent = [1 for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def DFS(node):
    for nextNode in graph[node]:
        if visited[nextNode] > 0:
            continue
        visited[node] = 1
        parent[nextNode] = node
        DFS(nextNode)

visited[1] = 1
DFS(1)
for i in range(2, len(parent)):
    print(parent[i])
