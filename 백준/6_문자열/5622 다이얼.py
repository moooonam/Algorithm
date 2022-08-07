a = input()
c=0
for i in a:
    if 65<=ord(i)<=67:
        c+=3
    elif 68<=ord(i)<=70:
        c+=4
    elif 71<=ord(i)<=73:
        c+=5
    elif 74<=ord(i)<=76:
        c+=6
    elif 77<=ord(i)<=79:
        c+=7
    elif 80<=ord(i)<=83:
        c+=8
    elif 84<=ord(i)<=86:
        c+=9
    else: 
        c+=10
print(c)
