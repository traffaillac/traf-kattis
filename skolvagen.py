C = [0, 1]
for c in input():
	if c=='S':
		C[1] = min(C[0]+1,C[1]+1)
	elif c=='N':
		C[0] = min(C[0]+1,C[1]+1)
	else:
		C[0] += 1
		C[1] += 1
print(C[0])