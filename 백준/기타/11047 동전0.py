N, K = map(int, input().split())
coins = []
ans = 0
for _ in range(N):
    coins.append(int(input()))
for i in range(len(coins)):
    if K == 0:
        break
    if K // coins[len(coins)-1-i] > 0:
        ans += K // coins[len(coins)-1-i]
        K -= (K // coins[len(coins)-1-i])*coins[len(coins)-1-i]
print(ans)