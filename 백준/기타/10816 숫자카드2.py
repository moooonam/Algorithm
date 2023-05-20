N = int(input())
cards = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

card_counts = {}

for card in cards:
    if card in card_counts:
        card_counts[card] += 1
    else:
        card_counts[card] = 1
# print(card_counts)
for target in targets:
    ans = card_counts.get(target, 0)
    print(ans, end=" ")
