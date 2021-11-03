A, B = input().split()
i, j = next((i, B.index(a)) for i, a in enumerate(A) if a in B)
for y in range(len(B)):
	for x in range(len(A)):
		print(A[x] if y == j else B[y] if x == i else '.', end='')
	print()
