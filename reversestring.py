a=input()
a=a.split(" ")


b=""
for i in a:
    if i!="":
       v=list(i)
       v=v[::-1]
       b=b+"".join(v)
       b=b+" "      
    
print(b)
