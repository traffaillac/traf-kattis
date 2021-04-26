n = int(input())
C = [1] * (n+1)
for i in range(n):
	C[i+1] = C[i] * 2 * (2*i+1) // (i+2)
print(sum(C[k]*C[n-k] for k in range(n+1)))
