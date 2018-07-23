str=input('enter the string')
count=0

for i in range(len(str)):
  if str[i].isdigit():
    count=count+1
  else:
    count=count
print(count)
