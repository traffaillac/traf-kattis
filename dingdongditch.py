N, Q = map(int, input().split())
A = [0]
for a in sorted(map(int, input().split())):
	A.append(A[-1]+a)
for b in input().split():
	print(A[int(b)])