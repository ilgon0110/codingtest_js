import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
visited = [0 for _ in range(N+1)]
arr.sort()
tmp = []
before = [0 for _ in range(N+1)]


def DFS(L):
    if L == M:
        print(*tmp)
        return
    else:
        before[L] = 0
        for i in range(N):
            if before[L] == arr[i]:
                continue
            if visited[i]:
                continue
            before[L] = arr[i]
            visited[i] = 1
            tmp.append(arr[i])
            DFS(L+1)
            visited[i] = 0
            tmp.pop()


DFS(0)


# print(arr)
