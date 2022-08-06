T = int(input())
my_list=[]
for i in range(T):
    a, b = input().split()
    a= int(a)
    for j in range(len(b)):
        print(b[j]*a, end='')
    print()
