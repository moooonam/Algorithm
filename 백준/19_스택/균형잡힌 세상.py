
while True:
    str = input()
    if str == ".":
        break
    stack = []
    ans = "yes"
    for i in str:
        if i == "(":
            stack.append(i)
        elif i == "[":
            stack.append(i)
        elif i == ")":
            if len(stack) == 0 or stack[-1] == "[":
                ans = "no"
                break
            else:
                stack.pop(-1)
        elif i == "]":
            if len(stack) == 0 or stack[-1] == "(":
                ans = "no"
                break
            else:
                stack.pop(-1)
    if len(stack) > 0:
        ans = "no"
    print(ans)
         