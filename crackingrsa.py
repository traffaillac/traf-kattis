for _ in range(int(input())):
	n, e = map(int, input().split())
	for p in range(2, n):
		if n % p == 0:
			q = n // p
			break
	totient = (p-1) * (q-1)
	for d in range(1, totient):
		if d*e%totient == 1:
			print(d)
			break
