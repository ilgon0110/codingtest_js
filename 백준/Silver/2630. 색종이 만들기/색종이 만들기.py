import sys
input = sys.stdin.readline

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))


def isBlock(arr):
    n = len(arr)
    flag = arr[0][0]
    for i in range(n):
        for j in range(n):
            if arr[i][j] != flag:
                return False
    return True


white = 0
blue = 0


def DFS(L, arr):
    if isBlock(arr) == True:
        global blue
        global white
        if arr[0][0] == 1:
            blue += 1
        else:
            white += 1
        return
    else:
        tmp = []
        tmp2 = []
        tmp3 = []
        tmp4 = []
        for i in range(len(arr)//2):
            tmp.append(arr[i][0:len(arr)//2])
            tmp3.append(arr[i][len(arr)//2: len(arr)])
        for i in range(len(arr)//2, len(arr)):
            tmp2.append(arr[i][len(arr)//2: len(arr)])
            tmp4.append(arr[i][0:len(arr)//2])
        DFS(L+1, tmp)
        DFS(L+1, tmp3)
        DFS(L+1, tmp2)
        DFS(L+1, tmp4)


DFS(0, board)
print(white)
print(blue)
