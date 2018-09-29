#Program to find te sum of digits of a no.
a = input("enter no.: ")
b = int(len(a))
c1 = 0
for i in range(0,b):
 c2 = int(a[i])
 c3 = c1 + c2
 c1 = c3
print(c3)