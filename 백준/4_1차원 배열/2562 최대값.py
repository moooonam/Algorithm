my_list=[]
for i in range(9):
    my_list.append(int(input()))
print(max(my_list))
c=1
for i in my_list:
    if i == max(my_list):
        print(c)
    c+=1