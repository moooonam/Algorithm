
N = int(input())
count = 1
num = 1600
if N==1:
    print(666)
else:
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
# 왜 내껀 안될가


# 구글링 답
# N = int(input())
# movie = 666
# while N:
#     if "666" in str(movie):
#         N -= 1
#     movie += 1
# print(movie - 1)