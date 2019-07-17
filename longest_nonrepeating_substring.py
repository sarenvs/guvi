a=input()
B=''
C=[]
for i in a:
    if i not in C:
        B=B+i
        C.append(i)
    elif i in C:
        break
print(len(C))
