N, K, Q = map(int, input().split())
for q in range(Q):
	# parent: (i + K - 2) // K
	x, y = map(int, input().split())
	if K == 1:
		print(abs(x - y))
		continue
	steps = 0
	while x != y:
		if x < y:
			x, y = y, x
		x = (x + K - 2) // K
		steps += 1
	print(steps)
