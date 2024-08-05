N = int(input())
s = 0
for _ in range(N):
	x, y = map(int, input().split())
	s += y-x
print(s/N)