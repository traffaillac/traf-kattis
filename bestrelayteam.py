R = []
n = int(input())
for _ in range(n):
	name, a, b = input().split()
	R.append((float(b), float(a), name))
R.sort()
T = 80
for a in range(n):
	b,c,d,*_ = (i for i in range(n) if i!=a)
	t = R[a][1]+R[b][0]+R[c][0]+R[d][0]
	if t<T:
		T,A,B,C,D = t,a,b,c,d
print(T)
print(R[A][2])
print(R[B][2])
print(R[C][2])
print(R[D][2])
