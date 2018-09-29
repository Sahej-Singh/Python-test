# Collatz Sequence
a = int(input("Enter no.: "))
while a != 1:
 if a%2 == 0:
  print(int(a))
  a = a/2
 else:
  print(int(a))
  a = 3*a + 1
print(1)