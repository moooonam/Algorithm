for tc in range(1,11):
    N = int(input())
    array = [list(map(int, input().split())) for __ in range(100)]
    sum_list = []
    for i in range(100):
        sum_list.append(sum(array[i]))
        part_sum1 = 0
        part_sum2 = 0
        part_sum3 = 0
        for j in range(100):
            if i == j:
                part_sum2+=array[i][j]
            if i + j == 99 and i != j:
                part_sum3+= array[i][j]
            part_sum1 += array[j][i]
        sum_list.append(part_sum1)
        sum_list.append(part_sum2)
        sum_list.append(part_sum3)
    print(f"#{tc} {max(sum_list)}")

