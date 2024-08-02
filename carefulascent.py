x, y = map(int, input().split())
X = y # final position if initial velocity is 1 km/min
for _ in range(int(input())):
	l, u, f = input().split()
	X += (int(u)-int(l)) * (float(f)-1)
print(x/X)