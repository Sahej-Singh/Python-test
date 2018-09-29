#Python program to find the prime factors of an integer.
def factor(n):
 b = int(n)
 d = []
 for i in range(1,b+1):
  if int(n)%i == 0:
   d.append(i)
 return(d)  
a = input("enter no.: ")
print(factor(a))

