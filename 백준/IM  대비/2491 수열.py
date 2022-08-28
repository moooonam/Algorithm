N = int(input())
arr = list(map(int, input().split()))
cnt_big = 1
maxleng_big =1
cnt_small = 1
maxleng_small = 1
for i in range(N-1):
    if arr[i] <= arr[i+1]:
        cnt_big += 1
        if cnt_big > maxleng_big:
            maxleng_big = cnt_big
    else:
        cnt_big=1
for i in range(N-1):
    if arr[i] >= arr[i+1]:
        cnt_small += 1
        if cnt_small > maxleng_small:
            maxleng_small = cnt_small
    else:
        cnt_small=1
if maxleng_small>maxleng_big:
    ans = maxleng_small
else:
    ans = maxleng_big
print(ans)



