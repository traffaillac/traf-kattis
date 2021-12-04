l, w, n, r = map(int, input().split())
cranes = [5] * 16
for _ in range(n):
	x, y = map(int, input().split())
	c0 = (2*x+l)**2 + 4*y**2 <= 4*r**2
	c1 = (2*x-l)**2 + 4*y**2 <= 4*r**2
	c2 = 4*x**2 + (2*y+w)**2 <= 4*r**2
	c3 = 4*x**2 + (2*y-w)**2 <= 4*r**2
	cranes[c0 | c1<<1 | c2<<2 | c3<<3] = 1
for _ in range(2):
	for i in range(16):
		if cranes[i] == 5: continue
		for j in range(16):
			if cranes[j] == 5: continue
			cranes[i | j] = min(cranes[i | j], cranes[i] + cranes[j])
print(cranes[15] if cranes[15]<5 else 'Impossible')
