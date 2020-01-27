T = int(input())
for t in range(T):
	d = int(input())
	print(8 * pow(9, d - 1, 1000000007) % 1000000007)
