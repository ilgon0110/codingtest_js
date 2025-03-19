import sys

input = sys.stdin.readline

N, M = map(int, input().split())
tmp = []


def DFS(L, s):
    if L == M:
        print(*tmp)
    else:
        for i in range(s, N+1):
            tmp.append(i)
            DFS(L+1, i)
            tmp.pop()


DFS(0, 1)
