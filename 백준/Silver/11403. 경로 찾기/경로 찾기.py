
N = int(input())

graph = [[0 for _ in range(N)] for _ in range(N)]


def DFS(start, end, vistied):
    global graph
    graph[start][end] = 1
    for i in range(len(graph[end])):
        target = graph[end][i]
        if target == 1 and vistied[i] == 0:
            vistied[i] = 1
            DFS(start, i, vistied)


arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            graph[i][j] = 1

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            DFS(i, j, [0 for _ in range(N)])

for i in range(N):
    print(' '.join(map(str, graph[i])))
