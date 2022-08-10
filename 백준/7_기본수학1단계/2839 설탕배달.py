N= int(input())
a = int(N//5)
b=True
for i in range(a,-1,-1):
    for j in range(1700):
        if 5*i+3*j==N:
            print(i+j)
            b =False
            break
    if b==False:
        break
if b==True:
    print(-1)
        
   

