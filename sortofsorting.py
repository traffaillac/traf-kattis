for i in range(500):
	n = int(input())
	if n == 0: break
	if i > 0: print()
	names = [input() for _ in range(n)]
	for n in sorted(names, key=lambda n: n[:2]):
		print(n)