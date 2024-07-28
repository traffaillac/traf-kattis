while True:
	n = int(input())
	if n==0: break
	M = {}
	for _ in range(n):
		n, *I = input().split()
		for i in I:
			M.setdefault(i, []).append(n)
	for i, N in sorted(M.items()):
		print(i, ' '.join(sorted(N)))
	print()