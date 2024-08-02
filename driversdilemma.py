C, X, M = map(float, input().split())
r = "NO"
for _ in range(6):
	s, e = input().split()
	t = M/int(s)
	f = M/float(e)+X*t
	if f<=C/2:
		r = f"YES {s}"
print(r)