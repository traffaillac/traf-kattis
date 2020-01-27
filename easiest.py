def digitsum(i):
	s = 0
	while i > 0:
		s += i % 10
		i //= 10
	return s

while True:
	N = int(input())
	if N == 0:
		break
	S = digitsum(N)
	for p in range(11, 101):
		if digitsum(N * p) == S:
			print(p)
			break
