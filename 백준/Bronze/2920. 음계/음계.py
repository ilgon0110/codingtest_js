arr = list(map(str, input().split()))
inputText = ''.join(arr)

if inputText == '12345678':
    print('ascending')
elif inputText == '87654321':
    print('descending')
else:
    print('mixed')
