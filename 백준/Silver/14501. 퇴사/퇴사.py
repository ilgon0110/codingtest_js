import sys

input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    t,p = map(int , input().split())
    arr.append((t,p))
visited = [0 for _ in range(N)]
answer = 0

def recursive(L,start,total):
    global answer
    answer = max(answer , total)

    for i in range(start,N):
        t,p = arr[i]
        if visited[i] == 0:
            if i+t <= N:
                for j in range(i, i + t):
                    visited[j] = 1
                total = total+p
                recursive(L+1,i+t,total)
                for j in range(i, i + t):
                    visited[j] = 0
                total -= p
                
recursive(0,0,0)
print(answer)