#Program to accept 3 digit no.s and print all possible combinations.
a = input("Enter a number with 3 digits only.")
while len(a) != 3:
 print("Please enter a 3 digit number")
 a = input("Enter a number with 3 digits only.")
 if len(a) == 3:
   break
d = [a[0], a[1], a[2]]
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if(i!=j & j!=k & k!=i):
                print(d[i],d[j],d[k])
 