h, k, v, s = map(int, input().split())
d = 0
while h > 0:
	v += s
	v -= max(1, v//10)
	h += v >= k
	h -= 0 < v < k
	if h == 0: v = 0
	if v <= 0: h, v = 0, 0
	d += v
	s -= s > 0
print(d)
