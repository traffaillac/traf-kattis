N = int(input())
m,s = 0,0
for _ in range(N):
	M,S = (int(i) for i in input().split())
	m += M
	s += S
print(s/m/60 if s/m>60 else "measurement error")
