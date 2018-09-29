list = []
a = input("Enter input or press q to quit: ")
list.append(a)
while a != 'q': 
 a = input("Enter input or press q to quit: ")
 if a == 'q':
  break
 list.append(a)
even = []
odd = []
for i in list:
 if int(i)%2 == 0:
  even.append(int(i))
 elif int(i)%2 != 0:
  odd.append(int(i))
print("Even inputs: ", even)
print("odd inputs: ", odd)
print("Sum of even inputs:", sum(even))
b = len(odd)
d = 1
e = 1
for i in range(0,b):
  c = odd[i]*d
  e = c*e 
print("Product of odd inputs:", e)