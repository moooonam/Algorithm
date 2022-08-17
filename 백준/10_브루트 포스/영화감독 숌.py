
N = int(input())
count = 1
num = 1600
while N != 666:
    num += 1
    num_list = list(map(int, str(num)))
    for i in range(len(num_list)-2):
        if num_list[i]==6 and num_list[i+1]==6 and num_list[i+2]==6:
            count+=1
            break
    if count == N:
        break
print(num)    

