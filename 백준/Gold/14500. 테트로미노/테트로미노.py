import sys

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
except_visited = [[0 for _ in range(M)] for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

answer = 0


def DFS(L, x, y, visited, total):
    if L == 3:
        global answer
        answer = max(answer, total)
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx >= 0 and nx < N and ny >= 0 and ny < M and visited[nx][ny] == 0):
                total += board[nx][ny]
                visited[nx][ny] = 1
                DFS(L+1, nx, ny, visited, total)
                visited[nx][ny] = 0
                total -= board[nx][ny]


def except_DFS(L, x, y, except_visited, total):
    if L == 1:
        directions = [[[-1, 0], [0, 1]], [[1, 0], [0, 1]],
                      [[1, 0], [0, -1]], [[-1, 0], [0, -1]]]
        for direction in directions:
            [one, two] = direction
            nx = x + one[0]
            ny = y + one[1]
            nx2 = x + two[0]
            ny2 = y + two[1]
            if (nx >= 0 and nx < N and ny >= 0 and ny < M and except_visited[nx][ny] == 0):
                if (nx2 >= 0 and nx2 < N and ny2 >= 0 and ny2 < M and except_visited[nx2][ny2] == 0):
                    total = total + board[nx][ny] + board[nx2][ny2]
                    except_visited[nx][ny] = 1
                    except_visited[nx2][ny2] = 1
                    global answer
                    answer = max(answer, total)
                    except_visited[nx][ny] = 0
                    except_visited[nx2][ny2] = 0
                    total = total - board[nx][ny] - board[nx2][ny2]
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx >= 0 and nx < N and ny >= 0 and ny < M and except_visited[nx][ny] == 0):
                total += board[nx][ny]
                except_visited[nx][ny] = 1
                except_DFS(L+1, nx, ny, except_visited, total)
                except_visited[nx][ny] = 0
                total -= board[nx][ny]


for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        except_visited[i][j] = 1
        DFS(0, i, j, visited, board[i][j])
        except_DFS(0, i, j, except_visited, board[i][j])
        visited[i][j] = 0
        except_visited[i][j] = 0

print(answer)
