N = int(input())
M = int(input())
while N > 0 or M > 0:
	n = N % 10
	m = M % 10
	if n >= m:
		top = top * 10 + n
	if m >= n:
		bot = bot * 10 + m
	
	N = N // 10
	M = M // 10
