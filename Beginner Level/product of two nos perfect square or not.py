import math
d=int(input("Enter the number:"))
a=int(input("Enter the number:"))
y=a*d
print(y)
y_sqrt=y**0.5
if(y_sqrt==int(math.sqrt(y))):
 print("Yes")
else:
 print("No")
