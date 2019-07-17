n=input()
N=[]
for i in n:
    if i not in N:
        N.append(i)
        
    else:
        break
print(len(N))
