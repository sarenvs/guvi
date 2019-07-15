
A,B=map(int,input().split())
C=list(map(int,input().split()))
pr=list(map(int,input().split()))
qr=[]
ar=0
for i in range(A):
    x=pr[i]/C[i]
    qr.append(x)
while B>=0 and len(qr)>0:
    mindex=qr.index(max(qr))
    if B>=C[mindex]:
        ar=ar+pr[mindex]
        B=B-C[mindex]
    C.pop(mindex)
    pr.pop(mindex)
    qr.pop(mindex)
print(ar)
