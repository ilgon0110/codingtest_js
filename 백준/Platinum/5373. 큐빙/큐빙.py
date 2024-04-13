import sys

input = sys.stdin.readline

T = int(input())

def self_roate(side, direction):
    newBoard = [[0 for _ in range(3)] for _ in range(3)]
    if direction == "+":
        for i in range(3):
            for j in range(3):
                newBoard[i][j] = side[2 - j][i]

    elif direction == '-':
        for i in range(3):
            for j in range(3):
                newBoard[i][j] = side[j][2 - i]

    return newBoard

for _ in range(T):
    n = int(input())
    arr = list(input().split())

    blank = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    cube = [[blank for _ in range(3)] for _ in range(4)]
    cube[1][1] = [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']]
    cube[3][1] = [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']]
    cube[2][1] = [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']]
    cube[0][1] = [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']]
    cube[1][0] = [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']]
    cube[1][2] = [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']]

    def rotate(side,direction):
        if side == 'U':
            #F,L,B,R
            tmp = [cube[2][1][0] , [cube[1][0][0][2],cube[1][0][1][2],cube[1][0][2][2]],
                   cube[0][1][2], [cube[1][2][0][0],cube[1][2][1][0],cube[1][2][2][0]]]
            if direction == '+':
                cube[2][1][0] = list(reversed(tmp[3]))
                [cube[1][0][0][2], cube[1][0][1][2], cube[1][0][2][2]] = tmp[0]
                cube[0][1][2] = list(reversed(tmp[1]))
                [cube[1][2][0][0], cube[1][2][1][0], cube[1][2][2][0]] = tmp[2]
            else:
                cube[2][1][0] = tmp[1]
                [cube[1][0][0][2], cube[1][0][1][2], cube[1][0][2][2]] = list(reversed(tmp[2]))
                cube[0][1][2] = tmp[3]
                [cube[1][2][0][0], cube[1][2][1][0], cube[1][2][2][0]] = list(reversed(tmp[0]))
            up_side = cube[1][1]
            cube[1][1] = self_roate(up_side,direction)

        if side == 'D':
            # F,L,B,R
            tmp = [cube[2][1][2],[cube[1][0][0][0],cube[1][0][1][0],cube[1][0][2][0]],
                   cube[0][1][0],[cube[1][2][0][2], cube[1][2][1][2], cube[1][2][2][2]]]
            if direction == '+':
                cube[2][1][2] = tmp[1]
                [cube[1][0][0][0], cube[1][0][1][0], cube[1][0][2][0]] = list(reversed(tmp[2]))
                cube[0][1][0] = tmp[3]
                [cube[1][2][0][2], cube[1][2][1][2], cube[1][2][2][2]] = list(reversed(tmp[0]))
            else:
                cube[2][1][2] = list(reversed(tmp[3]))
                [cube[1][0][0][0], cube[1][0][1][0], cube[1][0][2][0]] = (tmp[0])
                cube[0][1][0] = list(reversed(tmp[1]))
                [cube[1][2][0][2], cube[1][2][1][2], cube[1][2][2][2]] = (tmp[2])
            down_side = cube[3][1]
            cube[3][1] = self_roate(down_side,direction)

        if side == 'L':
            # B,U,F,D
            tmp = [[cube[0][1][0][0],cube[0][1][1][0],cube[0][1][2][0]],
                   [cube[1][1][0][0],cube[1][1][1][0],cube[1][1][2][0]],
                   [cube[2][1][0][0],cube[2][1][1][0],cube[2][1][2][0]],
                   [cube[3][1][0][0],cube[3][1][1][0],cube[3][1][2][0]]]
            if direction == '+':
                [cube[0][1][0][0], cube[0][1][1][0], cube[0][1][2][0]] = tmp[3]
                [cube[1][1][0][0], cube[1][1][1][0], cube[1][1][2][0]] = tmp[0]
                [cube[2][1][0][0], cube[2][1][1][0], cube[2][1][2][0]] = tmp[1]
                [cube[3][1][0][0], cube[3][1][1][0], cube[3][1][2][0]] = tmp[2]
            else:
                [cube[0][1][0][0], cube[0][1][1][0], cube[0][1][2][0]] = tmp[1]
                [cube[1][1][0][0], cube[1][1][1][0], cube[1][1][2][0]] = tmp[2]
                [cube[2][1][0][0], cube[2][1][1][0], cube[2][1][2][0]] = tmp[3]
                [cube[3][1][0][0], cube[3][1][1][0], cube[3][1][2][0]] = tmp[0]
            left_side = cube[1][0]
            cube[1][0] = self_roate(left_side,direction)

        if side == 'R':
            # B,U,F,D
            tmp = [[cube[0][1][0][2], cube[0][1][1][2], cube[0][1][2][2]],
                   [cube[1][1][0][2], cube[1][1][1][2], cube[1][1][2][2]],
                   [cube[2][1][0][2], cube[2][1][1][2], cube[2][1][2][2]],
                   [cube[3][1][0][2], cube[3][1][1][2], cube[3][1][2][2]]]
            if direction == '+':
                [cube[0][1][0][2], cube[0][1][1][2], cube[0][1][2][2]] = tmp[1]
                [cube[1][1][0][2], cube[1][1][1][2], cube[1][1][2][2]] = tmp[2]
                [cube[2][1][0][2], cube[2][1][1][2], cube[2][1][2][2]] = tmp[3]
                [cube[3][1][0][2], cube[3][1][1][2], cube[3][1][2][2]] = tmp[0]
            else:
                [cube[0][1][0][2], cube[0][1][1][2], cube[0][1][2][2]] = tmp[3]
                [cube[1][1][0][2], cube[1][1][1][2], cube[1][1][2][2]] = tmp[0]
                [cube[2][1][0][2], cube[2][1][1][2], cube[2][1][2][2]] = tmp[1]
                [cube[3][1][0][2], cube[3][1][1][2], cube[3][1][2][2]] = tmp[2]
            right_side = cube[1][2]
            cube[1][2] = self_roate(right_side, direction)

        if side == 'F':
            # U,L,D,R
            tmp = [cube[1][1][2],cube[1][0][2],cube[3][1][0],cube[1][2][2]]
            if direction == '+':
                cube[1][1][2] = tmp[1]
                cube[1][0][2] = list(reversed(tmp[2]))
                cube[3][1][0] = list(reversed(tmp[3]))
                cube[1][2][2] = tmp[0]
            else:
                cube[1][1][2] = tmp[3]
                cube[1][0][2] = tmp[0]
                cube[3][1][0] = list(reversed(tmp[1]))
                cube[1][2][2] = list(reversed(tmp[2]))
            front_side = cube[2][1]
            cube[2][1] = self_roate(front_side,direction)

        if side == 'B':
            # U,L,D,R
            tmp = [cube[1][1][0], cube[1][0][0], cube[3][1][2], cube[1][2][0]]
            if direction == '+':
                cube[1][1][0] = tmp[3]
                cube[1][0][0] = tmp[0]
                cube[3][1][2] = list(reversed(tmp[1]))
                cube[1][2][0] = list(reversed(tmp[2]))
            else:
                cube[1][1][0] = tmp[1]
                cube[1][0][0] = list(reversed(tmp[2]))
                cube[3][1][2] = list(reversed(tmp[3]))
                cube[1][2][0] = tmp[0]
            back_side = cube[0][1]
            cube[0][1] = self_roate(back_side,direction)

    for text in arr:
        rotate(text[0],text[1])
        # print(_,text[0],text[1],'-----------------------')
        # for i in range(4):
        #     print(cube[i])


    for i in range(3):
        ans = ''
        for j in range(3):
            ans += cube[1][1][i][j]
        print(ans)

