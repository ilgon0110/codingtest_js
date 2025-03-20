import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
before = [0 for _ in range(M)]
tmp = []

def DFS(L, s):
    if L == M:
        print(*tmp)
    else:
        bf = 0
        for i in range(N):
            if arr[i] < arr[s]:
                continue
            if bf == arr[i]:
                continue
            before[L] = arr[i]
            bf = before[L]
            tmp.append(arr[i])
            DFS(L+1, i)
            tmp.pop()

DFS(0, 0)
