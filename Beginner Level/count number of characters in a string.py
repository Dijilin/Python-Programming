b=input("enter the value:")
a=len(b)
while True:
    if " " in b:
        a=a-1
        if(" " not in b):
          break
        print(a)
        break
    else:
        print(a)
        break     
