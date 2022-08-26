nan = []
for i in range(9):
    nan.append(int(input()))
nansum = sum(nan)

ai=aj=0
for i in range(9):
    for j in range(i+1,9):
        if nansum-nan[i]-nan[j] == 100:
            ai = i 
            aj = j
            break
nan.pop(ai)
if ai <aj:
    nan.pop(aj-1)
else:
    nan.pop(aj)
ans = sorted(nan)
for i in range(7):
    print(ans[i])