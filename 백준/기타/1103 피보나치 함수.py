T = int(input())
arr = [[1,0],[0,1]]
for i in range(2, 41):
    new_arr = [arr[i-1][0]+arr[i-2][0], arr[i-1][1]+arr[i-2][1]]
    arr.append(new_arr)
for _ in range(T):
    N = int(input())
    print(arr[N][0], end=" ")
    print(arr[N][1])
    