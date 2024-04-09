import sys

input = sys.stdin.readline

N,M = map(int,input().split())
r,c,d = map(int,input().split())
board = []

direction = d

#북,동,남,서
dx = [-1,0,1,0]
dy = [0,1,0,-1]
for _ in range(N):
    board.append(list(map(int,input().split())))

answer = 0
def move(x,y):
    global direction
    global answer
    if board[x][y] == 0:
        board[x][y] = 9
        answer += 1
    cnt = 0
    for k in range(4):
        idx = k
        nx = x+dx[idx]
        ny = y+dy[idx]
        if 0<=nx<N and 0<=ny<M:
            #청소되지 않은 칸이 있는 경우(3번)
            if board[nx][ny] == 0:
                direction -= 1
                if direction == -1:
                    direction = 3
                nx = x+dx[direction]
                ny = y+dy[direction]
                if board[nx][ny] == 0:
                    return [nx,ny]
                else:
                    return [x,y]
            else:
                cnt+=1

        # 4칸 중 청소되지 않은 칸이 없는 경우(2번)
        if cnt == 4:
            nx = x-dx[direction]
            ny = y-dy[direction]
            if board[nx][ny] == 1:
                return False
            return [nx,ny]

x = r
y = c
flag = True

while flag:
    result = move(x,y)
    if result == False:
        break
    else:
        x = result[0]
        y = result[1]

print(answer)



