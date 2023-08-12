n, i, c = input(), 0, ''
while i < len(n):
	x = n[i]
	c += x
	while i < len(n) and n[i]==x: i += 1
print(c)
