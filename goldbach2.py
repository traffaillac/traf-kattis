def sieve(n:int):
	primes = [True]*n
	primes[0] = primes[1] = False
	for i in range(2, int(n**.5)+1):
		if primes[i]:
			for j in range(i*i, n, i):
				primes[j] = False
	return primes

P = sieve(32000)
for _ in range(int(input())):
	x = int(input())
	R = [f"{a}+{x-a}" for a in range(1, x//2+1) if P[a] and P[x-a]]
	print(f"{x} has {len(R)} representation(s)")
	print('\n'.join(R))
	print()
