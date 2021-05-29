#Reverse
n=int(input("Enter number"))
i=n
sum=0
while(n!=0):
    r=n%10
    sum=(sum*10)+r
    n=n//10
print("The Reverse of %d is %d" %(i,sum))

OUTPUT:
Enter number2345
The Reverse of 2345 is 5432
