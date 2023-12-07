while (True):
    text = str(input())
    if text == '0':
        break
    tmp = ''.join(reversed(list(text)))
    if text == tmp:
        print('yes')
    else:
        print('no')
