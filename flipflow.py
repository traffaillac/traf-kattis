t, s, n = map(int, input().split())
l, u, w = s, 0, 0
for a in map(int, input().split()):
	l = min(l+a-w, s)
	u = s-l
	w = a
	l, u = u, l
l = min(l+t-w, s)
u = s-l
print(u)