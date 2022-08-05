N,X = map(int, input().split())
my_list=list(map(int, input().split()))

re = []
for i in my_list:
    if i<X:
        re.append(i)
b = ' '.join(re)
print(b)
