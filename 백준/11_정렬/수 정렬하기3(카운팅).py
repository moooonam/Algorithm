N = int(input())
my_list = []
for i in range(N):
    my_list.append(int(input()))
counting_arr = [0]*10001
for i in my_list:
    counting_arr[i]+=1
for i in range(10000):
    counting_arr[i+1] += counting_arr[i]
output_arr = [-1]*len(my_list)
for i in my_list:
    output_arr[counting_arr[i]-1] = i
    counting_arr[i] -=1
for p in range(len(output_arr)):
    print(output_arr[p])
# 메모리 초과 뜸..