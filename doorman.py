X = int(input())
d = 0
for n, c in enumerate(input()):
	d += 1 if c=='M' else -1
	if abs(d)>X+1:
		print(n-1)
		exit()
print(n+(abs(d)<=X)) # this condition is actually ignored in test samples