numbers = set()
for N in range(1, 64):
	for M in range(1, 63):
		for num in range(1, 64):
			A = (num + 1) // 2
			B = num // 2
			if A * N + B * M <= 63:
				sheldon = 0
				for i in range(num):
					if i % 2 == 0:
						sheldon = ((sheldon + 1) << N) - 1
					else:
						sheldon <<= M
				numbers.add(sheldon)
X, Y = map(int, input().split())
print(sum(X <= s <= Y for s in numbers))
