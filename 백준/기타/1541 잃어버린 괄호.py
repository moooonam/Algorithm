equation = input()
split_by_minus = equation.split('-')
for i in range(len(split_by_minus)):
    if "+" in split_by_minus[i]:
        split_by_minus[i] = sum(map(int, split_by_minus[i].split('+')))
ans = int(split_by_minus[0])
if len(split_by_minus) > 1:
    for i in range(1,len(split_by_minus)):
        ans -= int(split_by_minus[i])
print(ans)