N = int(input())
my_list = []
for i in range(N):
    my_list.append(int(input()))
for p in range(N-1, 0, -1):
    for q in range(p):
        if my_list[q] > my_list[q+1]:
            my_list[q], my_list[q+1] = my_list[q+1], my_list[q]
for x in range(N):
    print(my_list[x])