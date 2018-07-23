d=raw_input("Enter first string:")
b=raw_input("Enter second string:")
count1=0
count2=0
for i in d:
      count1=count1+1
for j in b:
      count2=count2+1
if(count1<count2):
      print("Larger string is:")
      print(b)
elif(count1==count2):
      print("Both strings are equal.")
      print(d)
else:
      print("Larger string is:")
      print(d)
