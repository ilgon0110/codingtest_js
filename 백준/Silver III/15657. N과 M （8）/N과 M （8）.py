import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
tmp = []

def DFS(L, s):
    if L == M:
        print(*tmp)
    else:
        for i in range(N):
            if arr[i] < arr[s]:
                continue
            tmp.append(arr[i])
            DFS(L+1, i)
            tmp.pop()


DFS(0, 0)
