try :
  a=int(input())
  b=int(input())
  if a%2==0:
    for i in range(a,b-1,2):
      print(i+1)
  else :
    for i in range(a,b-2,2) :
      print(i+2)
except :
print ("Invalid input")
