a=int(input())
b=list(map(int,input().split(None,a)[:a]))


c=b.sort(key=None,reverse=False)
if b.count(0)!=len(b):
    
     print("".join(map(str,b)))
else:
    print(0)
    

