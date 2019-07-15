x,y=map(int,input().split())
a=list(map(int,input().split(None,x)[:x]))
f=[]
for i in range(y):
    d,g=map(int,input().split())
    f.append(sum(a[d:g+1]))
for i in f:
    print(i)
