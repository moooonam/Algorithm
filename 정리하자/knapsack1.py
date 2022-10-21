# arr[i][s] 는 배낭 크기가 s일 때, i개의 물건을 넣었을 때, 가능한 최대 가치를 의미한다.

def knapsack1(capacity, n):
    arr = [[0 for _ in range(capacity+1)] for _ in range(n+1)]
    for i in range(1, n+1): # 물건 갯수 하나씩 증가
        for s in range(1, capacity+1): #배낭크기 하나씩 증가
            if size[i-1] > s: # 물건의 부피가 배낭크기 s보다 크면
                arr[i][s] = arr[i-1][s] # 
            else: # 물건의 부피가 s보다 작거나 같으면
                arr[i][s] = max(value[i-1] + arr[i-1][s-size[i-1]], arr[i-1][s])
            # 지금 가치랑 가방 꽉채울수 있는 가치 vs 그냥 전에꺼까지랑 비교
    return arr[n][capacity]
size = [6, 4, 3, 5]
value = [13, 8, 6, 12]
print(knapsack1(7, 4))