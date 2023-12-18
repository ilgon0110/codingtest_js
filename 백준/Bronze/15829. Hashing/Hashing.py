L = int(input())
text = str(input())

total = 0
for i in range(L):
    total += (ord(text[i])-96) * (31**i)
print(int(total % 1234567891))
