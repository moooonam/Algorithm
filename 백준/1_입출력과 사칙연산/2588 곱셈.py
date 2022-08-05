#2588 곱셈
a = int(input())
b = int(input())
A = (b%10)*a
B = ((b//10)%10)*a
C = (b//100)*a
D = A+10*B+100*C
print(A)
print(B)
print(C)
print(D)