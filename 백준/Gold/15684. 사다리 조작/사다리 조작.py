import sys

input = sys.stdin.readline

N,M,H = map(int,input().split())
row_lines = []
not_row_lines = []
for _ in range(M):
    a,b = map(int,input().split())
    row_lines.append((a,b))
board = [[0 for _ in range(N*2)]]
for _ in range(H):
    board.append([1 for _ in range(N*2)])
board.append([0 for _ in range(N*2)])
for a,b in row_lines:
    board[a][(b-1)*2] = 2
    board[a][(b-1)*2+1] = 2
    board[a][b*2] = 2


#가로선이 없는 모든 경우의 수 not_row_lines 배열에 포함
for i in range(1,H+1):
    for j in range(0,(N-1)*2,2):
        if board[i][j] == 1 and board[i][j+1] == 1 and board[i][j+2] == 1:
            not_row_lines.append((i, j//2 + 1))


def move(number):
    x = 0
    y = number

    while x != H+1:
        #가로선을 만났을 때
        if board[x][y] == 2:
            #왼쪽이동
            if y > 0 and board[x][y-1] == 2 and board[x][y-2] == 2:
                y -= 2
            #오른쪽 이동
            elif y < (N*2)-2 and board[x][y+1] == 2 and board[x][y+2] == 2:
                y += 2
        x+=1

    return y

def check():
    for i in range(0,N*2,2):
        result = move(i)
        if i != result:
            return False
    return True

answer = 4

def recursive(L,s,tmp):
    if L > 3:
        return

    if check():
        global answer
        answer = min(answer,L)
        return
    for i in range(s,len(not_row_lines)):
        a,b = not_row_lines[i]

        if board[a][(b - 1) * 2] == 2 or board[a][(b - 1) * 2 + 1] == 2 or board[a][b * 2] == 2:
            continue
        board[a][(b - 1) * 2] = 2
        board[a][(b - 1) * 2 + 1] = 2
        board[a][b * 2] = 2
        tmp.append((a, b))
        recursive(L+1,i+1,tmp)
        board[a][(b - 1) * 2] = 1
        board[a][(b - 1) * 2 + 1] = 1
        board[a][b * 2] = 1
        tmp.pop()

recursive(0,0,[])
if answer == 4:
    print(-1)
else:
    print(answer)

