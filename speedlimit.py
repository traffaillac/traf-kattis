while True:
	n = int(input())
	if n < 0: break
	d, l = 0, 0
	for _ in range(n):
		s, t = map(int, input().split())
		d += s * (t - l)
		l = t
	print(d, "miles")
