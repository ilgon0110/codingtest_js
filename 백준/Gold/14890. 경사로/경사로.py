import sys

input = sys.stdin.readline

N,L = map(int , input().split())
board = []
roads = []
for _ in range(N):
    board.append(list(map(int,input().split())))

for i in range(N):
    roads.append(board[i])
    tmp = []
    for j in range(N):
        tmp.append(board[j][i])
    roads.append(tmp)

def check_road(road):
    height = road[0]
    flag = True
    for num in road:
        if num != height:
            flag = False
    if flag:
        return True

    visited = [0 for _ in range(N)]

    for i in range(N-1):
        if road[i] == road[i+1]:
            continue
        #높이가 다를 때
        else:
            diff_height = abs(road[i] - road[i+1])
            if diff_height > 1:
                return False
            #높이 차이가 1일 때
            if road[i+1] > road[i]:
                low_direction = -1
                low_height = road[i]
                idx = i
                for j in range(idx,idx-L,low_direction):
                    if j < 0 or j >= N:
                        return False
                    if road[j] != low_height:
                        return False
                    if visited[j] == 1:
                        return False
                for j in range(idx,idx-L,low_direction):
                    visited[j] = 1
            else:
                low_direction = 1
                low_height = road[i+1]
                idx = i+1
                # 낮은 높이가 L만큼 연속되어 있는지 확인
                for j in range(idx,idx+L,low_direction):
                    if j < 0 or j >= N:
                        return False
                    if road[j] != low_height:
                        return False
                    if visited[j] == 1:
                        return False
                for j in range(idx,idx+L,low_direction):
                    visited[j] = 1

    return True


answer = 0

for road in roads:
    one = check_road(road)
    two = check_road(list(reversed(road)))

    if one or two is True:
        answer+=1

print(answer)
