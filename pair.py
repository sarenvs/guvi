a=int(input())
b=[]
c=0
for i in range(0,a):
    b.append(i)
for j in range(len(b)):
    for k in range(j+1,len(b)):
        c+=1
print(c)
