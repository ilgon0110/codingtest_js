import sys
input = sys.stdin.readline

N, M = map(int, input().split())

tmp = []
total = 0

visited = [0 for _ in range(N+1)]

def DFS(L, s):
    if L == M:
        print(*tmp)
        return
    else:
        for i in range(s, N+1):
            if visited[i] > 0:
                continue
            visited[i] = 1
            tmp.append(i)
            DFS(L+1, i+1)
            tmp.pop()
            visited[i] = 0

DFS(0, 1)
