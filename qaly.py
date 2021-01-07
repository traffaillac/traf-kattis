N = int(input())
qaly = 0.0
for _ in range(N):
	q, y = map(float, input().split())
	qaly += q * y
print(qaly)
