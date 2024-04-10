import sys

input = sys.stdin.readline

wheels = []
for _ in range(4):
    wheels.append(list(map(int,input().rstrip())))
K = int(input())
orders = []
for _ in range(K):
    num , direction = map(int,input().split())
    orders.append((num,direction))


def rotate(index,direction,visited):
    # 시계 방향
    visited[index] = 1

    #양 옆 톱니바퀴가 회전해야 하는 지 확인
    if index > 0 and wheels[index-1][2] != wheels[index][6] and visited[index-1] == 0:
        if direction == 1:
            rotate(index-1,-1,visited)
        elif direction == -1:
            rotate(index-1,1,visited)
    if index < 3 and wheels[index+1][6] != wheels[index][2] and visited[index+1] == 0:
        if direction == 1:
            rotate(index+1,-1,visited)
        elif direction == -1:
            rotate(index+1,1,visited)

    if direction == 1:
        tmp = []
        for i in range(7):
            tmp.append(wheels[index][i])
        last = wheels[index][7]
        wheels[index] = [last, *tmp]
    # 반시계 방향
    if direction == -1:
        tmp = []
        for i in range(1,8):
            tmp.append(wheels[index][i])
        last = wheels[index][0]
        wheels[index] = [*tmp, last]



for num,direction in orders:
    rotate(num-1,direction,[0,0,0,0])

answer = wheels[0][0] + wheels[1][0]*2 + wheels[2][0]*4 + wheels[3][0]*8
print(answer)