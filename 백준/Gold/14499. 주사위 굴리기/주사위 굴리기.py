import sys

input = sys.stdin.readline

N,M,x,y,K = map(int,input().split())
board = []
dice = [[-1,-1,-1] for _ in range(4)]
dice[0][1] = 0
dice[1][0] = 0
dice[1][1] = 0
dice[1][2] = 0
dice[2][1] = 0
dice[3][1] = 0
for _ in range(N):
    board.append(list(map(int,input().split())))
orders = list(map(int,input().split()))

def move(direction):
    if direction == 1:
        dice[1][0] , dice[1][1] = dice[1][1] , dice[1][0]
        dice[1][0] , dice[1][2] = dice[1][2] , dice[1][0]
        dice[1][0] , dice[3][1] = dice[3][1] , dice[1][0]
    if direction == 2:
        dice[1][0] , dice[1][1] = dice[1][1] , dice[1][0]
        dice[1][1] , dice[3][1] = dice[3][1] , dice[1][1]
        dice[1][1] , dice[1][2] = dice[1][2] , dice[1][1]
    if direction == 3:
        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[1][1], dice[2][1], dice[3][1], dice[0][1]
    if direction == 4:
        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[3][1], dice[0][1], dice[1][1], dice[2][1]

dx = [(0,0), (0,1),(0,-1),(-1,0),(1,0)]

for order in orders:
    x = x+dx[order][0]
    y = y+dx[order][1]

    if 0<=x<N and 0<=y<M:
        move(order)
        if board[x][y] == 0:
            board[x][y] = dice[3][1]
        else:
            dice[3][1] = board[x][y]
            board[x][y] = 0
        print(dice[1][1])
    else:
        x-=dx[order][0]
        y-=dx[order][1]


