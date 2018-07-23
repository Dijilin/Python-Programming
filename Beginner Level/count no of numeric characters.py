str=input('enter the string')
n=0

for i in range(len(str)):
  if str[i].isdigit():
    n=n+1
  else:
    n=n
print(n)
