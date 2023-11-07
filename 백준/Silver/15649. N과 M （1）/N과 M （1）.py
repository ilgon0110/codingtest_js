[N, M] = list(map(int, input().split()))
tmp = []


def DFS(L):
    if L == M:
        print(' '.join(map(str, tmp)))
    else:
        for i in range(1, N+1):
            if i not in tmp:
                tmp.append(i)
                DFS(L+1)
                tmp.pop()

DFS(0)
