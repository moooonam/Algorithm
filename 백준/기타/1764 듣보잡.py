N, M = map(int, input().split())
Non_listen = set()
Non_see = set()
for _ in range(N):
    Non_listen.add(input())
for _ in range(M):
    Non_see.add(input())
ans = sorted(Non_listen&Non_see)
print(len(ans))
for i in ans:
    print(i)
