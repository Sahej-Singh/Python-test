def recur_factorial(n):
  return n*recur_factorial(n-1)

a = int(input("enter"))       
print(recur_factorial(a))	   
	   
