N= int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr) [[2, 4], [11, 4], [15, 8], [4, 6], [5, 3], [8, 10], [13, 6]]
arr = sorted(arr)
max_hi = 0
a = 0#맥스위치
b = 0#맥스높이
max_index = 0
for i in range(N):
    if arr[i][1] > max_hi:
        max_hi = arr[i][1]
        a = arr[i][0]
        b = arr[i][1]
        max_index = i
for i in range(max_index):# 3
    x= arr[i][1]
    
