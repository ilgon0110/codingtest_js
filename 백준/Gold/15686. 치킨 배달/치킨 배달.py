import sys
from collections import deque

input = sys.stdin.readline
N,M = map(int,input().split())
board = []
for _ in range(N):
    board.append(list(map(int,input().split())))

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def get_dist(chickens):
    dists = [[sys.maxsize for _ in range(N)] for _ in range(N)]
    for x,y in chickens:
        queue = deque()
        visited = [[0 for _ in range(N)] for _ in range(N)]
        queue.append((x,y,1))

        while queue:
            x,y,dist = queue.popleft()

            for k in range(4):
                nx = x+dx[k]
                ny = y+dy[k]
                if 0<=nx<N and 0<=ny<N and board[nx][ny] == 1:
                    dists[nx][ny] = min(dists[nx][ny] , dist)

                if 0<=nx<N and 0<=ny<N and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx,ny,dist+1))
    total = 0
    for x,y in citys:
        total += dists[x][y]

    return total


chicken_house = []
citys = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            chicken_house.append((i,j))
        if board[i][j] == 1:
            citys.append((i,j))

answer = sys.maxsize
def recursive(L,s,tmp):
    if L == M:
        global  answer
        total = get_dist(tmp)
        answer = min(total,answer)
        return
    else:
        for i in range(s,len(chicken_house)):
            tmp.append(chicken_house[i])
            recursive(L+1,i+1,tmp)
            tmp.pop()

recursive(0,0,[])
print(answer)