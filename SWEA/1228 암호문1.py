for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    M = int(input())
    command = list(map(str, input().split())) 
    for i in range(len(command)):
        if command[i] == "I":
            x = int(command[i+1])
            y = int(command[i+2])
            for j in range(i+3, i+3+y):
                if x> 10 :
                    break
                arr.insert(x, int(command[j]))
                x+=1
    print(f"#{tc}", end=" ")
    for _ in range(10):
        print(arr[_], end=" ")
