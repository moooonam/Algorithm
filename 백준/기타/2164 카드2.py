from collections import deque

N = int(input())
cards = deque(range(1,N+1))
ans = 0
while len(cards) > 1:
    del cards[0] 
    first_card = cards.popleft()
    cards.append(first_card)

ans = cards[0]
print(ans)
