import sys
import copy

input = sys.stdin.readline

N = int(input())
arr = list(map(int , input().split()))
cals = list(map(int,input().split()))
operators = []
tmp = ['+','-','*','/']

for i in range(4):
    for _ in range(cals[i]):
        operators.append(tmp[i])

visited = [0 for _ in range(len(operators))]
all_operators = []


def calculate(one,two,operator):
    if operator == '+':
        return one+two
    if operator == '-':
        return one-two
    if operator == '*':
        return one*two
    if operator == '/':
        if one < 0:
            return -(abs(one)//two)
        else:
            return one//two

answer = []


def recursive(L,tmp):
    if L == N-1:
        numbers = copy.deepcopy(arr)
        for i in range(N - 1):
            final = calculate(numbers[i], numbers[i + 1], tmp[i])
            numbers[i + 1] = final
        answer.append(numbers[-1])
        return
    else:
        for i in range(N-1):
            if visited[i] == 0:
                visited[i] = 1
                tmp.append(operators[i])
                recursive(L+1,tmp)
                tmp.pop()
                visited[i] = 0

recursive(0,[])

print(max(answer))
print(min(answer))



