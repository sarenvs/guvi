a=list(input())
b=[]
for i in range(len(a)-1):
    if (a[i] not in b) and(a[i]!=a[i+1]):
        b.append(a[i])
print(len(b))
