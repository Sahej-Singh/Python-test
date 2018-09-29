t = int(input("Enter value"))
test_inputs = []
for i in range(1,t+1):
	a = int(input("Enter value"))
	test_inputs.append(a)
print(test_inputs)
def pal_find(c):
	x = c + 1
	while x > c:
		s = str(x)
		if s == s[::-1]:
			return(x)
			break
		x += 1
for x in test_inputs:
	print(pal_find(int(x)))

			