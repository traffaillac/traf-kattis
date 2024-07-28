# Golfed afterwards though not kept ;)
def f(a):
	if type(P.setdefault(a,1))==int:
		return a
	else:
		P[a] = f(P[a])
		return P[a]
for _ in range(int(input())):
	F = int(input())
	P = {}
	for _ in range(F):
		a, b = map(f, input().split())
		if P[a] < P[b]:
			a, b = b, a
		if a != b:
			P[a] += P[b]
			P[b] = a
		print(P[a])