s = input("Enter string: ")
b = len(s)
c = list(s)
a = 0
for i in range(0,b-2):
 if c[i] == 'b' and c[i+1] == 'o' and c[i+2] == 'b':
  a += 1
print(a)