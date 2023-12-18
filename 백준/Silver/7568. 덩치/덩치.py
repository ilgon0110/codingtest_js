N = int(input())
arr = []
ans = []
for _ in range(N):
    [x, y] = list(map(int, input().split()))
    arr.append((x, y))

for i in range(len(arr)):
    [myTall, myWeight] = arr[i]
    cnt = 0
    for j in range(len(arr)):
        [targetTall, targetWeight] = arr[j]
        if targetTall > myTall and targetWeight > myWeight:
            cnt += 1
    ans.append(cnt+1)

answer = ''
for i in range(len(ans)):
    if i != (len(ans)-1):
        answer += str(ans[i]) + ' '
    else:
        answer += str(ans[i])

print(answer)
