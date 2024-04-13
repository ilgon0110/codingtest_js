import sys

input = sys.stdin.readline

N,M,K = map(int,input().split())
board = [[5 for _ in range(N)] for _ in range(N)]
trees = [[[] for _ in range(N)] for _ in range(N)]
fertilizer = []
for _ in range(N):
    fertilizer.append(list(map(int,input().split())))

for _ in range(M):
    x,y,z = map(int,input().split())
    trees[x-1][y-1].append(z)


dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

for year in range(K):
    death = []
    #봄

    for i in range(N):
        for j in range(N):
            if len(trees[i][j]) > 0:
                tmp = []
                trees[i][j].sort()
                for k in range(len(trees[i][j])):
                    tree = trees[i][j][k]
                    # print('year:', year , tree , i,j)
                    if board[i][j] >= tree:
                        board[i][j] -= tree
                        tmp.append(tree+1)
                    else:
                        death.append([tree,i,j])
                trees[i][j] = tmp

    #여름
    for [tree,i,j] in death:
        board[i][j] += tree//2

    #가을
    for i in range(N):
        for j in range(N):
            if len(trees[i][j]) > 0:
                for tree in trees[i][j]:
                    if tree >= 5 and tree % 5 == 0:
                        for k in range(8):
                            nx = i+dx[k]
                            ny = j+dy[k]
                            if 0<=nx<N and 0<=ny<N:
                                trees[nx][ny].append(1)

    #겨울
    for i in range(N):
        for j in range(N):
            board[i][j] += fertilizer[i][j]

ans = 0
for i in range(N):
    for j in range(N):
        ans += len(trees[i][j])

print(ans)