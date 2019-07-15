a=int(input())
c=list(map(int,input().split(None,a)[:a]))
c.sort(key=None,reverse=True)

for i in c:
    print(i)
