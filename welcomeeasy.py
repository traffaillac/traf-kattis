from itertools import combinations

jam = tuple('welcome to code jam')
for t in range(int(input())):
	c = 0
	for s in combinations(input(), 19):
		c += (s == jam)
	print(f'Case #{t+1}: {c:0>4}')
