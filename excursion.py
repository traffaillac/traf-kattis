i = 0 # index of first 1 in sorted list
j = 0 # index of first 2 in sorted list
swaps = 0
for k, c in enumerate(input()):
	if c == '0':
		swaps += k - i # swaps to put 0 at index i in list of size k
		i += 1
		j += 1
	elif c == '1':
		swaps += k - j # swaps to put 1 at index j in list of size k
		j += 1
print(swaps)
