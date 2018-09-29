#Program to do what dad said.
a =[]
b = input("Enter no. ")
while b != 'q':
 b = input("Enter no. ")
 if b == 'q':
  break
 a.append(b)
e = []
for i in a:
 if int(i)%3 != 0:
  e.append(int(i))
print(sum(e))  
