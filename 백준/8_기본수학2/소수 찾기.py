N= int(input())
my_list=list(map(int,(input().split())))
count=0
for i in my_list:
    if i==2:
        count+=1
    elif i>2:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            count+=1
print(count)