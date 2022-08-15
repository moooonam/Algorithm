# def combination(arr, n):    
#     result = []    
#     if n == 0:        
#         return [[]]        
#     for i in range(len(arr)):        
#         elem = arr[i]        
#         for rest in combination(arr[i + 1:], n - 1):           
#             result.append([elem] + rest)   
#     return result 
#      #print(combination([0,1,2,3], 2))

#      # [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]
    #순열 퍼옴

# 순열 이용해도 할수있고 그냥 합으로도 할수 있는데 그냥합 하는거 반복문 돌릴 범위 생각을 떠올리지 못해서 검색을 해버림...
N, M = map(int, input().split())
mylist = list(map(int, input().split()))
my_max = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if my_max<mylist[i]+mylist[j]+mylist[k]<= M:
                my_max=mylist[i]+mylist[j]+mylist[k]
print(my_max)
