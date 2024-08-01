def sieve(n:int):
	primes = [True]*n
	primes[0] = primes[1] = False
	for i in range(2, int(n**.5)+1):
		if primes[i]:
			for j in range(i*i, n, i):
				primes[j] = False
	return primes

P = sieve(10001)
for _ in range(int(input())):
	K, M = map(int, input().split())
	S = set()
	m = M
	while m!=1 and m not in S:
		S.add(m)
		m = sum(int(d)**2 for d in str(m))
	print(K, M, "YES" if m==1 and P[M] else "NO")