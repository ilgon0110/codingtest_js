import sys

input = sys.stdin.readline

R,C,M = map(int,input().split())
board = [[[] for _ in range(C+1)] for _ in range(R+1)]
for _ in range(M):
    r,c,s,d,z = map(int,input().split())
    board[r][c].append([s,d,z])

x = 0
y = 0
ans = 0
def catch_shark(y):
    global ans
    for i in range(R+1):
        if len(board[i][y]) > 0:
            [s,d,z] = board[i][y][0]
            ans += z
            board[i][y] = []
            break

# -,위,아래,오른쪽,왼쪽
dx = [0,-1,1,0,0]
dy = [0,0,0,1,-1]
def move_shark():
    new_board = [[[] for _ in range(C+1)] for _ in range(R+1)]
    for i in range(1,R+1):
        for j in range(1,C+1):
            if len(board[i][j]) > 0:
                [s,d,z] = board[i][j][0]
                direction = d
                nx = i
                ny = j
                for k in range(s):
                    nx += dx[direction]
                    ny += dy[direction]
                    # 어장 탈출하는 경우 = 방향 반대로 바꿔줘야 하는 경우
                    if nx == 0:
                        nx -= dx[direction]
                        direction = 2
                        nx += dx[direction]
                    if nx == R+1:
                        nx -= dx[direction]
                        direction = 1
                        nx += dx[direction]
                    if ny == 0:
                        ny -= dy[direction]
                        direction = 3
                        ny += dy[direction]
                    if ny == C+1:
                        ny -= dy[direction]
                        direction = 4
                        ny += dy[direction]
                new_board[nx][ny].append([s,direction,z])

    # 한 칸에 여러 상어가 있는 경우
    for i in range(1,R+1):
        for j in range(1,C+1):
            if len(new_board[i][j]) > 1:
                new_board[i][j].sort(key=lambda x: x[2])
                max_shark = new_board[i][j].pop()
                new_board[i][j] = [max_shark]

    return new_board



while y <= C:
    y += 1
    if y > C:
        break
    #상어 잡기
    catch_shark(y)
    #상어 이동
    new_board = move_shark()
    board = new_board
    # for i in range(1,R+1):
    #     print(board[i])
    # print(ans)
print(ans)

