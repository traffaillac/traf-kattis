from collections import defaultdict
i = 0
while True:
	n = int(input())
	if n==0: break
	i += 1
	A = defaultdict(lambda:0)
	for _ in range(n):
		A[input().split()[-1].lower()] += 1
	print(f"List {i}:")
	for a, c in sorted(A.items()):
		print(a, '|', c)