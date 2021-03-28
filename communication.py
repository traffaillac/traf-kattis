input()
B = [int(b) for b in input().split()]
for i, b in enumerate(B):
	res = 0
	for j in range(8):
		res |= (b ^ (res << 1)) & (1 << j)
	B[i] = res
print(" ".join(map(str, B)))
