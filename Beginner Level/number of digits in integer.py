N=int(input("Enter number:"))
count=0
while(N>0):
    count=count+1
    N=N//10
print("The number of digits in the number are:",count)
