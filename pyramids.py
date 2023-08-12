from bisect import bisect

H = []
i, h = 1, 1
while h <= 100_000_000:
	H.append(h)
	i += 2
	h += i * i
print(bisect(H, int(input())))
