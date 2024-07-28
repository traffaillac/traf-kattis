from math import ceil
for _ in range(int(input())):
	s = input()
	K = ceil(len(s)**.5)
	s += '*' * (K*K-len(s))
	print(''.join(s[r+(K-1-c)*K] for r in range(K) for c in range(K)).replace('*',''))