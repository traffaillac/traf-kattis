N = int(input())
S = [input() for _ in range(N)]
fol = [-1] * N
last = list(range(N))
a = 0 # corner case: N=1
for _ in range(N - 1):
	a, b = (int(i)-1 for i in input().split())
	fol[last[a]] = b
	last[a] = last[b]
while a >= 0:
	print(S[a], end="")
	a = fol[a]
print()
