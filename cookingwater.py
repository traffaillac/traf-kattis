A, B = 0, 1000
for _ in range(int(input())):
	a, b = map(int, input().split())
	A, B = max(A, a), min(B, b)
print("edward is right" if A>B else "gunilla has a point")