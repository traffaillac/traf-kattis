N, *V = map(int, input().split())
last = []
while len(V) > 0 and any(V):
	last.append(V[-1])
	V = [V[i + 1] - V[i] for i in range(len(V) - 1)]
print(len(last) - 1, sum(last))
