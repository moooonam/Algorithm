T = int(input())
for tc in range(1, T+1):
    stack=[]
    ans = ""
    my_str = input()
    for i in range(len(my_str)):
        if my_str[i] == "(":
            stack.append(my_str[i])
        elif my_str[i] == ")":
            if len(stack) == 0:
                ans = "NO"
                break 
            stack.pop(-1)
        if i == len(my_str)-1 and len(stack) == 0:
            ans = "YES"
        else:
            ans = "NO"

    print(ans)
