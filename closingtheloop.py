N = int(input())
for n in range(N):
	S = int(input())
	B, R = [], []
	for rope in input().split():
		L = int(rope[:-1])
		(B if rope[-1]=='B' else R).append(L)
	B.sort(reverse=True)
	R.sort(reverse=True)
	s = min(len(B), len(R))
	print('Case #{}: {}'.format(n+1, sum(B[:s])+sum(R[:s])-2*s))
