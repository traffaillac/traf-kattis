for _ in range(int(input())):
	K, N = map(int, input().split())
	p, q = 1, 1
	for b in f"{N:b}"[1:]:
		if int(b):
			p += q
		else:
			q += p
	print(K, f"{p}/{q}")