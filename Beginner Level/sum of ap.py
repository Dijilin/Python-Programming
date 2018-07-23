def fib(m):
	if m==1 or m==0:
		return(m)
	else :
		return fib(m-1)+fib(m-2)
try:
	m=int(input())
	sum=0
	for i in range(0,m):
		print(fib(i))
except:
print('invalid')
