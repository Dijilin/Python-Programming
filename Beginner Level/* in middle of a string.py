b=input("Enter any string:")
d=len(b)
l=list(b)
b=''
if d%2!=0:
	for i in range(d//2):
		b+=l[i]
	b+='*'
	j=d//2+1
else:
  for i in range(d//2):
    b+=l[i]
  b+='*'
  j=d//2+1
for i in range(j,d):
	b+=l[i]
print(b)
