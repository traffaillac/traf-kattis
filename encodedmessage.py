for _ in range(int(input())):
	s = input()
	n = int(len(s) ** .5)
	print(''.join(s[n-1-r+c*n] for r in range(n) for c in range(n)))
