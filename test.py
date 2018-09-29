a = int(input("enter lower bound"))
b = int(input("enter upper bound"))
i = 1
for num in range(a,b + 1):
 while i <= num:
  if num%i == 0:
   i += 1
  else:
   print(num)    
   i += 1
   break