a=list(input())
b=[]
for i in range(len(a)-1):
    if (a[i] not in b) and(a[i]!=a[i+1]):
        b.append(a[i])
    if a[i+1] not in b:
        b.append(a[i+1])
    
print(len(b))

