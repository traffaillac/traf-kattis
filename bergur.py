N = int(input())
A = [*map(int, input().split())]
m = 10000
s = 0
for a in reversed(A):
	m = min(m, a)
	s += m
print(s)