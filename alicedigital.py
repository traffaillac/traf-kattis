for _ in range(int(input())):
	_, m = map(int, input().split())
	N = [[0]]
	for v in map(int, input().split()):
		if v < m:
			N.append([0])
		elif v == m:
			N[-1].append(0)
		else:
			N[-1][-1] += v
	res = 0
	for n in N:
		for i in range(len(n) - 1):
			res = max(res, n[i]+n[i+1]+m)
	print(res)
