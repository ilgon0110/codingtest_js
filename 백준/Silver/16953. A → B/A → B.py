import sys
input = sys.stdin.readline
INF = sys.maxsize
A, B = map(int, input().split())
ans = INF

def DFS(now, cnt):
    if now > B:
        return
    if now == B:
        global ans
        ans = min(cnt, ans)
        return
    else:
        for nextNode in [now*2, now*10+1]:
            DFS(nextNode, cnt+1)


DFS(A, 1)
if ans == INF:
    print(-1)
else:
    print(ans)
