N, K = map(int,input().split())
arr = list(map(int, input().split()))
first_sum =0
for i in range(K):
    first_sum+=arr[i]
max_sum = first_sum
for j in range(N-K):
    first_sum-=arr[j]
    first_sum+=arr[j+K]
    if first_sum>max_sum:
        max_sum=first_sum
print(max_sum)

# for i in range(N-K+1):
#     sub_sum=0
#     for j in range(i, i+K):
#         sub_sum+=arr[j]
#     if sub_sum > max_sum:
#         max_sum=sub_sum
# print(max_sum)
# 이렇게 하면 시간초과가 떠..
