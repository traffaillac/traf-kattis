V = [*map(int, input().split())]
P = [2, 3, 5, 7, 11, 13, 17, 19]
a, b = 0, 1
for v, p in zip(V, P):
	a += v * b
	b *= p
print(2*3*5*7*11*13*17*19-a-1)