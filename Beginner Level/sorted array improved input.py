l=[]
k=int(input("value"))
for i in range(1,k+1):
 c=int(input("numbers"))
 l.append(c)
 l.sort()
print(l)
print(l[k//2])
