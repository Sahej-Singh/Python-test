# Python program to display all the prime numbers within an interval

# change the values of lower and upper for a different result
a = int(input("enter lower bound "))
b = int(input("enter upper bound "))

# uncomment the following lines to take input from the user
#lower = int(input("Enter lower range: "))
#upper = int(input("Enter upper range: "))

print("Prime numbers between",a,"and",b,"are:")

for num in range(a,b + 1):
   # prime numbers are greater than 1
   
       for i in range(2,num):
               if (num % i) == 0:
               break
       else:
           print(num)