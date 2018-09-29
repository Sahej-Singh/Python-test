a = int(input("enter first no."))
b = int(input("enter second no."))
i = 1
if a > b:
 while i <= b:
  if (a*i)%b != 0:
   i += 1   
  else:
   print(a*i) 
   break   
elif a==b:
 print(a)
else:
 while i <= a:
  if (b*i)%a != 0:
   i += 1   
  else:
   print(b*i) 
   break