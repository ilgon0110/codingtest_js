import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = [0 for _ in range(N+1)]
tmp = []

def DFS(L):
    if L == M:
        print(*tmp)
    else:
        for i in range(N):
            if visited[i] > 0:
                continue
            visited[i] = 1
            tmp.append(arr[i])
            DFS(L+1)
            tmp.pop()
            visited[i] = 0

DFS(0)
