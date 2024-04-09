import sys

input = sys.stdin.readline

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int,input().split())))

start_team = []

visited = [0 for _ in range(N)]

def count_score(arr):
    result = 0
    for i in arr:
        for j in arr:
            if i == j:
                continue
            result += board[i][j]
    return result

total_score = count_score([i for i in range(N)])
answer = sys.maxsize
def recursive(L,s,start_team):
    if L == N/2:
        link_team = []
        global answer
        for i in range(N):
            if visited[i] == 0:
                link_team.append(i)
        start_score = count_score(start_team)
        link_score = count_score(link_team)
        answer = min(answer , abs(start_score-link_score))
        return
    else:
        for i in range(s,N):
            start_team.append(i)
            visited[i] = 1
            recursive(L+1,i+1 , start_team)
            start_team.pop()
            visited[i] = 0

recursive(0,0 , [])
print(answer)