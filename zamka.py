def digitsum(x):
	sum = 0
	while x != 0:
		sum += x % 10
		x //= 10
	return sum

L = int(input())
D = int(input())
X = int(input())

N = 0
M = 0
for i in range(L, D + 1):
	if digitsum(i) == X:
		if N == 0:
			N = i
		M = i

print(N)
print(M)
