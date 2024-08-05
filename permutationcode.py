while True:
	x = int(input())
	if x==0: break
	S = input()
	P = input()
	C = input()
	n = len(C)
	d = int(n**1.5+x)%n
	M = [P[S.index(C[d])]]*n
	for i in range(1, n):
		j = (d-i)%n
		M[j] = P[S.index(C[j])^S.index(M[(j+1)%n])]
	print(''.join(M))