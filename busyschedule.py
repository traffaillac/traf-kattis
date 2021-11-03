first = True
while True:
	n = int(input())
	if n == 0: break
	if not first: print()
	first = False
	times = []
	for _ in range(n):
		hm, z = input().split()
		h, m = map(int, hm.split(':'))
		times.append((12 * 60 if z == "p.m." else 0) + h % 12 * 60 + m)
	times.sort()
	for t in times:
		print(f"{(t // 60 - 1) % 12 + 1}:{t % 60:02d} {'a' if t < 12*60 else 'p'}.m.")
