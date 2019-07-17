import string
a=list(string.ascii_lowercase+string.ascii_uppercase)
b=input()
c=[]
for i in list(b):
    if (i in a) and (i not in c):
        c.append(i)

if len(c)>=26:
    print("yes")
else:
    print("no")
