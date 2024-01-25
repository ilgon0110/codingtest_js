V = int(input())

graph = [[] for _ in range(V+1)]

for _ in range(V):
    num, *nodes = list(map(int, input().split()))
    last = nodes.index(-1)
    for i in range(0, last-1, 2):
        graph[num].append([nodes[i], nodes[i+1]])

def DFS(node, total, visited):
    for to, weight in graph[node]:
        if visited[to] == -1:
            visited[to] = total+weight
            DFS(to, total+weight, visited)

visited = [-1 for _ in range(V+1)]
visited[1] = 0
DFS(1, 0, visited)
start = visited.index(max(visited))
dist = [-1 for _ in range(V+1)]
dist[start] = 0
DFS(start, 0, dist)
print(max(dist))
