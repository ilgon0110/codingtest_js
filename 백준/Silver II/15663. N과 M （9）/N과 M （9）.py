import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
tmp = []
before = [0 for _ in range(M)]
visited = [0 for _ in range(N)]


def DFS(L):
    if L == M:
        print(*tmp)
        return
    else:
        bf = 0
        for i in range(N):
            if bf == arr[i]:
                continue
            if visited[i] > 0:
                continue
            visited[i] = 1
            before[L] = arr[i]
            bf = before[L]
            tmp.append(arr[i])
            DFS(L+1)
            tmp.pop()
            visited[i] = 0


DFS(0)
