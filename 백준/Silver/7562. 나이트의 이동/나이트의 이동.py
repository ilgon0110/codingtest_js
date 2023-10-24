from collections import deque

dx = [[-2, -1], [-1, -2], [1, -2], [2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1]]

I = int(input())

for _ in range(I):
    N = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))

    queue = deque()
    board = [[0 for _ in range(N)] for _ in range(N)]
    queue.append(start)
    board[start[0]][start[1]] = 1
    count = 0
    while len(queue):
        [x, y] = queue.popleft()
        if x == end[0] and y == end[1]:
            print(board[x][y]-1)
            break
        for i in range(len(dx)):
            nx = x + dx[i][0]
            ny = y + dx[i][1]

            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0:
                queue.append([nx, ny])
                board[nx][ny] = board[x][y] + 1
