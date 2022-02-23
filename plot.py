try:
	from math import comb
except:
	from math import factorial
	def comb(n, k):
		return factorial(n) // (factorial(k) * factorial(n - k))

n, *A = map(int, input().split())
C = [A[-1]] * (n+1)
for i in range(1, n+1):
	p = sum(A[-1-j]*i**j for j in range(n+1))
	C[i] = p - sum(comb(i, j)*C[j] for j in range(i))
print(" ".join(map(str, C)))
