a=int(input())
d=[]
c=list(map(int,input().split(None,a)[:a]))
for i in c:
    b=c.count(i)
    print(b)
    if b>1 and (i not in  d):
        d.append(i)
if len(d)!=0:
    f=" ".join(map(str,d))
    print(f)
else:
    print("unique")
