a=input()
a=a.split(" ")
print(a)
b=""
for i in a:
    if i!="":
       v=list(i)
       v=v[::-1]
       b=b+"".join(v)+" "
print(b)
