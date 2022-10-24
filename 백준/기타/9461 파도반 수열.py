arr = [1,1,1,2,2,3,4,5,7,9]
for i in range(9, 101):
    arr.append(arr[i]+arr[i-4])
T = int(input())
for tc in range(T):
    print(arr[int(input())-1])