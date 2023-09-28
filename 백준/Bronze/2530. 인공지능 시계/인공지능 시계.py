import sys
# sys.stdin = open("input.txt", "r")

[time, minute, second] = list(map(int, input().split()))
spendTime = int(input())

a = time*(60*60) + minute*60 + second + spendTime

aTime = a//3600
aMinute = (a - aTime*3600)//60
aSecond = a - aTime*60*60 - aMinute*60

if aTime >= 24:
    aTime = aTime % 24
print(aTime, aMinute, aSecond)
