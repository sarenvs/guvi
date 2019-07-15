x,y=map(int,input().split())
a=list(map(int,input().split(None,x)[:x]))
f=[]
for i in range(y):
    d,g=map(int,input().split())
    f.append(sum(a[d-1:g]))
for i in f:
    print(i)
