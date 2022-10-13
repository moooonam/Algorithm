# 구글에서 LIS라는 알고리즘을 가져옴...

N= int(input())
arr = list(map(int, input().split()))

# DP 테이블 1로 초기화
dp = [1] * N

for i in range(1, N):
    for j in range(0, i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# 가장 긴 증가하는 부분 수열의 길이값
result = max(dp)
print(result)
