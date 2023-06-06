N, M = map(int, input().split())
arr = list(map(int, input().split()))
sum_list=[0]
sub_sum = 0
for i in arr:
    sub_sum+=i
    sum_list.append(sub_sum)

for _ in range(M):
    a, b = map(int, input().split())
    total = sum_list[b]-sum_list[a-1] 
    print(total)