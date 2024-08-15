while True:
	n, m = map(int, input().split())
	if n==0: break
	D = sorted(int(input()) for _ in range(n))
	H = sorted(int(input()) for _ in range(m))
	k = 0
	c = 0
	for d in D:
		while k<len(H) and H[k]<d:
			k += 1
		if k==len(H):
			print("Loowater is doomed!")
			break
		c += H[k]
		k += 1
	else:
		print(c)