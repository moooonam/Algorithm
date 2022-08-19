N = input()
arr = []
for i in range(len(N)):
    arr.append(N[i])
map(int, arr)
arr.sort(reverse=True)
for k in range(len(arr)):
    print(arr[k], end="")