def subset(d,b):
    c=""
    for i in d:
        if i in b:
            continue
        else:
            return False
    return(True)

a,c=map(int,input().split())
b=list(map(int,input().split(None,a)[:a]))
d=list(map(int,input().split(None,c)[:c]))
print(subset(d,b))
    
