T = int(input())

for _ in range(T):
    N = int(input())
    cnt = 0

    def DFS(L, s):
        if (s > N):
            return
        if (s == N):
            global cnt
            cnt += 1
            return
        else:
            DFS(L+1, s+1)
            DFS(L+1, s+2)
            DFS(L+1, s+3)
    DFS(0, 0)
    print(cnt)
