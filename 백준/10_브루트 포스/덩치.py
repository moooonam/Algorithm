# 구글링 힌트 얻음...
T = int(input())
my_list = []
rank = []
for i in range(T):
    my_list.append(list(map(int, input().split())))
for p in range(T):
    cnt = 1
    for q in range(T):
        if my_list[p][0] < my_list[q][0] and my_list[p][1] < my_list[q][1]:
            cnt += 1
    rank.append(cnt)
for i in range(T):
    print(rank[i], end=" ")