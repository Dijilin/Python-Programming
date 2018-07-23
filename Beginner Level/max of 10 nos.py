d=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    d.append(b)
d.sort()
print("Largest element is:",d[n-1])
