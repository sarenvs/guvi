a=int(input())
b=list(map(int,input().split(None,a)[:a]))
b.sort(key=None,reverse=True)
if b.count(0)==len(b):
    print(0)
else:
    print("".join(map(str,b)))
