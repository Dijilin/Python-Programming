m=int(input("Enter a number:"))
s=0
while(m>0):
    dig=m%10
    s=s+dig
    m=m//10
print("The total sum of digits is:",s)
