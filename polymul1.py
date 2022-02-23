# (a0 + a1 x^1 + a2 x^2) * (b0 + b1 x^1 + b2 x^2)

for _ in range(int(input())):
	na = int(input())
	a = list(map(int, input().split()))
	nb = int(input())
	b = list(map(int, input().split()))
	c = [0] * (na + nb + 1)
	for i, ai in enumerate(a):
		for j, bj in enumerate(b):
			c[i + j] += ai * bj
	print(na + nb)
	print(*c)
