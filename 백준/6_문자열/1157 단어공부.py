a =input()
a = a.upper()
b = list(set(a))
my_list =[]
for i in b:
    my_list.append(a.count(i))
m = max(my_list)
if my_list.count(m)>1:
    print('?')
else:
    for i in a:
        if a.count(i)==m:
            print(i)
            break