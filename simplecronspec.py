def F(t, n):
	if t=='*':
		return [*range(n)]
	else:
		f = []
		for r in t.split(','):
			a, *b = map(int, r.split('-'))
			if b:
				f.extend([*range(a, b[0]+1)])
			else:
				f.append(a)
		return f

J = [0] * 86400
for _ in range(int(input())):
	h, m, s = input().split()
	H = F(h, 24)
	M = F(m, 60)
	S = F(s, 60)
	for h in H:
		for m in M:
			for s in S:
				J[h*3600+m*60+s] += 1
print(86400-J.count(0), sum(J))