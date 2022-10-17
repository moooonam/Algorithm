# 구글링 힌트 얻음... dp 너무 어려워....ㅠㅠㅠㅠㅠㅠㅠㅠㅠ
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]
    for i in range(1, N):
        if i==1:
            arr[0][1] += arr[1][0]
            arr[1][1] += arr[0][0]

        else:
            arr[0][i] += max(arr[1][i-1], arr[1][i-2])
            arr[1][i] += max(arr[0][i-1], arr[0][i-2])
    print(max(arr[0][N-1], arr[1][N-1]))
