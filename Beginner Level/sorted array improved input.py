a=[]
k=int(input("value"))
for i in range(1,k+1):
 c=int(input("numbers"))
 a.append(c)
 a.sort()
print(a)
print(a[k//2])
