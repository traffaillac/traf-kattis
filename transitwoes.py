s, t, n = map(int, input().split())
D = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
for i in range(n):
	s += D[i]
	s = (s + C[i] - 1) // C[i] * C[i]
	s += B[i]
s += D[-1]
print("yes" if s <= t else "no")
