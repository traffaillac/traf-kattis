P = [0] + [int(p)*(i+1) for i, p in enumerate(input().split())]
N = [0]*100
for _ in range(3):
	for t in range(*map(int, input().split())):
		N[t] += 1
print(sum(P[n] for n in N))