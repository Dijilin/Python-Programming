a = int(input('How many numbers: '))
total_sum = 0
 
for n in range(a):
    numbers = float(input('Enter number : '))
    total_sum += numbers
 
avg = total_sum/a
print('Average of ', a, ' numbers is :', avg)
