while True:
    length_list = list(map(int, input().split()))
    if sum(length_list) == 0:
        break
    if length_list[0]**2 == length_list[1]**2 + length_list[2]**2 or length_list[1]**2 == length_list[0]**2 + length_list[2]**2 or length_list[2]**2 == length_list[1]**2 + length_list[0]**2 :
        print("right")
    else:
        print("wrong")