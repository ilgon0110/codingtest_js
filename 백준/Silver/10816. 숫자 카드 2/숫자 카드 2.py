from collections import Counter

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
my_cards = list(map(int, input().split()))

my_dict = Counter(cards)

arr = []
for v in my_cards:
    arr.append(my_dict[v])

print(' '.join(map(str, arr)))
