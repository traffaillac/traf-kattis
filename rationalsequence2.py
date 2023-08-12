for _ in range(int(input())):
	K, pq = input().split()
	p, q = map(int, pq.split('/'))
	r, c = 0, 0
	while not p==q==1:
		c |= int(p>q)<<r
		r += 1
		if p>q:
			p -= q
		else:
			q -= p
	print(K, 2**r+c)