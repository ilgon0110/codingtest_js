result = int(input())
for _ in range(2):
    result *= int(input())

for i in range(10):
    print(str(result).count(str(i)))
