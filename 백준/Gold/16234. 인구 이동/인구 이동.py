import sys
from collections import deque

input = sys.stdin.readline

N,L,R = map(int,input().split())
board = []
dx = [-1,0,1,0]
dy = [0,-1,0,1]
for _ in range(N):
    board.append(list(map(int,input().split())))

def open_gate(visited,x,y):
    queue = deque()
    visited[x][y] = 1
    queue.append((x,y))
    result = []

    while queue:
        x,y = queue.popleft()
        result.append([board[x][y],x,y])
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] == 0:
                diff = abs(board[x][y] - board[nx][ny])
                if L <= diff <= R:
                    visited[nx][ny] = 1
                    queue.append((nx,ny))

    return [visited,result]


flag = True
answer = 0
while flag:
    new_board = [[0 for _ in range(N)] for _ in range(N)]
    copy_board = [[0 for _ in range(N)] for _ in range(N)]
    flag = False
    for i in range(N):
        for j in range(N):
            if new_board[i][j] == 0:
                [visited, result] = open_gate(new_board, i, j)
                new_board = visited
                #국경이 열리고 나라 2개가 연합되었다는 의미
                if len(result) > 1:
                    flag = True
                total = 0
                for [people,x,y] in result:
                    total += people
                target_people = total // len(result)
                for [people,x,y] in result:
                    copy_board[x][y] = target_people

    if flag == False:
        break
    board = copy_board
    answer += 1

print(answer)