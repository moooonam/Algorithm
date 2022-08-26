N, K = map(int, input().split())
arr1 = [0]*7 #남
arr2 = [0]*7 #여
cnt = 0
for i in range(N):
    a, b = map(int, input().split())
    if a == 0:
        arr1[b] += 1
    else:
        arr2[b] += 1
for j in range(7):
    if arr1[j]%K ==0:
        cnt += arr1[j]//K
    else:
        cnt += arr1[j]//K +1
    if arr2[j]%K ==0:
        cnt += arr2[j]//K
    else:
        cnt += arr2[j]//K +1
print(cnt)        
    