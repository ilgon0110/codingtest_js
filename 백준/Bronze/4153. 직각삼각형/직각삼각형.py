while (True):
    arr = sorted(list(map(int, input().split())))
    if arr[0] == 0:
        break
    [a, b, c] = arr
    if a*a + b*b == c*c:
        print('right')
    else:
        print('wrong')
