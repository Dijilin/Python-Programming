 m=int(input('Enter the number '))
factor=0
for i in range(1,m):
  if m%i==0:
    factor=i
if factor>1:
  print ("The number is a composite number!")
else:
  print ("This is not a composite number!")
