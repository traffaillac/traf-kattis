def fwht(a):
	"""In-place Fast Walsh–Hadamard Transform of array a."""
	h = 1
	while h < len(a):
		for i in range(0, len(a), h * 2):
			for j in range(i, i + h):
				x = a[j]
				y = a[j + h]
				a[j] = x + y
				a[j + h] = x - y
		h *= 2

for _ in range(int(input())):
	na = int(input())
	a = list(map(int, input().split()))
	nb = int(input())
	b = list(map(int, input().split()))
	target = 1 << (na + nb).bit_length()
	pad = target - na - nb - 1
	a += [0] * (nb + pad)
	b += [0] * (na + pad)
	fwht(a)
	fwht(b)
	c = [i*j for i, j in zip(a, b)]
	fwht(c)
	print(na + nb)
	print(*(i//4 for i in c))
