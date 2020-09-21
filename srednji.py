N, B = map(int, input().split())
A = [int(a) for a in input().split()]
right = [0] * N
offset = 0
for a in A:
	right[offset] += 1
	if a == B:
		left = right
		right = [0] * N
	else:
		offset += 1 if a > B else -1
right[offset] += 1
print(sum(l * r for l, r in zip(left, right)))
