#given number is prime number or not

num=int(input('enter a number'))

if num>1:
    for i in range(2,num//2):
      if num%i == 0:
          print('%d is not a prime number' %num)
          break
    else:
     print('%d is a prime number' %num)
else:
    print('%d is not a prime number')


'''
expected output

enter a number47
47 is a prime number
'''
