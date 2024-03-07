import sys

input = sys.stdin.readline

V = int(input())
graph = [[] for _ in range(V+1)]

for _ in range(V):
    [start, *arr] = list(map(int, input().split()))
    index = arr.index(-1)
    for i in range(0, index, 2):
        end = arr[i]
        weight = arr[i+1]
        graph[start].append((weight, end))

def DFS(node, total, visited):
    for v in graph[node]:
        weight, to = v
        if visited[to] == -1:
            cost = total+weight
            visited[to] = cost
            DFS(to, cost, visited)

visited = [-1 for _ in range(V+1)]
visited[1] = 0
DFS(1, 0, visited)
start = visited.index(max(visited))
dist = [-1 for _ in range(V+1)]
dist[start] = 0
DFS(start, 0, dist)
print(max(dist))
