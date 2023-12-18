[N, K] = list(map(int, input().split()))
cnt = 0

def DFS(L, s):
    if L == K:
        global cnt
        cnt += 1
        return
    else:
        for i in range(s, N+1):
            DFS(L+1, i+1)

DFS(0, 1)
print(cnt)
