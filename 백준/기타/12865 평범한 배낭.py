# 평범하지만 전혀 평범하지 않아....
# 배낭 알고리즘 구글링....
N, K = map(int, input().split()) # N 물품수 K 용량
my_bag = []
for _ in range(N):
    w, v =(map(int, input().split())) # w : 무게, v : 가치
    my_bag.append((w, v))
arr = [[0 for _ in range(K + 1)] for _ in range(N + 1)] # arr[num][size] 배낭의 크기가 size 일때 num개의 물건을 넣었을 때 최대 가치
for num in range(1, N+1): # 물건 갯수 하나씩 추가
    for size in range(1, K+1): # 용량 증가
        if my_bag[num-1][0] > size:
            arr[num][size] = arr[num-1][size]
        else:
            arr[num][size] = max((arr[num-1][size]),(my_bag[num-1][1]+ arr[num-1][size-my_bag[num-1][0]]))
print(arr[N][K])
# print(arr)