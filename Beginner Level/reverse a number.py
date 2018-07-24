d=int(input("Enter number: "))
rev=0
while(d>0):
    dig=d%10
    rev=rev*10+dig
    d=d//10
print("Reverse of the number:",rev)
