n = int(input())
W = [1, 1, 2]
for l in range(3, n+1):
	W.append(W[l-3]+W[l-2]+W[l-1])
print(W[n])