from collections import deque

isprime = [True] * 10000
isprime[0] = isprime[1] = False
p = 2
while p < 100:
	if isprime[p]:
		for q in range(p*p, 10000, p):
			isprime[q] = False
	p += 1

for _ in range(int(input())):
	start, end = map(int, input().split())
	seen = [False] * 10000
	fifo = deque([(start, 0)])
	seen[start] = True
	while fifo:
		p, cost = fifo.popleft()
		if p == end:
			print(cost)
			break
		for exp in range(4):
			for digit in range(10):
				if exp==3 and digit==0:
					continue
				q = p + (digit-(p//10**exp%10))*10**exp
				if not seen[q] and isprime[q]:
					seen[q] = True
					fifo.append((q, cost+1))
	else:
		print('Impossible')
