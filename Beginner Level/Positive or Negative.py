def main():
a=int(input())
if(1<=a<=100000):
 if(a<0):
    print("negative")
 elif(a>0):
    print("positive")
 elif(a==0):
    print("zero")
 else:
    print("Not Valid")
