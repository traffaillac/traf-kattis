from itertools import accumulate

n = int(input())
A = [int(i) for i in input().split()]
M = list(accumulate(A, max))
m = list(accumulate(reversed(A), min))
pivots = 0
for i, a in enumerate(A):
	if (i==0 or a>=M[i-1]) and (i==n-1 or a<m[n-2-i]):
		pivots += 1
print(pivots)
