def pal_find(c):
	x = c + 1
	while x > c:
		s = str(x)
		if s == s[::-1]:
			return(x)
			break
		x += 1
for i in range(int(input("Enter value: "))):
	print(pal_find(int(input("value"))))

			