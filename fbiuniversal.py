for _ in range(int(input())):
	K, U = input().split()
	for c, r in zip("BGIOQSUYZ","8C1005VV2"):
		U = U.replace(c, r)
	D = ["0123456789ACDEFHJKLMNPRTVWX".index(u) for u in U]
	print(K, "Invalid" if D[8]!=sum(m*d for m, d in zip((2,4,5,7,8,10,11,13),D))%27 else sum(d*27**(7-i) for i, d in enumerate(D[:-1])))