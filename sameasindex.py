a=int(input())
b=list(map(int,input().split(None,a)[:a]))
a=[]
for i in range(len(b)):
    if b[i]==i:
        
        print(b[i],end=" ")
