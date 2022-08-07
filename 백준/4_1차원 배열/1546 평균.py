n = int(input())
my_list =list (map(int, input().split()))
M = max(my_list)
re_list=[]
for i in my_list:
    re_list.append((i/M)*100)
m = sum(re_list)/n
print(m)