a, b = map(int, input().split())
N = int(input())
arr1 = [0, b] # 가로
arr2 = [0, a] # 세로
for i in range(N):
    c, d = map(int, input().split())
    if c ==0:
        arr1.append(d)
    else:
        arr2.append(d)
max1=0
max2=0
arr1= sorted(arr1)
arr2 = sorted(arr2)
for i in range(len(arr2)-1):
    x = arr2[i+1]-arr2[i] 
    if max1 < x:
        max1 = x
for i in range(len(arr1)-1):
    y = arr1[i+1]-arr1[i] 
    if max2 < y:
        max2 = y
print(max1*max2)