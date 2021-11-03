c1, c2, c3 = True, False, False
for move in input():
	if move == 'A':
		c1, c2 = c2, c1
	elif move == 'B':
		c2, c3 = c3, c2
	else:
		c1, c3 = c3, c1
print(1 if c1 else 2 if c2 else 3)
