# 팩토리얼을 for 말고 재귀로 한번 해보자잉
def fac(n):
    if n==0:
        return 1
    return fac(n-1)*n            
print(fac(int(input())))