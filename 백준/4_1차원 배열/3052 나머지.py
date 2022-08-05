#3502 나머지
my_list = []
for i in range(10):
    my_list.append(int(input()))
my_set =set() 
for i in my_list:
    my_set.add(i%42)
print(len(my_set))
