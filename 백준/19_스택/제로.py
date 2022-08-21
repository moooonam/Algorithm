N = int(input())
stack = []
for i in range(N):
    num = int(input())
    if num == 0:
        stack.pop(-1)
    else:
        stack.append(num)
print(sum(stack))